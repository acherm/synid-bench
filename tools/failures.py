#!/usr/bin/env python3
"""Failure report: every case a run gets wrong, grouped by root cause, with the program
→ <bench>/FAILURES.md (or FAILURES-<run>.md for a run other than the latest Synid baseline).

    python3 tools/failures.py benchmarks/bench-m                 # latest baseline vs the previous one
    python3 tools/failures.py benchmarks/bench-m --run 48c3c45-default --previous 9bc1c32-default
    python3 tools/failures.py benchmarks/bench-linguist --synid path/to/synid
    python3 tools/failures.py benchmarks/bench-linguist --run jev-cascade

Root causes come from the benchmark's own `root_causes.py` (CAUSES: title, mechanism,
evidence, how it was verified, suggested fix; diagnose(case, text, answers[, run, ctx]) →
cause id; optionally load_ctx(bench, synid_names) → ctx). Without one, failures are
grouped by outcome and tags. A large benchmark gets a summary per cause — counts, the
expected languages and answers most involved, the share of files seen in training — and
a few example programs instead of all of them (--examples).
"""

from __future__ import annotations

import argparse
import importlib.util
import inspect
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import name_key, outcome, read_cases, read_run  # noqa: E402

EXCERPT_LINES = 14
SWH = "https://archive.softwareheritage.org"
LARGE = 80  # more failures than this: summary mode


