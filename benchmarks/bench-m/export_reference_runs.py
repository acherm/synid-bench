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
ENTRIES = {
    "linguist": {"name": "GitHub Linguist (heuristics for .m)", "kind": "other-identifier",
                 "note": "Linguist's content heuristics for `.m`; abstains when no rule fires"},
    "pygments": {"name": "Pygments (guess_lexer_for_filename)", "kind": "other-identifier",
                 "note": "always answers among the lexers registered for `.m`"},
    "ours_v1": {"name": "PL-ultimate-llm .m study rules (v1)", "kind": "other-identifier",
                "note": "rules written for the study before any judge label was seen (prospective)"},
    "ours": {"name": "PL-ultimate-llm .m study rules (v2)", "kind": "other-identifier",
             "note": "v1 tuned on the judges' labels of the study's first 300 uniformly sampled files — "
                     "12 of the 54 cases are among them, so this entry is partly in-sample"},
    "judge": {"name": "LLM judge: Claude Sonnet 4.6", "kind": "llm-judge",
              "note": "blind (bytes, file name, path, repository); used to cross-check the ground truth"},
    "judge2": {"name": "LLM judge: Gemini 3.8 Flash", "kind": "llm-judge",
               "note": "blind (bytes, file name, path, repository); used to cross-check the ground truth"},
}


def main() -> int:
    with (HERE / "cases.csv").open(encoding="utf-8") as f:
        cases = list(csv.DictReader(line for line in f if not line.startswith("#")))
    bench = (HERE / "cases.csv").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0]
    recs = load()
    out_dir = HERE / "entries"
    out_dir.mkdir(exist_ok=True)
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
