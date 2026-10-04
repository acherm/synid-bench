#!/usr/bin/env python3
"""Build bench-fsf from the `.fsf` extension study of PL-ultimate-llm
(docs/fsf_swh_study.md) → cases.csv, labels.csv, files/.

    python3 benchmarks/bench-fsf/build_cases.py

Needs a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM, by default a sibling of
synid-bench) holding commit PL_REV (tools/study_cases.py); the study's data is
read at that commit, except the origin table with paths (fsf_files+origin.csv,
not in that repository's git: read from the working tree when present, else
the qualified SWHIDs carry the origin only). The bytes come from the
checkout's cache, else from Software Heritage.

Cases: the files of the study's uniform by-file sample (1,000 of the 21,802
`.fsf` contents in Software Heritage) that the LLM judge labelled with a
language Linguist names, or as not code. FSL FEAT design files (four in five)
are many near-identical generated files: a seeded draw keeps FEAT_CAP of them;
every other file is kept. Left out: non-text files, verdicts of low confidence,
and notations with no name in Linguist (a fractal L-system DSL, IDE settings,
FDT scripts, …). Weights re-weight each label's cases to its share of the
uniform sample.

Labels: the judge's (Claude Sonnet 4.6, schema fsf-judge/1, shown the file,
its name and the mechanical indicators) — silver. A FEAT design is a list of
Tcl `set fmri(…) …` commands that FSL loads with Tcl's `source`: its expected
language is Tcl (the judge: "expressed in Tcl set-variable syntax"), not Text.
git-annex pointers (a path, archived where the design was annexed) and
documentation are Text. The rules' answer to "is it a FEAT design?" (the
`set fmri(` marker) is recorded beside the judge's (judge-rules-agree /
judge-rules-disagree).
"""

from __future__ import annotations

import json
import random
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import study_cases as S  # noqa: E402

VERSION = "bench-fsf/1"
STUDY = "data/derived/fsf_study"
POPULATION = 21802  # unique `.fsf` contents in the study's population table (study §2.1)
N_SAMPLE = 1000     # the uniform by-file sample (frame E1)
FEAT_CAP = 300      # FEAT designs kept (seeded draw)
SEED = 2026
JUDGE = "claude-sonnet-4.6 (fsf-judge/1)"
FEAT = {"fsl-feat-design": "feat-design", "fsl-melodic-config": "melodic"}
LABELS = [("fsl-feat", "Tcl", "manual"), ("not-code:git-annex-pointer", "Text", "manual"),
          ("not-code:docs", "Text", "manual"), ("XML", "XML", "exact"), ("JSON", "JSON", "exact"),
          ("GLSL", "GLSL", "exact"), ("C++", "C++", "exact")]


def label(v: dict) -> tuple[str | None, str]:
    """(expected, the study's label) from the judge's verdict; None = left out (with why)."""
    ex, fmt = v.get("expressed_in") or "", v.get("format") or ""
    if v.get("confidence") == "low":
        return None, "low confidence"
    if "git-annex" in f"{ex} {fmt}".lower():  # the pointer, not the design it points to
        return "Text", "not-code:git-annex-pointer"
    if v.get("content_type") == "binary":
        return None, "binary"
    if v.get("artifact_kind") in FEAT or ex.startswith("Tcl"):
        return "Tcl", "fsl-feat"
    if v.get("content_type") == "docs" or v.get("artifact_kind") == "docs":
        return "Text", "not-code:docs"
    if ex in ("XML", "JSON"):
        return ex, ex
    if ex.startswith("GLSL"):
        return "GLSL", "GLSL"
    if ex.startswith("C++"):
        return "C++", "C++"
    return None, "a notation Linguist does not name"