def load_causes(bench: Path):
    p = bench / "root_causes.py"
    if not p.exists():
        return {}, None, None
    spec = importlib.util.spec_from_file_location(f"root_causes_{bench.name}", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CAUSES, mod.diagnose, getattr(mod, "load_ctx", None)


def runs_by_label(bench: Path) -> dict[str, tuple[dict, dict]]:
    out = {}
    for sub in ("baselines", "entries"):
        for p in sorted((bench / sub).glob("*.jsonl")) if (bench / sub).is_dir() else []:
            meta, ans = read_run(p)
            out[p.stem] = (meta, ans)
    return out


def latest_two_baselines(bench: Path) -> tuple[str, str | None]:
    bs = []
    for p in (bench / "baselines").glob("*.jsonl"):
        meta = json.loads(p.read_text(encoding="utf-8").splitlines()[0])["meta"]
        bs.append((meta.get("date", ""), p.stem))
    bs.sort()
    return bs[-1][1], (bs[-2][1] if len(bs) > 1 else None)


def excerpt(raw: bytes, n_lines: int = EXCERPT_LINES) -> tuple[str, str]:
    try:
        text, note = raw.decode("utf-8"), ""
    except UnicodeDecodeError:
        text, note = raw.decode("latin-1"), " (not valid UTF-8 — shown as Latin-1)"
    lines = [ln.rstrip()[:110] for ln in text.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    shown = lines[:n_lines]
    more = len(lines) - len(shown)
    body = "\n".join(shown).replace("```", "``​`")
    return body + (f"\n… ({more} more lines)" if more > 0 else ""), note


def fmt(ans) -> str:
    if not ans:
        return "no answer"
    return ans[0] if len(ans) == 1 else f"undecided ({len(ans)} candidates)"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bench", type=Path)
    ap.add_argument("--run", help="run label (default: latest baseline)")
    ap.add_argument("--previous", help="earlier run to compare with (default: the baseline before it)")
    ap.add_argument("--synid", help="a synid binary, to tell the languages it cannot name (`synid info syntaxes`)")
    ap.add_argument("--examples", type=int, default=3, help="example programs per cause, in summary mode")
    a = ap.parse_args()
    bench = a.bench.resolve()
    cases = read_cases(bench)
    runs = runs_by_label(bench)
    latest, prev = latest_two_baselines(bench)
    run_l = a.run or latest
    prev_l = a.previous or (prev if run_l == latest else None)
    meta, ans = runs[run_l]
    causes, diagnose, load_ctx = load_causes(bench)
    synid_names = None
    if a.synid:
        out = subprocess.run([a.synid, "info", "syntaxes"], capture_output=True, text=True).stdout
        synid_names = {name_key(x) for x in out.splitlines() if x.strip()}
    ctx = load_ctx(bench, synid_names) if load_ctx else None
    extended = diagnose is not None and len(inspect.signature(diagnose).parameters) > 3
    answers_all = {lab: r[1] for lab, r in runs.items()}
    is_synid = meta.get("kind", "synid") == "synid"
    who = f"Synid {meta.get('commit', '?')}" if is_synid else meta.get("name", run_l)

    def case_answers(cid):
        return {lab: a_.get(cid) for lab, a_ in answers_all.items()}

    def text_of(c):
        return (bench / "files" / c["sha1_git"]).read_bytes().decode("utf-8", "replace")

    def cause_of(c, cid, run):
        if not diagnose:
            return None
        if extended:
            return diagnose(c, text_of(c), case_answers(cid), run, ctx)
        return diagnose(c, text_of(c), case_answers(cid))

    failing = [cid for cid, c in cases.items() if outcome(c, ans.get(cid)) != "right"]
    groups = defaultdict(list)
    for cid in failing:
        c = cases[cid]
        groups[cause_of(c, cid, run_l) or f"{outcome(c, ans.get(cid))}: {c['tags'] or 'no tag'}"].append(cid)
    fixed = []
    if prev_l and prev_l in runs:
        pans = runs[prev_l][1]
        fixed = [cid for cid, c in cases.items()
                 if outcome(c, pans.get(cid)) != "right" and outcome(c, ans.get(cid)) == "right"]
    large = len(failing) > LARGE

    title = who + (f" ({meta['date']})" if meta.get("date") and is_synid else "")
    out_name = "FAILURES.md" if run_l == latest else f"FAILURES-{run_l}.md"
    out = [f"# Failure report — {bench.name}, {title}", "",
           f"Generated by `python3 tools/failures.py benchmarks/{bench.name}"
           + (f" --run {run_l}" if run_l != latest else "") + "`. Every case "
           f"`{run_l}` gets wrong ({len(failing)} of {len(cases)}), grouped by root cause"
           + (f" — a summary per cause and {a.examples} example programs each" if large else
              f", with the program, {'Synid' if is_synid else 'the entry'}'s answer, the expected language "
              "(the benchmark's reference) and the evidence")
           + (f"; then the cases fixed since `{prev_l}`." if prev_l and not large else ".")
           + " Root causes are documented in `root_causes.py`.", "",
           ""]
    has_seen = any("seen-in-training" in c["tags"] for c in cases.values())
    out[-1:] = (["| root cause | files | of which seen in training | suggested fix | verified by |",
                 "|---|---:|---:|---|---|"] if has_seen else
                ["| root cause | files | suggested fix | verified by |", "|---|---:|---|---|"])
    order = sorted(groups, key=lambda g: -len(groups[g]))
    for g in order:
        cz = causes.get(g, {})
        seen = sum(1 for cid in groups[g] if "seen-in-training" in cases[cid]["tags"])
        out.append(f"| [{cz.get('title', g)}](#{g}) | {len(groups[g])} | " + (f"{seen} | " if has_seen else "")
                   + f"{cz.get('fix', '—')} | {cz.get('verified', '—')} |")
    if fixed:
        out.append(f"| *fixed since `{prev_l}`* | {len(fixed)} | " + ("| " if has_seen else "") + "| |")

    ablations = [lab for lab, (m, _) in runs.items() if m.get("kind", "synid") == "synid" and m.get("disabled")
                 and m.get("commit") == meta.get("commit")] if is_synid else []

    def case_block(cid, show_prev=False, n_lines=EXCERPT_LINES, heading="####"):
        c = cases[cid]
        raw = (bench / "files" / c["sha1_git"]).read_bytes()
        body, note = excerpt(raw, n_lines)
        a_ = case_answers(cid)
        ev = [f"{'Synid' if is_synid else 'answer'} `{run_l}`: **{fmt(a_[run_l])}**"]
        if show_prev:
            ev.append(f"before (`{prev_l}`): {fmt(a_[prev_l])}")
        for lab in ablations:
            d = ", ".join(runs[lab][0].get("disabled") or [])
            ev.append(f"without {d}: {fmt(a_[lab])}")
        if "linguist" in a_ and bench.name == "bench-m":
            ev.append(f"Linguist `.m` rules: {fmt(a_['linguist'])}")
        return [f"{heading} `{c['filename']}`", "",
                f"expected **{c['expected_detail']}** · [archived file]({SWH}/{c['qualified_swhid']}/)"
                + (f" · [in this benchmark](files/{c['sha1_git']})" if (bench / "files" / c["sha1_git"]).exists()
                   and bench.name == "bench-m" else "")
                + f" · {len(raw):,} bytes" + (f" · tags: {c['tags']}" if c["tags"] else ""), "",
                " · ".join(ev), "", f"```{note}", body, "```", ""]

    for g in order:
        cz = causes.get(g, {})
        ids = sorted(groups[g], key=lambda i: cases[i]["filename"].lower())
        out += ["", f'<a id="{g}"></a>', f"## {cz.get('title', g)} — {len(ids)} file(s)", ""]
        if cz:
            out += [f"**Mechanism.** {cz['mechanism']}", ""]
            if cz.get("evidence"):
                out += [f"**Evidence.** {cz['evidence']}.", ""]
            out += [f"**Verified.** {cz['verified']}.", "", f"**Suggested fix.** {cz['fix']}.", ""]
        if not large:
            for cid in ids:
                out += case_block(cid)
            continue
        exp = Counter(cases[i]["expected"] for i in ids)
        pairs = Counter((cases[i]["expected"], fmt(ans.get(i))) for i in ids)
        exts = Counter(cases[i]["ext"] or "(file name)" for i in ids)
        seen = sum(1 for i in ids if "seen-in-training" in cases[i]["tags"])
        out += [f"{len(exp)} languages · {seen} of the {len(ids)} files seen in training · extensions: "
                + ", ".join(f"`{e}` {n}" for e, n in exts.most_common(8)), "",
                "| expected → answer | files |", "|---|---:|"]
        out += [f"| {e} → {r} | {n} |" for (e, r), n in pairs.most_common(12)]
        if len(pairs) > 12:
            out.append(f"| … {len(pairs) - 12} more pairs | {sum(n for _, n in pairs.most_common()[12:])} |")
        out.append("")
        # examples: the most common pairs first, one file each
        picked, seen_pairs = [], set()
        for (e, r), _ in pairs.most_common():
            cid = next(i for i in ids if (cases[i]["expected"], fmt(ans.get(i))) == (e, r))
            if (e, r) not in seen_pairs:
                picked.append(cid)
                seen_pairs.add((e, r))
            if len(picked) >= a.examples:
                break
        out += ["Examples:", ""]
        for cid in picked:
            out += case_block(cid, n_lines=8, heading="#####")
    if fixed and not large:
        out += ["", f"## Fixed since `{prev_l}` — {len(fixed)} file(s)", ""]
        for cid in fixed:
            c = cases[cid]
            pg = cause_of(c, cid, prev_l)
            if pg and pg in causes:
                out += [f"**{causes[pg]['title']}.** {causes[pg]['mechanism']} *{causes[pg]['verified']}.*", ""]
            out += case_block(cid, show_prev=True)
    elif fixed:
        out += ["", f"## Fixed since `{prev_l}` — {len(fixed)} file(s)", "",
                ", ".join(f"`{cases[i]['filename']}` ({cases[i]['expected']})" for i in fixed[:60])
                + (" …" if len(fixed) > 60 else "")]
    (bench / out_name).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{bench.name}: {len(failing)} failures of {run_l} in {len(groups)} group(s), {len(fixed)} fixed since "
          f"{prev_l} → {(bench / out_name)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
