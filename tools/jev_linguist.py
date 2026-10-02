#!/usr/bin/env python3
"""Ask Jev — TypeSafe's lightweight decision model, through OpenRouter's Decisions
API — which language each case is written in, choosing among *all* of GitHub
Linguist's languages (a generic list, not one tailored to a benchmark), and
record the answers as a leaderboard entry.

    python3 tools/jev_linguist.py benchmarks/bench-m --limit 1          # one call, to check
    python3 tools/jev_linguist.py benchmarks/bench-m                    # content only
    python3 tools/jev_linguist.py benchmarks/bench-m --with-filename    # file name shown too

The question mirrors the `langid` probe of the PL-ultimate-llm extension studies
(same wording, content truncated to 16,000 characters); only the options change:
the 804 names of Linguist's languages.yml (`tools/data/linguist_languages.json`),
each described mechanically by its Linguist type and aliases. Answers of type
data / markup / prose count as "not code" (`Text`).

The Decisions API accepts at most 255 choices per question, so the choice is a
knockout: the list, shuffled with a fixed seed, is split into 4 groups of ~200
(each with "none of these"); Jev picks one per group, then a final picks among
the groups' winners. All groups answering "none" = no answer.

Needs OPENROUTER_API_KEY (environment, or ~/.openrouter_env). Writes
<bench>/entries/<label>.jsonl and a log of the decisions (choice, top-5
probabilities, cost) in <bench>/entries/raw/<label>.jsonl.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import time
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


def decide(state: str, questions: dict, key: str) -> dict:
    body = json.dumps({"model": MODEL, "state": state, "questions": questions}).encode("utf-8")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json",
               "X-Title": "synid-bench (Jev with Linguist's languages)"}
    last = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(URL, data=body, headers=headers), timeout=120) as r:
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

    def ask(state: str, options: list[str], with_none: bool) -> tuple[str | None, dict, float, str]:
        crit = {n: criteria[n] for n in options}
        if with_none:
            crit[NONE] = "none of the options above fits this file"
        out = decide(state, {"language": {"type": "choice", "instructions": INSTRUCTIONS, "criteria": crit}}, key)
        ans = (out.get("answers") or {}).get("language") or {}
        return ans.get("choice"), ans.get("probabilities") or {}, float((out.get("usage") or {}).get("cost") or 0), \
            out.get("model") or MODEL
    key = api_key()
    label = "jev-linguist" + ("-filename" if a.with_filename else "")
    todo = cases[: a.limit] if a.limit else cases
    rows, cost = [], 0.0
    for i, c in enumerate(todo, 1):
        raw = (bench / "files" / c["sha1_git"]).read_bytes().decode("utf-8", "replace")
        trunc = len(raw) > MAX_CHARS
        body = (f"File content{' [truncated to the first %d characters]' % MAX_CHARS if trunc else ''}:\n"
                f"```\n{raw[:MAX_CHARS]}\n```")
        state = (f"Filename: {c['filename']}\n\n" + body) if a.with_filename else body
        winners, c_cost, model = [], 0.0, MODEL
        for g in groups:
            ch, _, co, model = ask(state, g, with_none=True)
            c_cost += co
            if ch and ch != NONE:
                winners.append(ch)
        probs = {}
        if len(winners) > 1:
            choice, probs, co, model = ask(state, winners, with_none=False)
            c_cost += co
        else:
            choice = winners[0] if winners else None
        top = sorted(probs.items(), key=lambda kv: -kv[1])[:5]
        cost += c_cost
        rows.append({"case_id": c["case_id"], "choice": choice, "type": kind_of.get(choice, ""),
                     "group_winners": winners, "final_top5": top, "cost": c_cost, "model": model,
                     "truncated": trunc})
        print(f"{i}/{len(todo)} {c['filename'][:36]:36} {c['expected']:20} → {choice} "
              f"({kind_of.get(choice, '?')}) from {winners}  ${c_cost:.5f}")
    print(f"total cost ${cost:.4f} for {len(todo)} call(s)")
    if a.limit:
        return 0
    (bench / "entries" / "raw").mkdir(parents=True, exist_ok=True)
    with (bench / "entries" / "raw" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    meta = {"label": label, "kind": "llm-light", "benchmark": version,
            "name": "Jev 1.13, Linguist's 804 languages" + (", with file name" if a.with_filename else ", content only"),
            "version": f"{rows[0]['model'] if rows else MODEL}, OpenRouter Decisions API",
            "about": ("TypeSafe's lightweight decision model asked which of GitHub Linguist's 804 languages the file "
                      "is written in — a generic list, not one tailored to this benchmark (knockout: 4 groups of "
                      "~200 with \"none of these\", then a final, as the API allows 255 choices); data / markup / "
                      f"prose answers count as not code. {len(rows)} files, ${cost:.4f}"),
            "date": time.strftime("%Y-%m-%d")}
    with (bench / "entries" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": meta}) + "\n")
        for r in rows:
            ans = None if not r["choice"] else ["Text"] if r["type"] in ("data", "markup", "prose") else [r["choice"]]
            f.write(json.dumps({"case_id": r["case_id"], "answer": ans}) + "\n")
    print(f"→ {bench / 'entries' / (label + '.jsonl')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
