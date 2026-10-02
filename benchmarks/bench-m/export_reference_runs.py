#!/usr/bin/env python3
"""Export other identifiers' answers on bench-m as leaderboard entries (entries/).

The `.m` study of PL-ultimate-llm ran several identifiers on every file; their
answers on the benchmark's cases become runs in the benchmark's format, so they
rank next to Synid. Needs a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM, by
default a sibling of synid-bench).

    python3 benchmarks/bench-m/export_reference_runs.py

Answers are mapped to the names used in `accept` (Synid's names); Octave maps
to MATLAB, as the benchmark scores MATLAB and Octave as one family; an
abstention stays an abstention (no answer).
"""

from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PL = Path(os.environ.get("PL_ULTIMATE_LLM", HERE.parents[2] / "PL-ultimate-llm")).resolve()
sys.path.insert(0, str(PL))
from tools.m.data import load  # noqa: E402

NAME = {"objective-c": "Objective-C", "matlab": "MATLAB", "octave": "MATLAB", "matlab-family": "MATLAB",
        "mathematica-wolfram": "Wolfram Language", "mercury": "Mercury", "mumps-m": "M", "magma": "Magma",
        "limbo": "Limbo", "muf": "MUF", "mason": "Mason", "maple": "Maple", "scilab": "Scilab",
        "c-or-cpp": "C", "not-code": "Text", "other-programming-language": "Other"}
PLB = "https://github.com/acherm/PL-ultimate-llm/blob/swh-evidence-v1"
ENTRIES = {
    "ours_v1": {"name": "Hand-written .m rules v1 (prospective)", "kind": "specialised",
                "version": "m-reclass/1, PL-ultimate-llm commit eb988475",
                "about": "the rule cascade written for the .m study before any judge label existed: unambiguous "
                         "markers first (Mercury `:-`, Objective-C `@` directives, Wolfram package cells, MUMPS "
                         "routines, Magma/Maple terminators), then the MATLAB family; Octave only on Octave-only "
                         "syntax. Specific to .m — it knows .m-only languages Synid has no candidate for",
                "url": f"{PLB}/tools/m/reclassify_v1.py"},
    "ours": {"name": "Hand-written .m rules v2 (partly tuned on these files)", "kind": "specialised",
             "version": "m-reclass/2",
             "about": "v1 revised after reading 7 disagreements with the LLM judges on the study's first 300 "
                      "uniformly sampled files (Wolfram expressions; a fallback for marker-less MATLAB scripts); "
                      "12 of the 54 cases were among those 300",
             "url": f"{PLB}/tools/m/reclassify.py"},
    "linguist": {"name": "Linguist .m heuristics (rules only)", "kind": "other-identifier",
                 "version": "heuristics.yml `.m` block, as vendored by Hyperpolyglot / Synid",
                 "about": "a Python port of GitHub Linguist's seven `.m` disambiguation rules — first match wins; "
                          "no match = abstain (Linguist itself would then fall back to its Bayesian classifier)",
                 "url": f"{PLB}/tools/m/labellers.py"},
    "pygments": {"name": "Pygments guess_lexer_for_filename", "kind": "other-identifier",
                 "version": "Pygments 2.19.2",
                 "about": "the lexer Pygments picks among the four that claim *.m (Matlab, Octave, Objective-C, "
                          "Mason); always answers",
                 "url": "https://pygments.org/docs/api/#pygments.lexers.guess_lexer_for_filename"},
    "judge": {"name": "LLM judge: Claude Sonnet 4.6", "kind": "llm-judge",
              "version": "anthropic/claude-sonnet-4.6 via OpenRouter, temperature 0, schema m-judge/1",
              "about": "blind: sees the bytes, file name, path and repository, no other label",
              "url": f"{PLB}/tools/m/judge.py"},
    "judge2": {"name": "LLM judge: Gemini 3.8 Flash", "kind": "llm-judge",
               "version": "google/gemini-3.8-flash via OpenRouter, temperature 0, schema m-judge/1",
               "about": "blind: sees the bytes, file name, path and repository, no other label",
               "url": f"{PLB}/tools/m/judge.py"},
}


