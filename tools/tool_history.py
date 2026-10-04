#!/usr/bin/env python3
"""Non-regression across the releases of another identifier: TOOL-HISTORY.md at
the repository root — for each tool family, on each benchmark, the score of every
release that was run there and what changed from one release to the next.

    python3 tools/tool_history.py --tool linguist pygments magika enry
    python3 tools/tool_history.py            # every tool with older releases in tools/external/

A family is tools/external/<tool>/ (the current release) and its siblings
tools/external/<tool>-<x>/ (older releases, e.g. linguist-v7), each run with
tools/external.py, so its entries are <bench>/entries/ext-<dir>.jsonl and
ext-<dir>-content-only.jsonl. Releases are ordered by version (the image tag in
the entry's meta; tool.json's otherwise). For each benchmark and each mode
(default, content only) where at least two releases were run: right/total per
release (right = exactly one language and an accepted one, as in score.py),
then, between consecutive releases, the cases fixed (not right → right) and
regressed (right → not right), grouped by expected language (the 10 with the
most cases), each with its most frequent changes of answer. A benchmark whose
contamination.json names a release says so: that release was built from (part
of) the benchmark's files. Exit status 0.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import outcome, pct, read_cases, read_run  # noqa: E402

EXT = ROOT / "tools" / "external"
MODES = (("default", ""), ("content only", "-content-only"))
TOP = 10


def family(tool: str) -> list[str]:
    """tools/external/<tool>/ and its siblings <tool>-<x>/ that have a tool.json."""
    return sorted(p.parent.name for p in EXT.glob(f"{tool}*/tool.json")
                  if p.parent.name == tool or p.parent.name.startswith(tool + "-"))


def version_key(version: str) -> tuple:
    """1.10.0 after 1.9.2; a version that is not dotted numbers (a commit) sorts last, as given."""
    m = re.fullmatch(r"v?(\d+(?:\.\d+)*)", version)
    return (0, tuple(int(x) for x in m.group(1).split("."))) if m else (1, version)


def read_contamination(bench: Path) -> dict[str, str]:
    p = bench / "contamination.json"
    return {k: v for k, v in json.loads(p.read_text(encoding="utf-8")).items() if not k.startswith("_")} \
        if p.exists() else {}


def fmt(answer: list[str] | None) -> str:
    return "—" if not answer else ", ".join(answer) if len(answer) < 4 else f"{len(answer)} candidates"


def plural(n: int, word: str) -> str:
    return f"{n} {word}{'' if n == 1 else 's'}"


def releases(bench: Path, dirs: list[str], suffix: str) -> list[dict]:
    """The family's entries on this benchmark in one mode, oldest release first."""
    out = []
    for d in dirs:
        p = bench / "entries" / f"ext-{d}{suffix}.jsonl"
        if not p.exists():
            continue
        meta, ans = read_run(p)
        m = re.search(r":(\S+)", meta.get("version", ""))
        version = m.group(1) if m else json.loads((EXT / d / "tool.json").read_text(encoding="utf-8"))["version"]
        out.append({"dir": d, "label": meta.get("label", p.stem), "name": meta.get("name", d),
                    "version": version, "ans": ans})
    return sorted(out, key=lambda r: version_key(r["version"]))


