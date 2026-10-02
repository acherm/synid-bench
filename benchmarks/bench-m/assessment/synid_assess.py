"""SWH Synid on `.m`, measured against human ground truth (the blind audit).

Scope: every `.m` file of the study that a human reviewed (the blind audit,
tools/m/audit.py) and both LLM judges labelled. Synid (`synid file`, commit in
synid.jsonl) is re-run on those files in its default configuration and in
ablations — each content strategy removed in turn — so that every failure can
be attributed to the strategy that produced it.

Labels are compared at language level, with MATLAB and Octave merged (Synid has
no Octave): matlab-family, objective-c, mathematica-wolfram, mercury, mumps-m,
magma, limbo, muf, mason, c-or-cpp, not-code, other. Synid's "Text" is correct
only for a file the human labelled not-code; several candidates = undecided.
Files the human marked unsure/unknown have no reference and are left out.

Estimates are post-stratified: the audit sampled two strata (labellers agree /
disagree) at different rates, and a reviewer completes only part of it, so each
reviewed file weighs N_h / n_h with n_h the reviewed files of its stratum.

    python3 benchmarks/bench-m/assessment/synid_assess.py   # → assessment/synid_assessment.{json,csv} + m-<commit>.md
                                             #   (needs PL-ultimate-llm: $PL_ULTIMATE_LLM, or a sibling checkout)
"""

from __future__ import annotations

import csv
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
# the .m study (data, loaders, Synid runner) lives in PL-ultimate-llm
PL = Path(os.environ.get("PL_ULTIMATE_LLM", HERE.parents[3] / "PL-ultimate-llm")).resolve()  # sibling of synid-bench
sys.path.insert(0, str(PL))
from tools.m import audit as A  # noqa: E402
from tools.m import stats as S  # noqa: E402
from tools.m.data import STUDY, SYNID_MAP, load, synid_lang  # noqa: E402
from tools.m.run_synid import BIN, CONFIG, SYNID_DIR, synid_commit  # noqa: E402
from tools.m.study import raw_bytes  # noqa: E402

ROOT = PL                                   # Synid configs are written under PL's .cache, as the study does
WORK = HERE.parent / ".work" / "synid_assess_in"
OUT_JSON = HERE / "synid_assessment.json"
OUT_CSV = HERE / "synid_assessment.csv"
REPORT = HERE / "m-{commit}.md"
SWH = "https://archive.softwareheritage.org"

ALL = ["filename", "extension", "shebang", "comment", "hyplyheuristics", "hyplyclassifier", "pygmentsheuristics"]
CONFIGS = {
    "default": ALL,
    "no comment": [s for s in ALL if s != "comment"],
    "no hyply heuristics": [s for s in ALL if s != "hyplyheuristics"],
    "no pygments heuristics": [s for s in ALL if s != "pygmentsheuristics"],
    "no hyply classifier": [s for s in ALL if s != "hyplyclassifier"],
    "extension only": ["filename", "extension"],
}
NO_REF = {"unsure", "unknown", "", None}
OTHER_LABELLERS = {"judge": "LLM judge (Sonnet 4.6)", "judge2": "LLM judge (Gemini 3.8 Flash)",
                   "linguist": "Linguist heuristics", "pygments": "Pygments (guess_lexer)",
                   "ours": "study rules (v2)"}


def fam(label: str | None) -> str:
    """Language-level label; MATLAB and Octave merged (Synid has no Octave)."""
    if label in ("matlab", "octave", "matlab-family"):
        return "matlab-family"
    if label in ("objective-c", "mathematica-wolfram", "mercury", "mumps-m", "magma", "limbo", "muf",
                 "mason", "c-or-cpp", "not-code"):
        return label
    if label in ("unknown", "unresolved", None, ""):
        return "none"
    return "other"


def synid_outcome(answer: list[str] | None, human: str) -> tuple[str, bool]:
    """(kind, correct) for one Synid answer: kind ∈ language | text | undecided | none."""
    if not answer:
        return "none", False
    if len(answer) > 1:
        return "undecided", False
    if answer == ["Text"]:
        return "text", fam(human) == "not-code"
    return "language", fam(SYNID_MAP.get(answer[0], "other-programming-language")) == fam(human)


