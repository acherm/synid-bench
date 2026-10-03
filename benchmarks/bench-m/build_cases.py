#!/usr/bin/env python3
"""Build the Synid benchmark cases from the `.m` extension study of PL-ultimate-llm
(README.md). Needs a checkout of PL-ultimate-llm: $PL_ULTIMATE_LLM, by default
a sibling of the synid-bench checkout.

Writes `cases.csv` (one row per archived file, with the answers that count as
right) and `files/<sha1_git>` (the files' bytes, each verified against its
sha1_git). Re-run only to release a new benchmark version: cases are frozen so
that results stay comparable across Synid versions.

    python3 benchmarks/bench-m/build_cases.py

Cases are the files a human reviewed in the blind audit of the `.m` study
(with a usable label); the two LLM judges agree with the human on all of them.
Small and checked beats large and noisy: files labelled by the judges alone
are not included.
"""

from __future__ import annotations

import csv
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# the .m study lives in PL-ultimate-llm (its data and loaders are needed to build cases)
ROOT = Path(os.environ.get("PL_ULTIMATE_LLM", HERE.parents[2] / "PL-ultimate-llm")).resolve()  # sibling of synid-bench
sys.path.insert(0, str(ROOT))
from tools import study_export as SE  # noqa: E402
from tools.m import audit as A  # noqa: E402
from tools.m.data import J1, J2, load  # noqa: E402
sys.path.insert(0, str(HERE / "assessment"))
from synid_assess import NO_REF, fam  # noqa: E402  (this repository's assessment module)

VERSION = "bench-m/1"
CASES = HERE / "cases.csv"
FILES = HERE / "files"
FIELDS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
          "accept", "reference", "provenance", "frame", "stratum", "weight", "tags"]

# Synid answers that count as right, per language-level label. Names Synid does
# not (yet) offer for `.m` are listed too, so that a future version gets credit.
ACCEPT = {
    "matlab-family": ["MATLAB", "Octave"],  # the study labels the family; Octave accepted since 2026-10-03 "objective-c": ["Objective-C"], "mathematica-wolfram": ["Wolfram Language"],
    "mercury": ["Mercury"], "mumps-m": ["M"], "limbo": ["Limbo"], "muf": ["MUF"], "mason": ["Mason"],
    "magma": ["Magma"], "c-or-cpp": ["C", "C++"], "not-code": ["Text"], "other": [],
}
# Synid's candidates for `.m` (from Linguist), as of 9bc1c32
M_CANDIDATES = {"objective-c", "matlab-family", "mercury", "mumps-m", "mathematica-wolfram", "limbo", "muf", "mason"}


def tags(expected: str, raw: bytes) -> list[str]:
    t = []
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        t.append("non-utf8")
        text = raw.decode("utf-8", "replace")
    if expected == "matlab-family" and not re.search(r"(?m)^\s*%|^function|^!\w+", text):
        t.append("comment-free-matlab")          # nothing for Synid's MATLAB heuristics to see
    if expected == "objective-c" and not re.search(r"//|/\*", text):
        t.append("comment-free-objc")            # nothing for the comment strategy to recognise
    if expected == "objective-c" and re.search(r'@"[^"\n]*%', text):
        t.append("objc-format-string")           # `%` in @"…": the comment strategy may take it for MATLAB
    if expected not in M_CANDIDATES and expected != "not-code":
        t.append("out-of-candidates")             # not among Synid's candidates for `.m`
    if text.count("\n") < 3:
        t.append("tiny")
    return t


def main() -> int:
    recs = load()
    queue = {d["sha1_git"]: d for d in A.queue()}
    gold = [r for r in recs.values() if r.sha in queue and r.human_latest() and r.lang("judge") and r.lang("judge2")
            and r.human()["language"] not in NO_REF]
    n_h = {}
    for r in gold:
        n_h[queue[r.sha]["stratum"]] = n_h.get(queue[r.sha]["stratum"], 0) + 1
    FILES.mkdir(exist_ok=True)
    for f in FILES.iterdir():
        f.unlink()
    rows = []
    for r in sorted(gold, key=lambda r: r.sha):
        raw = SE.content_bytes("m", r.sha)
        if raw is None:
            print(f"skip {r.sha[:12]}: bytes unavailable")
            continue
        h = r.human()
        exp = fam(h["language"])
        d = queue[r.sha]
        rows.append({
            "case_id": f"m:{r.sha[:12]}", "tier": "gold", "ext": ".m", "sha1_git": r.sha,
            "filename": r.row.get("name", ""),
            "qualified_swhid": SE.qualified_swhid(r.sha, r.row.get("origin"), r.row.get("path")),
            "expected": exp, "expected_detail": h["language"], "accept": ";".join(ACCEPT.get(exp, [])),
            "reference": f"human:{'+'.join(r.human_reviewers())}; judges agree: "
                         f"{'yes' if fam(r.lang('judge')) == fam(r.lang('judge2')) == exp else 'no'}",
            "provenance": h.get("provenance_kind") or "",
            "frame": "+".join(f for f in ("U", "R") if r.in_frame(f, 1000)) or "audit",
            "stratum": d["stratum"], "weight": round(int(d["stratum_N"]) / n_h[d["stratum"]], 4),
            "tags": ";".join(tags(exp, raw)),
        })
        (FILES / r.sha).write_bytes(raw)
    with CASES.open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {VERSION} — {len(rows)} archived .m files with human-checked labels; "
                "generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    size = sum((FILES / r["sha1_git"]).stat().st_size for r in rows)
    print(f"{VERSION}: {len(rows)} cases → {CASES.name}, {FILES.name}/ ({size / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
