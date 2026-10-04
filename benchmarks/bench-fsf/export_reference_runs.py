#!/usr/bin/env python3
"""Export the `.fsf` study's other identifiers on bench-fsf as leaderboard entries (entries/):
its hand-written rule and Jev's two probes. Needs a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM;
Jev's decisions are local data of that checkout, not in its git). No API is called.

    python3 benchmarks/bench-fsf/export_reference_runs.py

The rule's labels map to names: fsl-feat → Tcl (bench-fsf's name for a FEAT design), docs and data →
Text; config-other, other and binary are abstentions.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import study_cases as S  # noqa: E402

RULES = {"fsl-feat": ["Tcl"], "tcl-other": ["Tcl"], "docs": ["Text"], "data": ["Text"]}


def main() -> int:
    S.check_checkout()
    reports = [json.loads(b) for b in S.pinned_dir("data/derived/fsf_study/reports").values()]
    S.write_entry(HERE, "ours", {
        "name": "Hand-written .fsf rule (tuned on these files)", "kind": "specialised",
        "scope": "written for `.fsf` files only — bench-fsf's problem",
        "version": f"fsf-reclass (PL-ultimate-llm {S.PL_REV[:9]}, stored labels)",
        "about": "the study's zero-cost content rule: a file with a `set fmri(` line is a FEAT design; written "
                 "after reading the judge's labels on the study's files, these among them",
        "url": f"{S.PL_BLOB}/tools/fsf/reclassify.py", "source": "PL-ultimate-llm .fsf study (stored labels)"},
        {r["sha1_git"]: RULES.get(r["reclass"]["label"]) for r in reports})
    S.export_jev(HERE, "fsf")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
