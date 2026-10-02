#!/usr/bin/env python3
"""Ask Jev — TypeSafe's lightweight decision model, through OpenRouter's Decisions
API — which language each case is written in, choosing among *all* of GitHub
Linguist's languages (a generic list, not one tailored to a benchmark), and
record the answers as a leaderboard entry.

    python3 tools/jev_linguist.py benchmarks/bench-m --limit 1          # one call, to check
    python3 tools/jev_linguist.py benchmarks/bench-m                    # content only
    python3 tools/jev_linguist.py benchmarks/bench-m --with-filename    # file name shown too
    python3 tools/jev_linguist.py benchmarks/bench-linguist --workers 8 # resumable (.work/jev/)

The question mirrors the `langid` probe of the PL-ultimate-llm extension studies
(same wording, content truncated to 16,000 characters); only the options change:
the 804 names of Linguist's languages.yml (`tools/data/linguist_languages.json`),
each described mechanically by its Linguist type and aliases. The answer is the
chosen language's name; with --non-code-as-text, answers of type data / markup /
prose become `Text` (for a benchmark whose labels say "not code", like bench-m).

The Decisions API accepts at most 255 choices per question, so the choice is a
knockout: the list, shuffled with a fixed seed, is split into 4 groups of ~200
(each with "none of these"); Jev picks one per group, then a final picks among
the groups' winners. All groups answering "none" = no answer.

Any server speaking the same decision API works: --endpoint points elsewhere,
e.g. a local llama.cpp server with an open decision model (`/v1/systemone`,
TypeSafe-compatible), where the 4 groups go in one request (the questions of a
request are answered independently; the file is encoded once):

    llama-server -m Kev-4B-Q8_0.gguf --port 8080
    python3 tools/jev_linguist.py benchmarks/bench-linguist \
        --endpoint http://127.0.0.1:8080/v1/systemone --model kev-4b --name "Kev-4B (local)" --label kev-linguist

OpenRouter needs OPENROUTER_API_KEY (environment, or ~/.openrouter_env). Writes
<bench>/entries/<label>.jsonl and a log of the decisions (choice, top-5
probabilities, cost) in <bench>/entries/raw/<label>.jsonl.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINGUIST = HERE / "data" / "linguist_languages.json"
URL = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"
MAX_CHARS = 16000
MAX_CHOICES = 255
GROUPS = 4
NONE = "none of these"
SEED = 20261002
INSTRUCTIONS = ("Which programming language, notation or kind of content is this file written in? "
                "Judge from the content itself.")


def api_key() -> str:
    k = os.environ.get("OPENROUTER_API_KEY")
    if k:
        return k
    f = Path.home() / ".openrouter_env"
    if f.exists():
        for line in f.read_text().splitlines():
            if "OPENROUTER_API_KEY=" in line:
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("OPENROUTER_API_KEY not set (environment or ~/.openrouter_env)")


def decide(state: str, questions: dict, key: str | None, url: str = URL, model: str = MODEL) -> dict:
    body = json.dumps({"model": model, "state": state, "questions": questions}).encode("utf-8")
    headers = {"Content-Type": "application/json", "X-Title": "synid-bench (Jev with Linguist's languages)"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    last = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=headers), timeout=600) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}"
            if e.code not in (408, 429, 500, 502, 503, 520, 524, 529):
                raise SystemExit(last)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = str(e)
        time.sleep(min(30, 2 * 2 ** attempt))
    raise SystemExit(f"Decisions API failed: {last}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bench", type=Path)
    ap.add_argument("--with-filename", action="store_true")
    ap.add_argument("--limit", type=int, help="only the first N cases (a check; writes nothing)")
    ap.add_argument("--workers", type=int, default=4, help="parallel cases (each is 4–5 sequential calls)")
    ap.add_argument("--non-code-as-text", action="store_true",
                    help="answers of Linguist type data/markup/prose become `Text`")
    ap.add_argument("--endpoint", default=URL, help="decision API URL (default: OpenRouter)")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--name", default="Jev 1.13", help="entry name prefix")
    ap.add_argument("--label", default="jev-linguist", help="entry label prefix")
    ap.add_argument("--shuffle", action="store_true", help="ask the cases in a fixed random order")
    a = ap.parse_args()
    bench = a.bench.resolve()
    with (bench / "cases.csv").open(encoding="utf-8") as f:
        cases = list(csv.DictReader(line for line in f if not line.startswith("#")))
    version = (bench / "cases.csv").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0]
    ling = json.loads(LINGUIST.read_text(encoding="utf-8"))
    kind_of = {l["name"]: l["type"] for l in ling["languages"]}
    criteria = {l["name"]: (f"{l['name']} — {l['type'] or 'language'}"
                            + (f"; also: {', '.join(l['aliases'][:4])}" if l["aliases"] else ""))
                for l in ling["languages"]}
    names = sorted(criteria)
    random.Random(SEED).shuffle(names)
    groups = [names[i::GROUPS] for i in range(GROUPS)]
    assert all(len(g) + 1 <= MAX_CHOICES for g in groups)

    remote = a.endpoint.startswith("https://openrouter.ai")
    key = api_key() if remote else None

    def question(options: list[str], with_none: bool) -> dict:
        crit = {n: criteria[n] for n in options}
        if with_none:
            crit[NONE] = "none of the options above fits this file"
        return {"type": "choice", "instructions": INSTRUCTIONS, "criteria": crit}

    def ask(state: str, options: list[str], with_none: bool) -> tuple[str | None, dict, float, str]:
        out = decide(state, {"language": question(options, with_none)}, key, a.endpoint, a.model)
        ans = (out.get("answers") or {}).get("language") or {}
        return ans.get("choice"), ans.get("probabilities") or {}, float((out.get("usage") or {}).get("cost") or 0), \
            out.get("model") or a.model

    def ask_groups(state: str) -> tuple[list[str], float, str]:
        """The first round: one request per group (OpenRouter), or all groups in one request (local)."""
        if remote:
            winners, cost, model = [], 0.0, a.model
            for g in groups:
                ch, _, co, model = ask(state, g, with_none=True)
                cost += co
                if ch and ch != NONE:
                    winners.append(ch)
            return winners, cost, model
        out = decide(state, {f"group{i}": question(g, True) for i, g in enumerate(groups)}, key, a.endpoint, a.model)
        answers = out.get("answers") or {}
        winners = [answers[f"group{i}"]["choice"] for i in range(len(groups))
                   if (answers.get(f"group{i}") or {}).get("choice") not in (None, NONE)]
        return winners, 0.0, out.get("model") or a.model

    label = a.label + ("-filename" if a.with_filename else "")
    todo = cases[: a.limit] if a.limit else cases
    cache = bench / ".work" / "jev" / f"{label}.jsonl"
    done: dict[str, dict] = {}
    if not a.limit and cache.exists():
        for line in cache.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            done[r["case_id"]] = r
    lock = threading.Lock()
    cache.parent.mkdir(parents=True, exist_ok=True)

    def one(c: dict) -> dict:
        raw = (bench / "files" / c["sha1_git"]).read_bytes().decode("utf-8", "replace")
        trunc = len(raw) > MAX_CHARS
        body = (f"File content{' [truncated to the first %d characters]' % MAX_CHARS if trunc else ''}:\n"
                f"```\n{raw[:MAX_CHARS]}\n```")
        state = (f"Filename: {c['filename']}\n\n" + body) if a.with_filename else body
        winners, c_cost, model = ask_groups(state)
        probs = {}
        if len(winners) > 1:
            choice, probs, co, model = ask(state, winners, with_none=False)
            c_cost += co
        else:
            choice = winners[0] if winners else None
        r = {"case_id": c["case_id"], "choice": choice, "type": kind_of.get(choice, ""),
             "group_winners": winners, "final_top5": sorted(probs.items(), key=lambda kv: -kv[1])[:5],
             "cost": c_cost, "model": model, "truncated": trunc}
        if not a.limit:
            with lock, cache.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        return r

    pending = [c for c in todo if c["case_id"] not in done]
    if a.shuffle:  # a long run, stopped at any time, has then answered a random sample
        random.Random(SEED).shuffle(pending)
    print(f"{len(todo)} cases, {len(done)} already answered, {len(pending)} to ask")
    t0, n = time.time(), 0
    with ThreadPoolExecutor(max_workers=max(1, a.workers)) as ex:
        for r in ex.map(one, pending):
            done[r["case_id"]] = r
            n += 1
            if n % 100 == 0 or a.limit:
                spent = sum(x["cost"] for x in done.values())
                print(f"{n}/{len(pending)}  {time.time() - t0:.0f}s  ${spent:.3f} so far", flush=True)
    rows = [done[c["case_id"]] for c in todo]
    cost = sum(r["cost"] for r in rows)
    print(f"total cost ${cost:.4f} for {len(todo)} file(s)")
    if a.limit:
        return 0
    (bench / "entries" / "raw").mkdir(parents=True, exist_ok=True)
    with (bench / "entries" / "raw" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    meta = {"label": label, "kind": "llm-light", "benchmark": version,
            "name": f"{a.name}, Linguist's 804 languages" + (", with file name" if a.with_filename else ", content only"),
            "version": (f"{rows[0]['model'] if rows else a.model}, "
                        + ("OpenRouter Decisions API" if remote else f"local decision API ({a.endpoint})")),
            "about": (("TypeSafe's lightweight decision model" if remote else f"the decision model {a.model}, run "
                       "locally,") + " asked which of GitHub Linguist's 804 languages the file "
                      "is written in — a generic list, not one tailored to this benchmark (knockout: 4 groups of "
                      "~200 with \"none of these\", then a final, as the API allows 255 choices)"
                      + ("; data / markup / prose answers count as not code" if a.non_code_as_text else "")
                      + f". {len(rows)} files, ${cost:.4f}"),
            "date": time.strftime("%Y-%m-%d")}
    with (bench / "entries" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": meta}) + "\n")
        for r in rows:
            non_code = a.non_code_as_text and r["type"] in ("data", "markup", "prose")
            ans = None if not r["choice"] else ["Text"] if non_code else [r["choice"]]
            f.write(json.dumps({"case_id": r["case_id"], "answer": ans}) + "\n")
    print(f"→ {bench / 'entries' / (label + '.jsonl')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
