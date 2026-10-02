#!/usr/bin/env python3
"""Score a Synid run against the benchmark, and compare it with a baseline.

    python3 tools/score.py benchmarks/bench-m/results/head.jsonl
    python3 tools/score.py benchmarks/bench-m/results/head.jsonl \
        --baseline benchmarks/bench-m/baselines/48c3c45-default.jsonl --report benchmarks/bench-m/results/head.md

A case is right when Synid gives exactly one syntax and it is in the case's
`accept` list. `Text` is right only where accepted (files that are not code);
several syntaxes = undecided; no answer = none.

Exit status: 1 when the run regresses on a case the baseline got right
(--fail-on gold: gold cases only; any: every case; none: never).
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

Z = 1.959963984540054


def read_cases(bench: Path) -> dict[str, dict]:
    with (bench / "cases.csv").open(encoding="utf-8") as f:
        return {c["case_id"]: c for c in csv.DictReader(line for line in f if not line.startswith("#"))}


def read_run(path: Path) -> tuple[dict, dict[str, list[str] | None]]:
    meta, ans = {}, {}
    for line in path.read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        if "meta" in d:
            meta = d["meta"]
        else:
            ans[d["case_id"]] = d["answer"]
    return meta, ans


def outcome(case: dict, answer: list[str] | None) -> str:
    """right | wrong | text | undecided | none"""
    if not answer:
        return "none"
    if len(answer) > 1:
        return "undecided"
    accept = {a for a in case["accept"].split(";") if a}
    if answer[0] in accept:
        return "right"
    return "text" if answer[0] == "Text" else "wrong"


def wilson(k: float, n: float) -> tuple[float, float]:
    if not n:
        return float("nan"), float("nan")
    p = k / n
    den = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / den
    h = Z * ((p * (1 - p) / n + Z * Z / (4 * n * n)) ** 0.5) / den
    return max(0.0, c - h), min(1.0, c + h)


def metrics(cases: dict, ans: dict, ids: list[str], weighted: bool = False) -> dict:
    oc = Counter(outcome(cases[i], ans.get(i)) for i in ids)
    n = len(ids)
    right = oc["right"]
    # a language answer: exactly one syntax, other than Text — its precision is what
    # a user of Synid relies on when it does name a language
    lang = [i for i in ids if ans.get(i) and len(ans[i]) == 1 and ans[i][0] != "Text"]
    lang_right = sum(1 for i in lang if outcome(cases[i], ans.get(i)) == "right")
    m = {"n": n, "right": right, "accuracy": right / n if n else None, "ci": wilson(right, n),
         "language_answers": len(lang), "precision": lang_right / len(lang) if lang else None,
         "outcomes": dict(oc)}
    if weighted:
        ws = [float(cases[i]["weight"] or 0) for i in ids]
        xs = [outcome(cases[i], ans.get(i)) == "right" for i in ids]
        sw = sum(ws)
        if sw:
            p = sum(w for w, x in zip(ws, xs) if x) / sw
            neff = sw * sw / sum(w * w for w in ws)
            m["weighted"] = {"accuracy": p, "ci": wilson(p * neff, neff), "n_eff": neff}
    return m


def pct(x):
    return "—" if x is None or x != x else f"{100 * x:.1f}%"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run", type=Path, help="a run: <benchmark>/results/<label>.jsonl or <benchmark>/baselines/…")
    ap.add_argument("--bench", type=Path, help="benchmark directory (default: the run's grandparent)")
    ap.add_argument("--baseline", type=Path)
    ap.add_argument("--report", type=Path, help="write a markdown report here")
    ap.add_argument("--fail-on", choices=["gold", "any", "none"], default="gold")
    a = ap.parse_args()
    cases = read_cases((a.bench or a.run.resolve().parents[1]).resolve())
    meta, ans = read_run(a.run)
    tiers = defaultdict(list)
    for cid, c in cases.items():
        tiers[c["tier"]].append(cid)

    out = [f"# Synid benchmark — `{meta.get('label')}`", "",
           f"Synid {meta.get('version', '?')} · commit `{meta.get('commit') or '?'}` · strategies "
           f"{', '.join(meta.get('strategies', []))} · benchmark {meta.get('benchmark', '?')} "
           f"({len(cases)} cases).", "",
           "| tier | cases | right | accuracy [95 % CI] | language answers | precision of language answers | "
           "`Text` on code | undecided | wrong language |",
           "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    summary = {}
    for tier in ("gold", "silver"):
        ids = tiers.get(tier, [])
        if not ids:
            continue
        m = metrics(cases, ans, ids, weighted=(tier == "gold"))
        summary[tier] = m
        o = m["outcomes"]
        out.append(f"| {tier} | {m['n']} | {m['right']} | {pct(m['accuracy'])} [{pct(m['ci'][0])}, {pct(m['ci'][1])}] | "
                   f"{m['language_answers']} | {pct(m['precision'])} | {o.get('text', 0)} | "
                   f"{o.get('undecided', 0)} | {o.get('wrong', 0)} |")
    if "weighted" in summary.get("gold", {}):
        w = summary["gold"]["weighted"]
        out += ["", f"Gold, weighted to the `.m` population (post-stratified audit weights): "
                    f"**{pct(w['accuracy'])}** [{pct(w['ci'][0])}, {pct(w['ci'][1])}], n_eff {w['n_eff']:.1f}."]

    # by expected language and by tag (all tiers)
    for title, key in (("By expected language", "expected"), ("By failure trigger (tag)", "tags")):
        groups = defaultdict(list)
        for cid, c in cases.items():
            for g in (c[key].split(";") if key == "tags" else [c[key]]):
                if g:
                    groups[g].append(cid)
        out += ["", f"## {title}", "", "| | cases | right | accuracy | `Text` | undecided | wrong |",
                "|---|---:|---:|---:|---:|---:|---:|"]
        for g, ids in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            m = metrics(cases, ans, ids)
            o = m["outcomes"]
            out.append(f"| {g} | {m['n']} | {m['right']} | {pct(m['accuracy'])} | {o.get('text', 0)} | "
                       f"{o.get('undecided', 0)} | {o.get('wrong', 0)} |")

    regressions = []
    if a.baseline:
        bmeta, bans = read_run(a.baseline)
        changes = defaultdict(list)
        for cid, c in cases.items():
            old, new = outcome(c, bans.get(cid)), outcome(c, ans.get(cid))
            if bans.get(cid) == ans.get(cid):
                continue
            kind = ("fixed" if new == "right" and old != "right" else
                    "regressed" if old == "right" and new != "right" else "changed")
            changes[kind].append((c, bans.get(cid), ans.get(cid)))
        regressions = [x for x in changes["regressed"] if a.fail_on == "any" or
                       (a.fail_on == "gold" and x[0]["tier"] == "gold")]
        out += ["", f"## Against the baseline `{bmeta.get('label')}` (commit `{bmeta.get('commit') or '?'}`)", "",
                "| tier | fixed | regressed | changed, still not right |", "|---|---:|---:|---:|"]
        for tier in ("gold", "silver"):
            out.append(f"| {tier} | {sum(1 for x in changes['fixed'] if x[0]['tier'] == tier)} | "
                       f"{sum(1 for x in changes['regressed'] if x[0]['tier'] == tier)} | "
                       f"{sum(1 for x in changes['changed'] if x[0]['tier'] == tier)} |")
        fmt = lambda v: "—" if not v else ", ".join(v) if len(v) < 4 else f"{len(v)} candidates"  # noqa: E731
        for kind in ("regressed", "fixed", "changed"):
            rows = sorted(changes[kind], key=lambda x: (x[0]["tier"] != "gold", x[0]["case_id"]))
            if not rows:
                continue
            out += ["", f"### {kind.capitalize()} ({len(rows)})", "",
                    "| case | tier | file | expected | before | now | tags |", "|---|---|---|---|---|---|---|"]
            for c, old, new in rows[:200]:
                out.append(f"| `{c['case_id']}` | {c['tier']} | [`{c['filename']}`](https://archive.softwareheritage.org/"
                           f"{c['qualified_swhid']}/) | {c['expected']} | {fmt(old)} | {fmt(new)} | {c['tags']} |")
            if len(rows) > 200:
                out.append(f"| … {len(rows) - 200} more | | | | | | |")
        summary["baseline"] = {k: len(v) for k, v in changes.items()}

    text = "\n".join(out) + "\n"
    if a.report:
        a.report.write_text(text, encoding="utf-8")
    parts = [f"{t} {m['right']}/{m['n']} ({pct(m['accuracy'])})" for t, m in summary.items() if t in ("gold", "silver")]
    w = summary.get("gold", {}).get("weighted")
    print(f"{meta.get('label')}: " + ", ".join(parts)
          + (f", weighted {pct(w['accuracy'])}" if w else "")
          + (f" · vs baseline: {summary['baseline']}" if "baseline" in summary else ""))
    if regressions:
        print(f"REGRESSIONS ({a.fail_on}): " + ", ".join(c["case_id"] for c, _, _ in regressions[:20]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