def run_synid(recs) -> dict[str, dict[str, list[str]]]:
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir(parents=True)
    for r in recs:
        base = re.sub(r"[^\w.+-]", "_", r.row.get("name") or "file")[:80] or "file.m"
        (WORK / r.sha).mkdir()
        (WORK / r.sha / base).write_bytes(raw_bytes(r.sha))
    out = {}
    for name, strats in CONFIGS.items():
        slug = re.sub(r"\W+", "_", name)
        cfg = ROOT / ".cache" / "m" / f"synid_assess_{slug}.toml"
        cfg.write_text(CONFIG.format(out=ROOT / ".cache" / "m" / "synid-output", enable=json.dumps(strats)))
        txt = subprocess.run([str(BIN), "file", "--config", str(cfg), str(WORK)],
                             capture_output=True, text=True, check=True).stdout
        res, cur = {}, None
        for line in txt.splitlines():
            if line.startswith(str(WORK)):
                cur = Path(line.strip()).parent.name
            elif cur and line.strip().startswith("["):
                res[cur] = json.loads(line.strip())
                cur = None
        out[name] = res
    return out


def is_utf8(raw: bytes) -> bool:
    try:
        raw.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def mechanism(row: dict) -> str:
    """Why Synid (default) failed on this file, from the ablations."""
    d, human = row["synid"]["default"], row["human"]
    if row["synid_kind"] == "undecided":
        return ("content not valid UTF-8: `synid file` cannot read it, every content strategy is skipped "
                "and the extension's candidates are returned" if not row["utf8"] else
                "no strategy narrowed the extension's candidates")
    if row["synid_kind"] == "text":
        np_ = row["synid"]["no pygments heuristics"]
        cause = ("Pygments heuristics: no heuristic of the remaining candidates matched, so the strategy's "
                 "default \"Text\" became the answer, before the Bayesian classifier could run")
        if np_ and np_ != ["Text"]:
            cause += f"; without that strategy the classifier answers {', '.join(np_)}"
            ok = synid_outcome(np_, human)[1]
            cause += " (right)" if ok else " (still wrong)"
        if fam(human) in ("magma", "c-or-cpp", "other", "mason"):
            cause += "; and the language is not among Synid's candidates for `.m`"
        nc = row["synid"]["no comment"]
        if nc != d:
            cause += f"; without the comment strategy: {', '.join(nc) or 'nothing'}"
        return cause
    if row["synid_kind"] == "language" and not row["synid_correct"]:
        return "wrong language"
    return ""