# Jev (TypeSafe's lightweight decision model, via OpenRouter's Decisions API), run by the
# study on every .m file: data/derived/jev/m/<probe>.jsonl in PL-ultimate-llm.
JEV_NAME = {"matlab": "MATLAB", "objective-c": "Objective-C", "wolfram": "Wolfram Language", "magma": "Magma",
            "mercury": "Mercury", "mumps": "M", "limbo": "Limbo", "c": "C", "cpp": "C++", "maple": "Maple",
            "scilab": "Scilab"}
JEV_NOT_CODE = {"binary-or-garbled", "empty", "json-yaml", "key-value-config", "natural", "placeholder-text",
                "prose", "tabular-data", "xml-html"}
JEV_ENTRIES = {
    "langid": {"name": "Jev 1.13, content only", "probe": "langid",
               "about": "TypeSafe's lightweight decision model (OpenRouter's Decisions API), asked which of "
                        "63 labels the file is written in, "
                        "from its content only (no file name); ~0.3 s and ~$0.15 per 1,000 files. Its label set "
                        "was designed for the extension studies, so it includes the rare `.m` languages"},
    "langid_ext": {"name": "Jev 1.13, with file name", "probe": "langid_ext",
                   "about": "the same question, the file name shown as well"},
}


def export_jev(cases: list[dict], bench: str, out_dir: Path) -> None:
    for label, e in JEV_ENTRIES.items():
        last = {}
        src = PL / "data" / "derived" / "jev" / "m" / f"{e['probe']}.jsonl"
        for line in src.open(encoding="utf-8"):
            d = json.loads(line)
            if d.get("ok"):
                last[d["sha1_git"]] = d
        model = next(iter(last.values())).get("model", "typesafe/jev-1.13")
        with (out_dir / f"jev-{label}.jsonl").open("w", encoding="utf-8") as f:
            f.write(json.dumps({"meta": {"label": f"jev-{label}", "name": e["name"], "kind": "llm-light",
                                         "benchmark": bench, "version": f"{model}, probe jev-probe/1 `{e['probe']}`",
                                         "about": e["about"],
                                         "source": "stored decisions of the .m study (PL-ultimate-llm, "
                                                   "data/derived/jev/m, not in its public repository)"}}) + "\n")
            for c in cases:
                d = last.get(c["sha1_git"])
                ch = d["answers"]["language"]["choice"] if d else None
                ans = None if ch is None else ["Text"] if ch in JEV_NOT_CODE else [JEV_NAME.get(ch, "Other")]
                f.write(json.dumps({"case_id": c["case_id"], "answer": ans}) + "\n")
        print(f"jev-{label}: → {out_dir / f'jev-{label}.jsonl'}")


def main() -> int:
    with (HERE / "cases.csv").open(encoding="utf-8") as f:
        cases = list(csv.DictReader(line for line in f if not line.startswith("#")))
    bench = (HERE / "cases.csv").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0]
    recs = load()
    out_dir = HERE / "entries"
    out_dir.mkdir(exist_ok=True)
    export_jev(cases, bench, out_dir)
    # the ground truth itself, as a reference row: the human reviewer's label
    with (out_dir / "human.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": {"label": "human", "name": "Human reviewer (blind) — the ground truth",
                                     "kind": "ground-truth", "benchmark": bench,
                                     "version": "blind audit of the .m study, October 2026",
                                     "about": "the labels every entry is scored against: a reviewer read each file "
                                              "and its provenance, with no machine label shown; right on every case "
                                              "by definition. The two LLM judges agree with it on all 54",
                                     "url": f"{PLB}/docs/m_swh_study.md"}}) + "\n")
        for c in cases:
            f.write(json.dumps({"case_id": c["case_id"], "answer": [c["accept"].split(";")[0]]}) + "\n")
    for layer, meta in ENTRIES.items():
        path = out_dir / f"{layer}.jsonl"
        with path.open("w", encoding="utf-8") as f:
            f.write(json.dumps({"meta": {"label": layer, **meta, "benchmark": bench,
                                         "source": "PL-ultimate-llm .m study (stored labels)"}}) + "\n")
            for c in cases:
                lab = recs[c["sha1_git"]].lang(layer)
                f.write(json.dumps({"case_id": c["case_id"],
                                    "answer": [NAME.get(lab, "Other")] if lab and lab not in ("unknown", "unresolved")
                                    else None}) + "\n")
        print(f"{layer}: → {path.relative_to(HERE.parents[2])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