def step(cases: dict, old: dict, new: dict, mode: str) -> tuple[list[str], dict[str, list]]:
    """Lines comparing two consecutive releases, and the fixed / regressed cases."""
    moved = {"fixed": [], "regressed": []}
    for cid, c in cases.items():
        a, b = old["ans"].get(cid), new["ans"].get(cid)
        was, now = outcome(c, a) == "right", outcome(c, b) == "right"
        if was != now:
            moved["fixed" if now else "regressed"].append((c, a, b))
    lines = [f"#### {mode + ': ' if mode != 'default' else ''}{old['version']} → {new['version']}: "
             f"{len(moved['fixed'])} fixed, "
             f"{len(moved['regressed'])} regressed (net {len(moved['fixed']) - len(moved['regressed']):+d})"]
    for kind in ("regressed", "fixed"):
        rows = moved[kind]
        if not rows:
            continue
        by_lang = defaultdict(list)
        for c, a, b in rows:
            by_lang[c["expected"]].append((fmt(a), fmt(b)))
        langs = sorted(by_lang, key=lambda g: (-len(by_lang[g]), g))
        lines += ["", f"{kind.capitalize()} ({plural(len(rows), 'case')}, {plural(len(langs), 'language')}), "
                      "by expected language:", "",
                  f"| expected | cases | answer {old['version']} → {new['version']} |", "|---|---:|---|"]
        for g in langs[:TOP]:
            ch = Counter(by_lang[g]).most_common()
            text = "; ".join(f"{a} → {b}" + (f" ×{n}" if n > 1 else "") for (a, b), n in ch[:3])
            more = sum(n for _, n in ch[3:])
            lines.append(f"| {g} | {len(by_lang[g])} | {text}" + (f"; {more} other" if more else "") + " |")
        if len(langs) > TOP:
            lines.append(f"| … {len(langs) - TOP} more languages | {sum(len(by_lang[g]) for g in langs[TOP:])} | |")
    return lines, moved


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tool", nargs="+", help="tool families (default: every tool with older releases)")
    a = ap.parse_args()
    tools = a.tool or sorted(t for t in (p.parent.name for p in EXT.glob("*/tool.json")) if len(family(t)) > 1)
    benches = sorted(p.parent for p in (ROOT / "benchmarks").glob("*/cases.csv"))
    summary = ["| tool | benchmark | mode | right per release, oldest → newest | fixed / regressed per step |",
               "|---|---|---|---|---|"]
    body = []
    for tool in tools:
        dirs = family(tool)
        if not dirs:
            raise SystemExit(f"no tools/external/{tool}*/tool.json")
        base = json.loads((EXT / (tool if tool in dirs else dirs[0]) / "tool.json").read_text(encoding="utf-8"))
        title = base["name"].replace(base["version"], "").strip()
        body += ["", f"## {title} (`tools/external/{{{','.join(dirs)}}}`)"]
        alone = []
        for bench in benches:
            cases = read_cases(bench)
            cont = read_contamination(bench)
            runs = {mode: releases(bench, dirs, suffix) for mode, suffix in MODES}
            if max(len(rs) for rs in runs.values()) < 2:
                if runs["default"]:
                    alone.append(f"{bench.name} ({runs['default'][0]['version']})")
                continue
            body += ["", f"### {title} on {bench.name} ({len(cases)} cases)", "",
                     "| release | entry | right | accuracy | trained on these files |", "|---|---|---:|---:|---|"]
            for mode, _ in MODES:
                for r in runs[mode]:
                    right = sum(1 for cid, c in cases.items() if outcome(c, r["ans"].get(cid)) == "right")
                    seen = next((v for k, v in cont.items() if r["name"].startswith(k)), "")
                    body.append(f"| {r['version']}{', ' + mode if mode != 'default' else ''} | `{r['label']}` | "
                                f"{right}/{len(cases)} | {pct(right / len(cases))} | {seen} |")
            for mode, _ in MODES:
                rs = runs[mode]
                if len(rs) < 2:
                    continue
                steps = []
                for old, new in zip(rs, rs[1:]):
                    lines, moved = step(cases, old, new, mode)
                    body += [""] + lines
                    steps.append(f"{old['version']} → {new['version']}: +{len(moved['fixed'])} / "
                                 f"−{len(moved['regressed'])}")
                rights = [sum(1 for cid, c in cases.items() if outcome(c, r["ans"].get(cid)) == "right") for r in rs]
                summary.append(f"| {title} | {bench.name} | {mode} | "
                               + " → ".join(f"{r['version']} {k}" for r, k in zip(rs, rights))
                               + f" (of {len(cases)}) | {'; '.join(steps)} |")
        if alone:
            body += ["", f"Run with one release only (not compared): {'; '.join(alone)}."]
    lines = ["# Other identifiers across their releases", "",
             f"Generated by `python3 tools/tool_history.py --tool {' '.join(tools)}` from the benchmarks' "
             "`entries/ext-<tool>[-<release>][-content-only].jsonl` (each release in its pinned Docker image, "
             "`tools/external/<tool>[-<release>]/`). Right = exactly one language, and an accepted one (as in "
             "`tools/score.py`). *Fixed*: not right in the older release, right in the newer; *regressed*: the "
             "reverse. A release trained on (part of) a benchmark's files says so (the benchmark's "
             "`contamination.json`): its score there is partly accuracy on training data.", "", *summary, *body]
    out = ROOT / "TOOL-HISTORY.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(tools)} tool(s), {len(summary) - 2} comparison(s) → {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