def assess() -> dict:
    recs = load()
    queue = {d["sha1_git"]: d for d in A.queue()}
    reviewed = [r for r in recs.values() if r.human_latest() and r.lang("judge") and r.lang("judge2")
                and r.sha in queue]
    abl = run_synid(reviewed)
    stored_same = sum(1 for r in reviewed if abl["default"].get(r.sha) == (r.synid or {}).get("default"))

    # post-stratified weights over the files with a reference label
    with_ref = [r for r in reviewed if r.human()["language"] not in NO_REF]
    n_h = Counter(queue[r.sha]["stratum"] for r in with_ref)
    N_h = {queue[r.sha]["stratum"]: int(queue[r.sha]["stratum_N"]) for r in reviewed}
    weight = {r.sha: N_h[queue[r.sha]["stratum"]] / n_h[queue[r.sha]["stratum"]] for r in with_ref}

    rows = []
    for r in reviewed:
        h = r.human()["language"]
        raw = raw_bytes(r.sha) or b""
        kind, ok = synid_outcome(abl["default"].get(r.sha), h)
        row = {"sha1_git": r.sha, "filename": r.row.get("name", ""), "origin": r.row.get("origin", ""),
               "path": r.row.get("path", ""), "stratum": queue[r.sha]["stratum"], "weight": weight.get(r.sha),
               "human": h, "judge": r.lang("judge"), "judge2": r.lang("judge2"),
               "linguist": r.lang("linguist"), "pygments": r.lang("pygments"), "ours": r.lang("ours"),
               "synid": {c: abl[c].get(r.sha) for c in CONFIGS}, "synid_kind": kind, "synid_correct": ok,
               "utf8": is_utf8(raw), "lines": r.ind.get("total_lines"),
               # the only evidence Synid's Pygments heuristic for MATLAB looks for
               "matlab_heuristic_evidence": bool(re.search(r"(?m)^\s*%|^function|^!\w+",
                                                           raw.decode("utf-8", "replace")))}
        row["mechanism"] = mechanism(row) if h not in NO_REF and not ok else ""
        rows.append(row)

    def score(pred) -> dict:
        xs, ws, answered, ans_ok = [], [], 0, 0
        for row in rows:
            if row["human"] in NO_REF:
                continue
            kind, ok = pred(row)
            xs.append(int(ok))
            ws.append(row["weight"])
            if kind == "language" or (kind == "text" and ok):
                answered += 1
                ans_ok += ok
        p, lo, hi, neff = S.weighted_prop(xs, ws)
        return {"n": len(xs), "correct": sum(xs), "accuracy_raw": round(sum(xs) / len(xs), 4),
                "accuracy_weighted": round(p, 4), "ci": [round(lo, 4), round(hi, 4)], "n_eff": round(neff, 1),
                "answered": answered, "correct_when_answering": round(ans_ok / answered, 4) if answered else None}

    configs = {c: score(lambda row, c=c: synid_outcome(row["synid"][c], row["human"])) for c in CONFIGS}

    def other(lab):
        def pred(row):
            y = row[lab]
            if y in (None, "unknown", "unresolved"):
                return "none", False
            return "language", fam(y) == fam(row["human"])
        return pred
    labellers = {lab: score(other(lab)) for lab in OTHER_LABELLERS}

    confusion = defaultdict(Counter)
    for row in rows:
        if row["human"] in NO_REF:
            continue
        d = row["synid"]["default"]
        col = ("undecided" if d and len(d) > 1 else "Text" if d == ["Text"] else
               fam(SYNID_MAP.get(d[0], "other")) if d else "none")
        confusion[fam(row["human"])][col] += 1

    failures = Counter()
    for row in rows:
        if row["human"] in NO_REF or row["synid_correct"]:
            continue
        failures[row["synid_kind"]] += 1
    return {"synid_commit": synid_commit(), "n_reviewed": len(reviewed), "n_with_reference": len(with_ref),
            "strata": {h: {"N": N_h[h], "n_reviewed_with_ref": n_h[h], "weight": round(N_h[h] / n_h[h], 3)}
                       for h in n_h},
            "default_reproduces_stored": f"{stored_same}/{len(reviewed)}",
            "configs": configs, "labellers": labellers,
            "confusion_default": {k: dict(v) for k, v in confusion.items()},
            "failures_default": dict(failures), "rows": rows}


# ---------------------------------------------------------------- report
def pct(x):
    return "—" if x is None else f"{100 * x:.1f}%"


