#!/usr/bin/env python3
"""Ask a local language model (through Ollama) the language of each case → a
leaderboard entry.

    ollama pull starcoder2:3b
    python3 tools/ollama_llm.py benchmarks/bench-linguist --model starcoder2:3b

A base (completion) model is not asked a question but given a text to continue:
the first 2,000 characters of the file, then

    Question: Which programming language is the code above written in?
    Answer: The code above is written in

decoded greedily (temperature 0, seed 0, 12 tokens, raw prompt — no chat
template). The answer is the continuation up to the first period, comma,
parenthesis or line break, matched to a Linguist language by name or alias
(case, spaces and punctuation ignored); an answer matching none is kept as it
is (and counts as wrong). The file name is never shown. The model's digest is
recorded in the entry. Resumable: answers accumulate in <bench>/.work/llm/.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from score import name_key, read_cases  # noqa: E402

OLLAMA = "http://127.0.0.1:11434"
CHARS = 2000
SUFFIX = ("\n\nQuestion: Which programming language is the code above written in?\n"
          "Answer: The code above is written in")
OPTIONS = {"temperature": 0, "seed": 0, "num_predict": 12, "num_ctx": 4096}
PROMPT_VERSION = "llm-prompt/1"


def post(path: str, body: dict) -> dict:
    req = urllib.request.Request(OLLAMA + path, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def linguist_names() -> dict[str, str]:
    data = json.loads((HERE / "data" / "linguist_languages.json").read_text(encoding="utf-8"))
    out = {}
    for lang in data["languages"]:
        for n in [lang["name"], *lang["aliases"]]:
            out.setdefault(name_key(n), lang["name"])
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bench", type=Path)
    ap.add_argument("--model", default="starcoder2:3b")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--name", help="display name (default: the model tag)")
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    bench = a.bench.resolve()
    cases = list(read_cases(bench).values())[: a.limit] if a.limit else list(read_cases(bench).values())
    tags = {m["name"]: m for m in json.loads(urllib.request.urlopen(OLLAMA + "/api/tags").read())["models"]}
    if a.model not in tags:
        raise SystemExit(f"{a.model} is not pulled (ollama pull {a.model})")
    digest = tags[a.model]["digest"]
    names = linguist_names()
    label = "llm-" + re.sub(r"[^\w.-]", "-", a.model)
    cache = bench / ".work" / "llm" / f"{label}.jsonl"
    cache.parent.mkdir(parents=True, exist_ok=True)
    done = {}
    if cache.exists() and not a.limit:
        for line in cache.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r.get("digest") == digest:
                done[r["case_id"]] = r

    def one(c: dict) -> dict:
        text = (bench / "files" / c["sha1_git"]).read_bytes().decode("utf-8", "replace")[:CHARS]
        out = post("/api/generate", {"model": a.model, "prompt": text + SUFFIX, "raw": True, "stream": False,
                                     "options": OPTIONS})
        cont = out.get("response", "")
        said = re.split(r"[.,(\n]", cont.strip(), maxsplit=1)[0].strip().strip("`*\"'")
        return {"case_id": c["case_id"], "continuation": cont, "said": said, "digest": digest}

    pending = [c for c in cases if c["case_id"] not in done]
    print(f"{len(cases)} cases, {len(done)} cached, {len(pending)} to ask ({a.model} {digest[:12]})", flush=True)
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for n, r in enumerate(ex.map(one, pending), 1):
            done[r["case_id"]] = r
            if not a.limit:
                with cache.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
            if n % 200 == 0 or a.limit:
                print(f"{n}/{len(pending)} {time.time() - t0:.0f}s  {r['said']!r}", flush=True)
    if a.limit:
        return 0
    meta = {"label": label, "kind": "llm-light", "benchmark": (bench / "cases.csv").read_text(encoding="utf-8")
            .splitlines()[0].lstrip("# ").split(" —")[0],
            "name": f"{a.name or a.model} (local, completion prompt), content only",
            "version": f"ollama {a.model} @ {digest[:12]}, {PROMPT_VERSION}",
            "about": (f"a local language model continuing the first {CHARS} characters of the file followed by "
                      "\"Question: Which programming language is the code above written in? Answer: The code above "
                      "is written in\" (greedy, 12 tokens; tools/ollama_llm.py); the answer is matched to a Linguist "
                      "language by name or alias"),
            "date": time.strftime("%Y-%m-%d")}
    (bench / "entries" / "raw").mkdir(parents=True, exist_ok=True)
    with (bench / "entries" / "raw" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps(done[c["case_id"]], ensure_ascii=False) + "\n")
    with (bench / "entries" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": meta}) + "\n")
        for c in cases:
            said = done[c["case_id"]]["said"]
            ans = [names.get(name_key(said), said)] if said else None
            f.write(json.dumps({"case_id": c["case_id"], "answer": ans}) + "\n")
    print(f"→ {bench / 'entries' / (label + '.jsonl')} ({time.time() - t0:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
