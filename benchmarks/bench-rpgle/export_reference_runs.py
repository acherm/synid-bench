#!/usr/bin/env python3
"""Export the `.rpgle` study's other identifiers on bench-rpgle as leaderboard entries (entries/):
its hand-written rules and Jev's two probes. Needs a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM;
Jev's decisions are local data of that checkout, not in its git). No API is called.

    python3 benchmarks/bench-rpgle/export_reference_runs.py

The rules' labels map to names: rpgle and rpgle-copybook → RPGLE, data and docs → Text; `other`
and `binary` are abstentions.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import study_cases as S  # noqa: E402

RULES = {"rpgle": ["RPGLE"], "rpgle-copybook": ["RPGLE"], "data": ["Text"], "docs": ["Text"]}


def main() -> int:
    S.check_checkout()
    reports = [json.loads(b) for b in S.pinned_dir("data/derived/rpgle_study/reports").values()]
    S.write_entry(HERE, "ours", {
        "name": "Hand-written .rpgle rules (frozen before these files)", "kind": "specialised",
        "scope": "written for `.rpgle` files only — bench-rpgle's problem",
        "version": f"rpgle-reclass v2 (PL-ultimate-llm {S.PL_REV[:9]}, stored labels)",
        "about": "the study's zero-cost content rules (spec letters in column 6, `**FREE`, `dcl-*`, `ctl-opt`, "
                 "free-form statements; copy members). Frozen after reading the judge's labels on the 326 files "
                 "of the tuning split, which bench-rpgle leaves out: on these files they are prospective",
        "url": f"{S.PL_BLOB}/tools/rpgle/reclassify.py", "source": "PL-ultimate-llm .rpgle study (stored labels)"},
        {r["sha1_git"]: RULES.get(r["reclass"]["label"]) for r in reports})
    S.export_jev(HERE, "rpgle")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