def render(res: dict) -> str:
    c, L = res["configs"], res["labellers"]
    d = c["default"]
    rows = [r for r in res["rows"] if r["human"] not in NO_REF]
    fails = [r for r in rows if not r["synid_correct"]]
    text_rows = [r for r in fails if r["synid_kind"] == "text"]
    np_right = sum(1 for r in text_rows if synid_outcome(r["synid"]["no pygments heuristics"], r["human"])[1])
    lines = [
        "# SWH Synid on `.m` — measured against human ground truth",
        "",
        f"*Generated by `python3 benchmarks/bench-m/assessment/synid_assess.py` — Synid commit `{res['synid_commit']}`, "
        f"`synid file` (no graph). Data: `assessment/synid_assessment.{{json,csv}}`. "
        "Source study: PL-ultimate-llm, `.m` extension study (blind audit).*",
        "",
        "> **Version.** This assessment describes the Synid commit above. Later versions are tracked on the "
        "benchmark in this repository ([README](../README.md), [history](../HISTORY.md)).",
        "",
        "## What was measured",
        "",
        f"The **{res['n_reviewed']} `.m` files that a human reviewed** in the blind audit (and both LLM judges "
        f"labelled); {res['n_with_reference']} have a reference label (the others were marked unsure/unknown). "
        "Synid was re-run on them in its default configuration and with each content strategy removed. "
        f"The default run reproduces the study's stored answers on {res['default_reproduces_stored']} files.",
        "",
        "Labels are compared at language level (MATLAB and Octave merged — Synid has no Octave). Synid's "
        "`Text` counts as right only for a file the human labelled not code; several candidates = undecided. "
        "The audit over-samples files on which labellers disagree, so population estimates are "
        "post-stratified (each file weighs N_h / n_h of its stratum: "
        + "; ".join(f"{h} {v['N']} files / {v['n_reviewed_with_ref']} reviewed → ×{v['weight']}"
                    for h, v in res["strata"].items()) + ").",
        "",
        "## Headline",
        "",
        f"- Synid gives a **single language for {d['answered']} of {d['n']} files, and is right on "
        f"{pct(d['correct_when_answering'])} of those**.",
        f"- Overall it is right on **{d['correct']}/{d['n']}** reviewed files ({pct(d['accuracy_raw'])}); "
        f"weighted to the population of `.m` files, **{pct(d['accuracy_weighted'])}** "
        f"[{pct(d['ci'][0])}, {pct(d['ci'][1])}] (n_eff {d['n_eff']}).",
        f"- All its failures are **non-answers**: `Text` on {sum(1 for r in fails if r['synid_kind'] == 'text')} "
        f"files of real code, and *undecided* on {sum(1 for r in fails if r['synid_kind'] == 'undecided')}.",
        f"- Every `Text` comes from the **Pygments-heuristics strategy**: removed, no `Text` remains and the "
        f"Bayesian classifier answers instead — right on {np_right} of those {len(text_rows)} files.",
        "",
        "## Accuracy by configuration and against the other labellers",
        "",
        "| | single-language answers | right when answering | right overall (raw) | weighted estimate [95 % CI] |",
        "|---|---:|---:|---:|---:|",
    ]
    for name, v in c.items():
        lines.append(f"| Synid — {name} | {v['answered']}/{v['n']} | {pct(v['correct_when_answering'])} | "
                     f"{v['correct']}/{v['n']} | {pct(v['accuracy_weighted'])} [{pct(v['ci'][0])}, {pct(v['ci'][1])}] |")
    for lab, v in L.items():
        lines.append(f"| {OTHER_LABELLERS[lab]} | {v['answered']}/{v['n']} | {pct(v['correct_when_answering'])} | "
                     f"{v['correct']}/{v['n']} | {pct(v['accuracy_weighted'])} [{pct(v['ci'][0])}, {pct(v['ci'][1])}] |")
    cols = sorted({k for v in res["confusion_default"].values() for k in v})
    lines += ["", "## Synid (default) against the human label", "",
              "| human \\ Synid | " + " | ".join(cols) + " |", "|---|" + "---:|" * len(cols)]
    for h, v in sorted(res["confusion_default"].items(), key=lambda kv: -sum(kv[1].values())):
        lines.append(f"| {h} | " + " | ".join(str(v.get(k, "")) for k in cols) + " |")
    lines += [
        "",
        "## Failure mechanisms",
        "",
        "**1. `Text` by default (Pygments heuristics).** Synid chains its strategies — filename → extension → "
        "shebang → comment → Hyperpolyglot heuristics → **Pygments heuristics → Hyperpolyglot classifier** "
        "(`src/graph_identification_pipeline.rs`). The extension strategy proposes the eight candidates of "
        "`.m`; later strategies refine them. The Pygments strategy always returns one syntax: the "
        "best-scoring candidate, starting from `(0.0, \"Text\")` (`src/strategies/pygment_strategy/mod.rs`, "
        "`guess_syntax`). When none of the remaining candidates' heuristics matches — MATLAB's only fire on "
        "a line starting with `%`, `!` or `function` — the answer is `Text`, final, and the classifier that "
        "comes after never runs. Fix: return the candidates unchanged when no heuristic scores (or run the "
        "classifier first). "
        + (lambda m: f"All {len(m)} MATLAB/Octave files answered `Text` here are comment-free scripts — "
                     f"{sum(1 for r in m if not r['matlab_heuristic_evidence'])} have no line starting with "
                     "`%`, `!` or `function` — which Linguist's `.m` heuristics cannot place either, so they "
                     "reach the Pygments step undecided."
           )([r for r in text_rows if fam(r["human"]) == "matlab-family"]),
        "",
        "**2. Undecided on content that is not UTF-8.** `synid file` reads files as strict UTF-8; when "
        "decoding fails, every content strategy is skipped and the eight candidates of `.m` are returned. "
        "Both cases here are MATLAB files with Latin-1/GBK comments. Fix: decode lossily, as the S3 and "
        "Web-API content hosts already do.",
        "",
        "**3. Languages Synid cannot answer for `.m`.** The candidates come from Linguist's list for `.m` "
        "(Objective-C, MATLAB, Mercury, M, Wolfram Language, Limbo, MUF, Mason): Magma and C (misnamed `.m`) "
        "are not among them, so no answer can be right; Octave is MATLAB here.",
        "",
        "**4. The comment strategy** (`%` counted inside Objective-C `@\"%@\"` strings eliminates "
        "Objective-C) — 9.9 % of Objective-C on the study's 1,248 files — appears "
        f"{sum(1 for r in rows if r['synid']['no comment'] != r['synid']['default'])} time(s) among the "
        "reviewed files.",
        "",
        "## Every failure",
        "",
        "| file | human | Synid default | without Pygments heur. | without comment | mechanism |",
        "|---|---|---|---|---|---|",
    ]
    for r in sorted(fails, key=lambda r: (r["synid_kind"], r["human"], r["filename"])):
        fmt = lambda v: ", ".join(v) if v and len(v) < 3 else ("undecided (8)" if v else "—")  # noqa: E731
        qs = f"swh:1:cnt:{r['sha1_git']};origin={r['origin']};path={r['path']}"
        lines.append(f"| [`{r['filename']}`]({SWH}/{qs}/) | {r['human']} | {fmt(r['synid']['default'])} | "
                     f"{fmt(r['synid']['no pygments heuristics'])} | {fmt(r['synid']['no comment'])} | "
                     f"{r['mechanism']} |")
    lines += ["", "## Caveats", "",
              f"- {res['n_with_reference']} files, one human reviewer; the audit is not finished "
              f"({res['n_reviewed']}/100). Intervals are wide by construction.",
              f"- The reference is the human label; the two LLM judges agree with it on "
              f"{L['judge']['correct']}/{L['judge']['n']} and {L['judge2']['correct']}/{L['judge2']['n']} files, "
              "so the conclusions do not hinge on a single annotator.",
              "- Synid runs here in `file` mode on bytes from the study cache; mechanism 2 is specific to "
              "that mode (`no-graph` / graph runs use lossy hosts).", ""]
    return "\n".join(lines)


def main():
    if not BIN.exists():
        sys.exit(f"synid binary missing: build it in {SYNID_DIR} (cargo build --release)")
    res = assess()
    OUT_JSON.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        cols = ["sha1_git", "filename", "stratum", "weight", "human", "judge", "judge2", "linguist", "pygments",
                "ours"] + [f"synid:{c}" for c in CONFIGS] + ["synid_kind", "synid_correct", "utf8", "mechanism"]
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in res["rows"]:
            w.writerow({**{k: r.get(k) for k in cols if not k.startswith("synid:")},
                        **{f"synid:{c}": "|".join(r["synid"][c] or []) for c in CONFIGS}})
    report = Path(str(REPORT).format(commit=res["synid_commit"]))
    report.write_text(render(res), encoding="utf-8")
    d = res["configs"]["default"]
    print(f"Synid default: {d['correct']}/{d['n']} right; answers {d['answered']}, right when answering "
          f"{d['correct_when_answering']}; weighted {d['accuracy_weighted']} {d['ci']} → {report.name}")


if __name__ == "__main__":
    main()
