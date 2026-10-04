#!/usr/bin/env python3
"""Why does Jev beat Kev? An experiment on a fixed sample of bench-linguist.

    llama-server -m Kev-4B-Q8_0.gguf --port 8091 -c 65536 -b 4096 -ub 1024 -fa on -ngl 99
    python3 benchmarks/bench-linguist/analysis/kev_order_experiment.py

Hypothesis (from the stored runs): with ~200 options per question, Kev favours the options
listed first — its wrong answers are the first options of their groups (Ecere Projects, Move:
position 0), and languages listed last (Swift: 198 of 201) are rarely chosen. Variants, each on
the same sample (100 files Jev gets right and Kev wrong + 50 both get right, seed 20261003):

- `original`  — the stored run (4 groups of ~200 in a fixed shuffled order, then a final);
- `reversed`  — the same groups, each listed in reverse order;
- `small`     — 16 groups of ~50 options (same shuffle), then a final among the winners;
- `cascade`   — PL-ultimate-llm's candidates for the file's extension (tools/data/pl_candidates.json,
                as tools/jev_cascade.py), with the file name not shown; Linguist knockout if none fits.

Same question, same 16,000-character truncation, content only. Results → kev_order_experiment.jsonl
(one line per file and variant, resumable) and a summary printed at the end.
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BENCH = HERE.parent
ROOT = BENCH.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(BENCH))
from jev_linguist import INSTRUCTIONS, MAX_CHARS, NONE, decide  # noqa: E402
from root_causes import candidates  # noqa: E402
from score import name_key, outcome, read_cases  # noqa: E402

URL = "http://127.0.0.1:8091/v1/systemone"
MODEL = "kev-4b-q8_0"
OUT = HERE / "kev_order_experiment.jsonl"
SEED = 20261003
TEXT = "Text"


def main() -> int:
    cases = read_cases(BENCH)
    raw = {lab: {json.loads(line)["case_id"]: json.loads(line)
                 for line in (BENCH / "entries" / "raw" / f"{lab}.jsonl").read_text(encoding="utf-8").splitlines()}
           for lab in ("kev-linguist", "jev-linguist")}
    ok = lambda c, ch: outcome(c, [ch] if ch else None) == "right"  # noqa: E731
    jev_only = sorted(cid for cid, c in cases.items()
                      if ok(c, raw["jev-linguist"][cid]["choice"]) and not ok(c, raw["kev-linguist"][cid]["choice"]))
    both = sorted(cid for cid, c in cases.items()
                  if ok(c, raw["jev-linguist"][cid]["choice"]) and ok(c, raw["kev-linguist"][cid]["choice"]))
    rnd = random.Random(SEED)
    sample = [("jev-only", cid) for cid in rnd.sample(jev_only, 100)] + [("both", cid) for cid in rnd.sample(both, 50)]

    ling = json.loads((ROOT / "tools" / "data" / "linguist_languages.json").read_text(encoding="utf-8"))["languages"]
    crit = {lg["name"]: (f"{lg['name']} — {lg['type'] or 'language'}"
                         + (f"; also: {', '.join(lg['aliases'][:4])}" if lg["aliases"] else "")) for lg in ling}
    names = sorted(crit)
    random.Random(20261002).shuffle(names)          # the stored runs' order
    groups4 = [names[i::4] for i in range(4)]
    groups16 = [names[i::16] for i in range(16)]
    pl = json.loads((ROOT / "tools" / "data" / "pl_candidates.json").read_text(encoding="utf-8"))

    def ask(state: str, options: list[str], extra: dict[str, str], descr=None) -> str | None:
        c = {o: (descr or crit).get(o) for o in options} | extra
        out = decide(state, {"q": {"type": "choice", "instructions": INSTRUCTIONS, "criteria": c}}, None, URL, MODEL)
        return ((out.get("answers") or {}).get("q") or {}).get("choice")

    def knockout(state: str, groups: list[list[str]]) -> tuple[str | None, list[str]]:
        winners = [w for g in groups if (w := ask(state, g, {NONE: "none of the options above fits this file"}))
                   and w != NONE]
        if len(winners) > 1:
            return ask(state, winners, {}), winners
        return (winners[0] if winners else None), winners

    def cascade(state: str, case: dict) -> tuple[str | None, list[str]]:
        cand = candidates(case, pl)
        if cand:
            descr = {pl["languages"][p]["name"]: pl["languages"][p]["name"] for p in cand}
            ch = ask(state, list(descr), {TEXT: "plain text or data, not any of the languages above",
                                          NONE: "none of the options above fits this file"}, descr)
            if ch and ch != NONE:
                return ch, [pl["languages"][p]["name"] for p in cand]
        ch, w = knockout(state, groups4)
        return ch, w

    done = set()
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            done.add((r["case_id"], r["variant"]))
    for i, (stratum, cid) in enumerate(sample, 1):
        c = cases[cid]
        raw_text = (BENCH / "files" / c["sha1_git"]).read_bytes().decode("utf-8", "replace")
        trunc = len(raw_text) > MAX_CHARS
        state = (f"File content{' [truncated to the first %d characters]' % MAX_CHARS if trunc else ''}:\n"
                 f"```\n{raw_text[:MAX_CHARS]}\n```")
        for variant in ("reversed", "small", "cascade"):
            if (cid, variant) in done:
                continue
            if variant == "reversed":
                ch, w = knockout(state, [list(reversed(g)) for g in groups4])
            elif variant == "small":
                ch, w = knockout(state, groups16)
            else:
                ch, w = cascade(state, c)
            with OUT.open("a", encoding="utf-8") as f:
                f.write(json.dumps({"case_id": cid, "stratum": stratum, "variant": variant, "choice": ch,
                                    "winners": w, "right": ok(c, ch)}, ensure_ascii=False) + "\n")
        print(f"{i}/{len(sample)}", flush=True)

    rows = [json.loads(line) for line in OUT.read_text(encoding="utf-8").splitlines()]
    print("\nright answers per variant (100 files Jev gets right and Kev wrong | 50 both right):")
    for variant in ("original", "reversed", "small", "cascade"):
        for stratum in ("jev-only", "both"):
            ids = [cid for s, cid in sample if s == stratum]
            if variant == "original":
                n = sum(ok(cases[cid], raw["kev-linguist"][cid]["choice"]) for cid in ids)
            else:
                n = sum(1 for r in rows if r["variant"] == variant and r["stratum"] == stratum and r["right"])
            print(f"  {variant:9} {stratum:9} {n}/{len(ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
