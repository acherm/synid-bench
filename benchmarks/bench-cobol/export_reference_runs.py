#!/usr/bin/env python3
"""Export the COBOL study's other identifiers on bench-cobol as leaderboard entries (entries/):
its hand-written rules and Jev's two probes. Needs a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM;
Jev's decisions are local data of that checkout, not in its git). No API is called.

    python3 benchmarks/bench-cobol/export_reference_runs.py

The rules' labels map to names: cobol, cobol-generated and cobol-copybook → COBOL,
synthetic-placeholder → Text, comic-book-list → XML (when the file is a ReadingList; the binary
CCBridgeLibrary format is an abstention); other and binary-data are abstentions.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import study_cases as S  # noqa: E402

RULES = {"cobol": ["COBOL"], "cobol-generated": ["COBOL"], "cobol-copybook": ["COBOL"],
         "synthetic-placeholder": ["Text"], "comic-book-list": ["XML"]}


def main() -> int:
    S.check_checkout()
    _, cases = S.read_entries_cases(HERE)
    rules = {d["sha1_git"]: d["label"] for d in S.pinned_jsonl("data/derived/cobol_study/corpus_estimate.jsonl")}
    ans = {}
    for c in cases:
        lab = rules.get(c["sha1_git"])
        raw = (HERE / "files" / c["sha1_git"]).read_bytes()
        ans[c["sha1_git"]] = None if lab == "comic-book-list" and b"<ReadingList" not in raw else RULES.get(lab)
    S.write_entry(HERE, "ours", {
        "name": "Hand-written COBOL rules (tuned on these files)", "kind": "specialised",
        "scope": "written for `.cbl` / `.CBL` files only — bench-cobol's problem",
        "version": f"cobol-reclass (PL-ultimate-llm {S.PL_REV[:9]}, stored labels of corpus_estimate.jsonl)",
        "about": "the study's zero-cost content rules (divisions, PROGRAM-ID, level numbers with PIC, the WBC "
                 "stub sentence, ReadingList XML); written from the judge's labels on the study's files, and "
                 "the only reference of bench-cobol's rules-only cases",
        "url": f"{S.PL_BLOB}/tools/cobol/reclassify.py", "source": "PL-ultimate-llm COBOL study (stored labels)"},
        ans)
    S.export_jev(HERE, "cobol")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