def main() -> int:
    S.check_checkout()
    work = HERE / ".work"
    worklist = {w["sha1_git"]: w for w in S.pinned_csv(f"{STUDY}/worklist_all.csv")}
    reports = {Path(p).stem: json.loads(b) for p, b in S.pinned_dir(f"{STUDY}/reports").items()}
    uniform = sorted(s for s, w in worklist.items() if w["in_uniform"] == "1")
    table = S.local("fsf_files+origin.csv")
    origins = S.origin_index(table.decode("utf-8"), set(uniform)) if table else {}
    ling = S.Linguist()

    sample, labelled, left_out = Counter(), {}, Counter()
    for sha in uniform:
        r = reports.get(sha)
        v = (r.get("judge") or {}).get("verdict") if r else None
        exp, lab = label(v) if v else (None, "not fetched" if r is None else "not judged (not text)")
        sample[exp or f"left out: {lab}"] += 1
        if exp is None:
            left_out[lab] += 1
        else:
            labelled[sha] = (exp, lab, v)
    feat = sorted(s for s, (e, _, _) in labelled.items() if e == "Tcl")
    keep = set(random.Random(SEED).sample(feat, min(FEAT_CAP, len(feat)))) | {
        s for s, (e, _, _) in labelled.items() if e != "Tcl"}

    rows, blobs = [], {}
    for sha in sorted(keep):
        exp, lab, v = labelled[sha]
        r = reports[sha]
        raw = S.content(sha, work)
        if raw is None:
            raise SystemExit(f"{sha}: bytes unavailable")
        name = r["name"].lstrip("/")
        origin, path, swhid = S.locate(sha, name, origins.get(sha, []), r["origin"])
        accept = ling.accept(exp, "FSL FEAT design" if exp == "Tcl" else "")
        filename = S.neutral_name(name, ".fsf", accept.split(";"))
        rules_feat = r["reclass"]["label"] == "fsl-feat"
        agree = rules_feat == (exp == "Tcl")
        tags = [FEAT[v["artifact_kind"]]] if exp == "Tcl" and v.get("artifact_kind") in FEAT else []
        if exp == "Tcl" and any(w in (v.get("expressed_in") or "").lower() for w in ("templat", "placeholder")):
            tags.append("template")
        if lab == "not-code:git-annex-pointer":
            tags.append("git-annex-pointer")
        tags += ["judge-rules-agree" if agree else "judge-rules-disagree", *S.text_tags(raw)]
        if filename != name:
            tags.append("renamed")
        rows.append({
            "case_id": f"fsf:{sha[:12]}", "tier": "silver", "ext": ".fsf", "sha1_git": sha,
            "filename": filename, "qualified_swhid": swhid, "expected": exp,
            "expected_detail": f"{v.get('format', '')} ({v.get('expressed_in', '')})",
            "accept": accept,
            "reference": f"judge: {JUDGE}; rules: {r['reclass']['label']} ({'agree' if agree else 'disagree'})",
            "provenance": f"PL-ultimate-llm@{S.PL_REV[:9]} .fsf study", "frame": "U", "stratum": exp,
            "weight": "", "tags": ";".join(tags), "path": path or (name if filename != name else ""),
        })
        blobs[sha] = raw
    S.post_stratify(rows, sample, N_SAMPLE, POPULATION)
    S.write_cases(HERE, f"{VERSION} — {len(rows)} archived .fsf files (FSL FEAT designs and what else squats "
                        f"on .fsf), labelled by an LLM judge (silver), weighted to the population", rows)
    S.write_labels(HERE, LABELS)
    mb = S.write_files(HERE, blobs)
    print(f"{VERSION}: {len(rows)} cases ({dict(Counter(r['expected'] for r in rows))}), files/ {mb:.1f} MB; "
          f"FEAT designs {len(feat)} → {FEAT_CAP}; left out of the uniform sample: {dict(left_out)}; "
          f"judge/rules disagree on {sum('judge-rules-disagree' in r['tags'] for r in rows)}; "
          f"paths from {'fsf_files+origin.csv' if table else 'nowhere (table absent)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
