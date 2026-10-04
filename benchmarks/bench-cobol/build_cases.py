#!/usr/bin/env python3
"""Build bench-cobol from the COBOL extension study of PL-ultimate-llm
(docs/cobol_swh_study.md, `.cbl` and `.CBL`) → cases.csv, labels.csv, files/.

    python3 benchmarks/bench-cobol/build_cases.py

Needs a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM, by default a sibling of
synid-bench) holding commit PL_REV (tools/study_cases.py); the study's data is
read at that commit, except the re-judging of gate-skipped files
(data/derived/jev/cobol/gate_rescue.jsonl, not in that repository's git: read
from the working tree when present). The bytes (54 MB, not stored in this
repository) come from the checkout's cache, else from Software Heritage.

Cases: the study's uniform by-file sample (E3: 1,000 of the 276,831 `.cbl` /
`.CBL` contents in Software Heritage). The judge saw only the files with at
least two COBOL divisions (a cost gate); the others carry the label of the
study's content rules. Kept: every file the judge labelled; the gate-skipped
files the judge re-judged later; the files the rules label COBOL (copybooks,
programs, generated code) or ReadingList XML; and a seeded draw of SYNTH_CAP of
the 408 `WBC_*_FOO.CBL` stubs ("This is cobol file number N", one synthetic
repository, 41 % of the population), which the rules and a human assertion over
their repository label not code. Left out: binary files, files the rules call
`other` (no label: foreign code, metadata, …) and ambiguous verdicts. Weights
re-weight each stratum (label × who labelled it) to its share of the sample.

Labels: the judge's (Claude Sonnet 4.6, schema cobol-judge/2, shown the file,
its name and the mechanical indicators) where it judged — silver —, else the
rules' (tag rules-only); a file a human reviewed is gold. A copybook is COBOL
source text (Linguist files `.cpy` under COBOL): expected COBOL, tag copybook.
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

VERSION = "bench-cobol/1"
STUDY = "data/derived/cobol_study"
POPULATION = 276831  # unique `.cbl` / `.CBL` contents in the study's population tables (study §2.1)
N_SAMPLE = 1000      # the uniform by-file sample (E3, worklist_1k.csv)
SYNTH_CAP = 40       # synthetic WBC stubs kept (seeded draw)
SEED = 2026
JUDGE = "claude-sonnet-4.6 (cobol-judge/2)"
SYNTH_ORIGIN = "https://gitlab.com/fbetestpublic/repo-with-many-files-in-one-tree.git"
RULES = {"cobol": "COBOL", "cobol-generated": "COBOL", "cobol-copybook": "COBOL",
         "synthetic-placeholder": "Text", "comic-book-list": "XML"}  # comic lists: ReadingList XML only
LABELS = [("cobol", "COBOL", "exact"), ("copybook-only", "COBOL", "manual"), ("cobol-copybook", "COBOL", "manual"),
          ("cobol-generated", "COBOL", "manual"), ("synthetic-placeholder", "Text", "manual"),
          ("not-cobol:synthetic", "Text", "manual"), ("data", "Text", "manual"), ("docs", "Text", "manual"),
          ("jcl", "JCL", "exact"), ("comic-book-list (ReadingList XML)", "XML", "manual")]


def judge_label(v: dict) -> tuple[str | None, str]:
    """(expected, the study's label) from the judge's verdict; None = left out (with why)."""
    nl = v.get("not_cobol_label")
    if v.get("overall_confidence") == "low":
        return None, "low confidence"
    if v.get("cobol_confirmed") or nl == "copybook-only":
        return "COBOL", nl if nl == "copybook-only" else "cobol"
    if nl in ("data", "docs"):
        return "Text", nl
    if nl == "jcl":
        return "JCL", nl
    return None, nl or "unclear"


def main() -> int:
    S.check_checkout()
    work = HERE / ".work"
    worklist = S.pinned_csv(f"{STUDY}/worklist_1k.csv")
    reports = {}
    for b in S.pinned_dir(f"{STUDY}/reports").values():
        r = json.loads(b)
        reports[r["sample"]["sha1_git"]] = r
    rules = {d["sha1_git"]: d for d in S.pinned_jsonl(f"{STUDY}/corpus_estimate.jsonl")}
    rescue = {d["sha1_git"]: d for d in map(json.loads, (S.local("data/derived/jev/cobol/gate_rescue.jsonl")
                                                       or b"").decode("utf-8").splitlines())}
    human = {}
    for p, b in S.pinned_dir("reviews_cobol").items():
        if p.endswith(".json"):
            h = json.loads(b)
            human[h["subject"]["sha1_git"]] = h
    synth_rule = [d for d in S.pinned_jsonl("reviews_cobol/_rules.jsonl") if d["value"] == SYNTH_ORIGIN]
    shas = {w["sha1_git"] for w in worklist}
    origins = S.origin_index(S.pinned("cbl_file+origin.csv").decode("utf-8"), shas)
    for sha, rows in S.origin_index(S.pinned("CBL_files+origins.csv").decode("utf-8"), shas).items():
        origins.setdefault(sha, []).extend(rows)
    ling = S.Linguist()

    sample, picked, left_out = Counter(), {}, Counter()
    for w in sorted(worklist, key=lambda w: w["sha1_git"]):
        sha = w["sha1_git"]
        rep = reports.get(sha) or {}
        v = (rep.get("judge") or {}).get("verdict")
        rl = rules[sha]["label"]
        src = "judge"
        if not v and sha in rescue:
            v, src = rescue[sha]["judge"]["verdict"], "judge (re-judged)"
        if v:
            exp, lab = judge_label(v)
        else:
            exp, lab, src = RULES.get(rl), rl, "rules"
            if rl == "comic-book-list" and b"<ReadingList" not in (S.content(sha, work) or b""):
                exp = None  # the binary CCBridgeLibrary format, not the XML list
        if exp is None:
            left_out[f"{lab} ({src})"] += 1
            sample[f"left out: {lab}"] += 1
            continue
        stratum = f"{exp} ({'origin rule' if rl == 'synthetic-placeholder' and not v else src.split(' ')[0]})"
        sample[stratum] += 1
        picked[sha] = (exp, lab, src, v, w, stratum)
    synth = sorted(s for s, p in picked.items() if p[5] == "Text (origin rule)")
    drop = set(synth) - set(random.Random(SEED).sample(synth, min(SYNTH_CAP, len(synth))))

    rows, blobs = [], {}
    for sha in sorted(set(picked) - drop):
        exp, lab, src, v, w, stratum = picked[sha]
        raw = S.content(sha, work)
        if raw is None:
            raise SystemExit(f"{sha}: bytes unavailable")
        ext = ".CBL" if w["source_csv"] == "CBL_files.csv" else ".cbl"
        rows_o = origins.get(sha, [])
        name = w["name"].lstrip("/")
        if not name.endswith(ext):  # the sample's name is another name of the same content
            name = next((r["name"] for r in sorted(rows_o, key=lambda r: r["name"]) if r["name"].endswith(ext)),
                        name + ext)
        origin, path, swhid = S.locate(sha, name, rows_o)
        accept = ling.accept(exp)
        filename = S.neutral_name(name, ext, accept.split(";"))
        rl = rules[sha]["label"]
        rep = reports.get(sha) or {}
        ind = rep.get("indicators") or {}
        tags = []
        if exp == "COBOL":
            if lab == "copybook-only" or rl == "cobol-copybook" or (v or {}).get("purpose", {}).get(
                    "program_type") == "copybook":
                tags.append("copybook")
            if rl == "cobol-generated":
                tags.append("generated")
            if ind.get("source_format_guess") in ("fixed", "free"):
                tags.append(f"{ind['source_format_guess']}-format")
            tags += [t for t, k in (("exec-sql", "has_exec_sql"), ("exec-cics", "has_exec_cics")) if ind.get(k)]
        if rl == "synthetic-placeholder":
            tags.append("synthetic-stub")
        if src == "rules":
            tags.append("rules-only")
            reference = f"rules: {rl} (no judge: fewer than two COBOL divisions)"
            if rl == "synthetic-placeholder" and synth_rule and origin == SYNTH_ORIGIN:
                tags.append("human-origin-rule")
                reference += f"; human assertion over its repository ({synth_rule[0]['reviewer']['id']}, " \
                             f"reviews_cobol/_rules.jsonl)"
        else:
            agree = (rl in ("cobol", "cobol-generated", "cobol-copybook")) == (exp == "COBOL")
            tags.append("judge-rules-agree" if agree else "judge-rules-disagree")
            if src != "judge":
                tags.append("gate-rescued")
            reference = f"{src}: {JUDGE}; rules: {rl} ({'agree' if agree else 'disagree'})"
        tier = "silver"
        if sha in human:
            hv = human[sha]["human"].get("is_cobol")
            tier = "gold" if (hv == "yes") == (exp == "COBOL") else "silver"
            reference = f"human: {human[sha]['reviewer']['id']} (is COBOL: {hv}); " + reference
        if ext == ".CBL":
            tags.append("upper-case-ext")
        tags += S.text_tags(raw)
        if filename != name:
            tags.append("renamed")
        detail = (f"{v['dialect']['family']} · {v['purpose']['program_type']}" if v and exp == "COBOL"
                  else lab)
        rows.append({
            "case_id": f"cobol:{sha[:12]}", "tier": tier, "ext": ext, "sha1_git": sha, "filename": filename,
            "qualified_swhid": swhid, "expected": exp, "expected_detail": detail, "accept": accept,
            "reference": reference, "provenance": f"PL-ultimate-llm@{S.PL_REV[:9]} COBOL study (E3)",
            "frame": "U", "stratum": stratum, "weight": "", "tags": ";".join(tags),
            "path": path or (name if filename != name else ""),
        })
        blobs[sha] = raw
    S.post_stratify(rows, sample, N_SAMPLE, POPULATION)
    S.write_cases(HERE, f"{VERSION} — {len(rows)} archived .cbl/.CBL files, labelled by an LLM judge or the "
                        f"study's rules (silver), weighted to the population", rows)
    S.write_labels(HERE, LABELS)
    mb = S.write_files(HERE, blobs)
    print(f"{VERSION}: {len(rows)} cases ({dict(Counter(r['stratum'] for r in rows))}), files/ {mb:.1f} MB "
          f"(not in git); synthetic stubs {len(synth)} → {SYNTH_CAP}; left out of the sample: {dict(left_out)}; "
          f"judge/rules disagree on {sum('judge-rules-disagree' in r['tags'] for r in rows)}; "
          f"gold {sum(r['tier'] == 'gold' for r in rows)}; re-judging {'read' if rescue else 'absent'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
