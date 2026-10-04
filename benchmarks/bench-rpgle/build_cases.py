#!/usr/bin/env python3
"""Build bench-rpgle from the `.rpgle` extension study of PL-ultimate-llm
(docs/rpgle_swh_study.md) → cases.csv, labels.csv, files/.

    python3 benchmarks/bench-rpgle/build_cases.py

Needs a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM, by default a sibling of
synid-bench) holding commit PL_REV (tools/study_cases.py); the study's data is
read at that commit. The bytes come from the checkout's cache, else from
Software Heritage.

Cases: the files of the study's uniform by-file sample (1,000 of the 13,002
`.rpgle` contents in Software Heritage) that the LLM judge labelled *after* the
study's hand-written rules were frozen (the study's held-out split), with a
usable label. Left out: the 326 files of the tuning split (the rules were
revised on their errors), non-text files (never judged), and verdicts that are
`ambiguous` or of low confidence. Weights re-weight each label's cases to its
share of the uniform sample, so the weighted accuracy estimates the accuracy on
`.rpgle` contents in the archive.

Labels: the judge's (Claude Sonnet 4.6, schema rpgle-judge/1, shown the file,
its name and the mechanical indicators) — silver. The rules' answer to "is it
RPG?" is recorded beside it (tag judge-rules-agree / judge-rules-disagree).
RPG's three source formats (fully-free, hybrid-free, fixed-format) are one
language for Linguist (RPGLE): they are tags, all accepted as RPGLE.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import study_cases as S  # noqa: E402

VERSION = "bench-rpgle/1"
STUDY = "data/derived/rpgle_study"
POPULATION = 13002  # unique `.rpgle` contents in the study's population table (study §2.1)
N_SAMPLE = 1000     # the uniform by-file sample (frame E1)
JUDGE = "claude-sonnet-4.6 (rpgle-judge/1)"
TOOLING = {"https://github.com/smeup/jariko", "https://github.com/JCErasmus/antlr4-rpgle",
           "https://github.com/chrjorgensen/rpgleparser"}  # parsers / an interpreter of RPG: test fixtures
# the judge's `language` for files it calls another language → that language's name
OTHER = {"REXX": "REXX", "DDS": "DDS", "XSL": "XSLT"}
LABELS = [("rpgle", "RPGLE", "exact"), ("not-code:data", "Text", "manual"), ("not-code:docs", "Text", "manual"),
          ("not-code:generated", "Text", "manual"), ("other-language:REXX", "REXX", "exact"),
          ("other-language:XSLT", "XSLT", "exact"), ("other-language:DDS", "", "none")]


def label(v: dict) -> tuple[str | None, str]:
    """(expected, the study's label) from the judge's verdict; None = left out (with why)."""
    nl = v.get("not_rpgle_label")
    if v.get("confidence") == "low":
        return None, "low confidence"
    if nl == "ambiguous":
        return None, "ambiguous"
    if nl == "other-language":
        name = next((n for k, n in OTHER.items() if v.get("language", "").startswith(k)), None)
        return (name, f"other-language:{name}") if name else (None, "another language, unnamed")
    if nl in ("data", "docs", "generated"):
        return "Text", f"not-code:{nl}"
    if nl == "none" and v.get("is_programming_language") and v.get("content_type") in (
            "source-code", "copybook-or-header"):
        return "RPGLE", "rpgle"
    return None, f"not code: {nl}"


def main() -> int:
    S.check_checkout()
    work = HERE / ".work"
    worklist = {w["sha1_git"]: w for w in S.pinned_csv(f"{STUDY}/worklist_all.csv")}
    reports = {Path(p).stem: json.loads(b) for p, b in S.pinned_dir(f"{STUDY}/reports").items()}
    tuning = set(json.loads(S.pinned(f"{STUDY}/eval_tuning_set.json"))["shas"])
    uniform = sorted(s for s, w in worklist.items() if w["in_uniform"] == "1")
    origins = S.origin_index(S.pinned("rpgle_files+origins.csv").decode("utf-8"), set(uniform))
    ling = S.Linguist()

    sample, rows, blobs, left_out = Counter(), [], {}, Counter()
    for sha in uniform:
        r = reports[sha]
        v = (r.get("judge") or {}).get("verdict")
        exp, why = label(v) if v else (None, "not judged (not text)")
        if exp is None:
            left_out[why] += 1
            sample[f"left out: {why}"] += 1
            continue
        sample[exp] += 1
        if sha in tuning:
            left_out["tuning split"] += 1
            continue
        raw = S.content(sha, work)
        if raw is None:
            raise SystemExit(f"{sha}: bytes unavailable")
        name = r["name"].lstrip("/")
        origin, path, swhid = S.locate(sha, name, origins.get(sha, []), r["origin"])
        accept = ling.accept(exp, OTHER.get(exp, ""))
        filename = S.neutral_name(name, ".rpgle", accept.split(";"))
        ind = r["indicators"]
        rules_rpg = r["reclass"]["label"] in ("rpgle", "rpgle-copybook")
        agree = rules_rpg == (exp == "RPGLE")
        tags = [ind["source_format_guess"]] if exp == "RPGLE" and ind["source_format_guess"] != "unknown" else []
        if exp == "RPGLE" and (v.get("content_type") == "copybook-or-header"
                               or v.get("unit_kind") == "copybook-prototype-header"):
            tags.append("copy-member")
        if exp == "RPGLE" and ind.get("has_exec_sql"):
            tags.append("embedded-sql")
        if origin in TOOLING:
            tags.append("tooling-repo")
        tags += ["judge-rules-agree" if agree else "judge-rules-disagree", *S.text_tags(raw)]
        if filename != name:
            tags.append("renamed")
        rows.append({
            "case_id": f"rpgle:{sha[:12]}", "tier": "silver", "ext": ".rpgle", "sha1_git": sha,
            "filename": filename, "qualified_swhid": swhid, "expected": exp,
            "expected_detail": v.get("language", ""), "accept": accept,
            "reference": f"judge: {JUDGE}; rules: {r['reclass']['label']} ({'agree' if agree else 'disagree'})",
            "provenance": f"PL-ultimate-llm@{S.PL_REV[:9]} .rpgle study", "frame": "U", "stratum": exp,
            "weight": "", "tags": ";".join(tags), "path": path or (name if filename != name else ""),
        })
        blobs[sha] = raw
    S.post_stratify(rows, sample, N_SAMPLE, POPULATION)
    S.write_cases(HERE, f"{VERSION} — {len(rows)} archived .rpgle files, labelled by an LLM judge (silver), "
                        f"weighted to the population", rows)
    S.write_labels(HERE, LABELS)
    mb = S.write_files(HERE, blobs)
    print(f"{VERSION}: {len(rows)} cases ({dict(Counter(r['expected'] for r in rows))}), files/ {mb:.1f} MB; "
          f"left out of the uniform sample: {dict(left_out)}; "
          f"judge/rules disagree on {sum('judge-rules-disagree' in r['tags'] for r in rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
