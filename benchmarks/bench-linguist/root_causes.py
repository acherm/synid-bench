"""Root causes of failures on bench-linguist (used by tools/failures.py).

Two families: Synid's failures (any Synid run), and the failures of the two-stage
identifier (`jev-cascade*`: PL-ultimate-llm's candidates for the extension, then Jev),
whose causes point at the encyclopedia's mapping as much as at the model.

`diagnose(case, text, answers, run, ctx)` assigns one cause; `ctx` carries Linguist's
languages.yml (from build_cases.py's checkout), the names the Synid binary can output
(tools/failures.py --synid), the candidate mapping (tools/data/pl_candidates.json) and
the cascade's raw answers. Established on Synid 48c3c45 (2026-10-03).
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def key(n: str) -> str:
    return re.sub(r"[^a-z0-9+#*]", "", n.lower())


# Synid heuristic rules named by a Linguist name that is not the candidate's canonical name: the rule
# is filtered out by a string comparison (hyply_heuristics_strategy) — see bench-m's FAILURES.md.
RULE_NAME_MISMATCH = {"PLpgSQL": ".sql", "Wolfram Language": ".m", "Rocq Prover": ".v", "xBase": ".ch", "q": ".q"}

CAUSES = {
    "synid-unknown-language": {
        "title": "Synid has no syntax for the language",
        "mechanism": "No syntax of Synid carries the expected language's name or one of its Linguist aliases: no "
                     "strategy can name it. Mostly languages added to Linguist after Synid imported Hyperpolyglot's "
                     "2023 data.",
        "fix": "import the languages Linguist added since (names, extensions, file names, heuristics)",
        "verified": "the language is absent from `synid info syntaxes`",
    },
    "synid-text-default": {
        "title": "`Text` by default from the Pygments step (the classifier would be right)",
        "mechanism": "No heuristic decides between the extension's candidates; the Pygments-heuristics strategy "
                     "then returns its starting value `Text`, which is final — the Bayesian classifier, which comes "
                     "after it, never runs. The mechanism of bench-m's 10 MATLAB failures, here across hundreds of "
                     "files and languages.",
        "fix": "when no candidate's heuristic scores, return the candidates unchanged instead of `Text` (or run the "
               "classifier first) — but see the precision trade-off in the README",
        "verified": "Synid with `pygmentsheuristics` disabled answers the expected language on these files",
    },
    "synid-text-other": {
        "title": "`Text`, and the classifier would not be right either",
        "mechanism": "As above, `Text` ends the chain; with the Pygments step off, the classifier names another "
                     "language (or none): neither heuristics nor classifier hold the evidence.",
        "fix": "heuristics for these extensions; a classifier trained on more (and newer) samples",
        "verified": "Synid with `pygmentsheuristics` disabled is still not right on these files",
    },
    "synid-rule-name": {
        "title": "A heuristic rule never fires (its name is not the candidate's name)",
        "mechanism": "The rule for the expected language is named by a Linguist name (e.g. `PLpgSQL`, `Mathematica`) "
                     "while the candidate carries Synid's canonical name (`PL/pgSQL`, `Wolfram Language`); rules are "
                     "kept by comparing names as strings, so this one is dropped.",
        "fix": "compare syntax ids rather than names when filtering rules",
        "verified": "bench-m: renaming the Wolfram rule makes its 4 files right; 9bc1c32 → 48c3c45 regressed the "
                    "PL/pgSQL files once the heuristics ran first",
    },
    "synid-taxonomy": {
        "title": "Synid names a syntax Linguist files under another language",
        "mechanism": "The answer is not a Linguist language: a more specific or neighbouring syntax from Synid's "
                     "other sources (Pygments) — `Systemd` for an INI unit file, `MSBuild` for XML, `ASP` for "
                     "ASP.NET. A disagreement of granularity as much as an error.",
        "fix": "a taxonomy link (Synid syntax → Linguist language) so that answers can be compared, or report both",
        "verified": "the answer is neither a Linguist name nor an alias",
    },
    "synid-same-extension": {
        "title": "Another language claiming the same extension",
        "mechanism": "Synid picks the wrong one among the languages that claim the file's extension: its heuristics "
                     "do not separate them (or pick wrongly) and the classifier decides wrongly.",
        "fix": "heuristics for these extension pairs (e.g. `.bf` Befunge vs Brainfuck)",
        "verified": "the answer is a Linguist language listing the file's extension",
    },
    "synid-filename": {
        "title": "A file known by its whole name",
        "mechanism": "The sample is identified by its file name (Dockerfile, .babelrc, …); Synid's file-name table "
                     "does not know it, or maps it elsewhere.",
        "fix": "import Linguist's file names",
        "verified": "the case is tagged `by-filename`",
    },
    "synid-other": {
        "title": "Another wrong language",
        "mechanism": "The answer is a Linguist language that does not claim the extension: a shebang, a modeline or "
                     "a file name led elsewhere.",
        "fix": "case by case",
        "verified": "none of the above",
    },
    "cascade-no-candidate": {
        "title": "No candidate: the encyclopedia does not know the extension",
        "mechanism": "PL-ultimate-llm associates no language with the file's extension or name, and the fallback "
                     "(1,207 languages with a known extension) does not name it either. Mostly languages added to "
                     "Linguist after the encyclopedia's May 2026 import.",
        "fix": "refresh PL-ultimate-llm's Linguist import (and its other sources)",
        "verified": "no candidate for the case",
    },
    "cascade-not-among": {
        "title": "Candidates, but not the right one",
        "mechanism": "The encyclopedia associates languages with the extension, but not the expected one; Jev "
                     "chooses among the wrong set.",
        "fix": "add the missing claim to the encyclopedia (often a compound extension or a newer Linguist claim)",
        "verified": "the expected language is not among the candidates",
    },
    "cascade-confused": {
        "title": "The right candidate was there, Jev chose another",
        "mechanism": "The expected language is among the candidates, and Jev picks another candidate (or `Text`).",
        "fix": "content rules (the encyclopedia's heuristics) before the model; better descriptions of the options",
        "verified": "the expected language is among the candidates; Jev decided at the candidate stage",
    },
    "cascade-fell-back": {
        "title": "The right candidate was there, Jev said none",
        "mechanism": "Jev answered \"none of these\" although the expected language was a candidate; the fallback "
                     "then chose wrongly.",
        "fix": "keep the candidates in the fallback's final",
        "verified": "the expected language is among the candidates; the case went to the fallback",
    },
}


def load_ctx(bench: Path, synid_names: set[str] | None) -> dict:
    ling_p = bench / ".work" / "linguist" / "lib" / "linguist" / "languages.yml"
    ling = yaml.safe_load(ling_p.read_text(encoding="utf-8")) if ling_p.exists() else {}
    ext_l = defaultdict(set)
    for n, d in ling.items():
        for e in d.get("extensions") or []:
            ext_l[e.lower()].add(n)
    raw = {}
    for p in (bench / "entries" / "raw").glob("jev-cascade*.jsonl"):
        raw[p.stem] = {json.loads(line)["case_id"]: json.loads(line) for line in p.read_text(encoding="utf-8").splitlines()}
    return {"linguist_keys": {key(a) for n, d in ling.items() for a in [n, *(d.get("aliases") or [])]},
            "ext_langs": ext_l, "synid": synid_names,
            "pl": json.loads((ROOT / "tools" / "data" / "pl_candidates.json").read_text(encoding="utf-8")),
            "cascade_raw": raw}


def candidates(case: dict, pl: dict) -> list[str]:
    if case["filename"] in pl["by_filename"]:
        return pl["by_filename"][case["filename"]]
    parts = case["filename"].lower().split(".")[1:]
    out = []
    for i in range(len(parts)):
        out += [p for p in pl["by_ext"].get("." + ".".join(parts[i:]), []) if p not in out]
    return out


def diagnose(case: dict, text: str, answers: dict, run: str | None = None, ctx: dict | None = None) -> str | None:
    ctx = ctx or {}
    acc = {key(a) for a in case["accept"].split(";") if a}
    ans = answers.get(run) if run else None
    if run and run.startswith("jev-cascade"):
        cand = candidates(case, ctx["pl"])
        if not cand:
            return "cascade-no-candidate"
        if not any(key(ctx["pl"]["languages"][p]["name"]) in acc for p in cand):
            return "cascade-not-among"
        stage = ctx["cascade_raw"].get(run, {}).get(case["case_id"], {}).get("stage")
        return "cascade-fell-back" if stage == "fallback" else "cascade-confused"
    # Synid
    syn = ctx.get("synid")
    if syn is not None and not (acc & syn):
        return "synid-unknown-language"
    if case["expected"] in RULE_NAME_MISMATCH and case["ext"].lower() == RULE_NAME_MISMATCH[case["expected"]]:
        return "synid-rule-name"
    if ans == ["Text"]:
        nop = next((v for k, v in answers.items() if k.endswith("no-pygmentsheuristics")), None)
        return "synid-text-default" if nop and len(nop) == 1 and key(nop[0]) in acc else "synid-text-other"
    if "by-filename" in case["tags"]:
        return "synid-filename"
    if ans and len(ans) == 1:
        if key(ans[0]) not in ctx.get("linguist_keys", set()):
            return "synid-taxonomy"
        if ans[0] in ctx.get("ext_langs", {}).get(case["ext"].lower(), ()):
            return "synid-same-extension"
        return "synid-other"
    return None
