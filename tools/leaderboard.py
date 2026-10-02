#!/usr/bin/env python3
"""Leaderboards: one per benchmark (benchmarks/<name>/LEADERBOARD.md) and an
overall one (LEADERBOARD.md), from every recorded run — Synid versions
(baselines/) and other entries (entries/: Synid configurations, other
identifiers, specialised rules, LLM judges, the ground truth itself).

    python3 tools/leaderboard.py

Ranking: accuracy (exactly one syntax, and an accepted one), then precision of
language answers. The ground truth and the LLM judges whose agreement backs it
are listed apart as references, not ranked. Overall: an entry is the same system
and configuration across benchmarks; micro = all cases pooled, macro = mean of
the benchmarks' accuracies; only benchmarks the entry was run on count.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import metrics, pct, read_cases, read_run  # noqa: E402

SYNID_REPO = "https://gitlab.softwareheritage.org/teams/codecommons/swh-syntax-identification"
KIND = {"synid": "Synid", "specialised": "specialised rules", "other-identifier": "other identifier",
        "llm-light": "lightweight LLM", "llm-judge": "LLM judge", "ground-truth": "ground truth"}
REFERENCE_KINDS = ("ground-truth", "llm-judge")
HOW_TO_READ = [
    "**How to read.** Every entry answers, for each file, the language it is written in. A case is right when the "
    "answer is exactly one language and an accepted one; *no answer / undecided* means the entry abstained or "
    "returned several candidates; `Text` means it called a source file plain text. The ground truth is a blind "
    "human review of every file (shown under *References*, right by definition), cross-checked by two LLM judges "
    "that agree with it on every case. **Kinds:** *Synid* — a version of Synid, the CodeCommons syntax-identification tool, in its "
    "default configuration or with one strategy turned off (a setting of Synid's configuration file); "
    "*other identifier* — another tool, as a reference point; *specialised rules* — rules written for one "
    "benchmark's problem only, a ceiling for what targeted rules achieve rather than a general identifier; "
    "*lightweight LLM* — a small, cheap model asked the language (not used to build the ground truth).",
]


def entry_name(meta: dict) -> str:
    if meta.get("name"):
        return meta["name"]
    dis = meta.get("disabled") or []
    return f"Synid {meta.get('commit') or '?'}" + (f", {' + '.join(dis)} off" if dis else "")


def entry_info(meta: dict) -> dict:
    """Name, kind, version, configuration, what it is, where to find it."""
    kind = meta.get("kind", "synid")
    if kind == "synid":
        version = (f"`{meta.get('commit')}` — {meta.get('date', '?')}, "
                   f"{meta.get('commit_subject', '')}".rstrip(", "))
        return {"name": entry_name(meta), "kind": KIND["synid"], "version": version,
                "config": meta.get("config", "default strategies"),
                "about": "Synid, the CodeCommons syntax-identification tool (`synid file`)",
                "url": SYNID_REPO, "where": "Synid repository (access-restricted)"}
    return {"name": entry_name(meta), "kind": KIND.get(kind, kind), "version": meta.get("version", ""),
            "config": "—", "about": meta.get("about") or meta.get("note", ""),
            "url": meta.get("url", ""), "where": "source" if meta.get("url") else ""}


def info_table(infos: list[dict]) -> list[str]:
    out = ["| entry | kind | version | configuration | what it is | where |", "|---|---|---|---|---|---|"]
    for i in infos:
        where = f"[{i['where']}]({i['url']})" if i["url"] else "—"
        out.append(f"| {i['name']} | {i['kind']} | {i['version']} | {i['config']} | {i['about']} | {where} |")
    return out


def load_runs(bench: Path) -> list[tuple[dict, dict, str]]:
    runs = []
    for sub in ("baselines", "entries"):
        for p in sorted((bench / sub).glob("*.jsonl")) if (bench / sub).is_dir() else []:
            meta, ans = read_run(p)
            runs.append((meta, ans, sub))
    return runs


def bench_board(bench: Path) -> tuple[str, dict[str, dict], list[dict]]:
    cases = read_cases(bench)
    ids = list(cases)
    tags: dict[str, list[str]] = {}
    for cid, c in cases.items():
        for t in filter(None, c.get("tags", "").split(";")):
            tags.setdefault(t, []).append(cid)
    tag_names = sorted(tags, key=lambda t: -len(tags[t]))
    has_weights = any(c.get("weight") for c in cases.values())
    version = (bench / "cases.csv").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0]
    rows, refs, by_name, infos = [], [], {}, []
    for meta, ans, sub in load_runs(bench):
        m = metrics(cases, ans, ids, weighted=has_weights)
        info = entry_info(meta)
        rec = {"name": info["name"], "meta": meta, "m": m, "baseline": sub == "baselines", "info": info,
               "tags": {t: metrics(cases, ans, tags[t])["right"] for t in tag_names}}
        (refs if meta.get("kind") in REFERENCE_KINDS else rows).append(rec)
        by_name[info["name"]] = {"right": m["right"], "n": m["n"], "accuracy": m["accuracy"],
                                 "kind": meta.get("kind", "synid")}
        infos.append(info)
    rows.sort(key=lambda r: (-(r["m"]["accuracy"] or 0), -(r["m"]["precision"] or 0), r["name"]))
    refs.sort(key=lambda r: (r["meta"].get("kind") != "ground-truth", r["name"]))

    def line(rank, r):
        m, o = r["m"], r["m"]["outcomes"]
        w = f" | {pct(m['weighted']['accuracy'])}" if has_weights else ""
        return (f"| {rank} | {r['name']}{' (baseline)' if r['baseline'] else ''} | {r['info']['kind']} | "
                f"**{m['right']}/{m['n']}** ({pct(m['accuracy'])}) [{pct(m['ci'][0])}, {pct(m['ci'][1])}]{w} | "
                f"{pct(m['precision'])} | {o.get('text', 0)} | {o.get('undecided', 0) + o.get('none', 0)} | "
                f"{o.get('wrong', 0)} | " + " | ".join(f"{r['tags'][t]}/{len(tags[t])}" for t in tag_names) + " |")

    head = ("| # | entry | kind | right (accuracy) [95 % CI]" + (" | weighted to the population" if has_weights else "")
            + " | precision of language answers | `Text` on code | no answer / undecided | wrong language | "
            + " | ".join(f"`{t}`" for t in tag_names) + " |")
    sep = "|---:|---|---|---:|" + ("---:|" if has_weights else "") + "---:|---:|---:|---:|" + "---:|" * len(tag_names)
    out = [f"# Leaderboard — {bench.name}", "",
           f"Generated by `python3 tools/leaderboard.py` · benchmark `{version}`, {len(ids)} cases "
           f"([README](README.md) · [history of Synid versions](HISTORY.md)). Ranked by accuracy, then precision of "
           "language answers. Trigger columns: right / cases carrying that failure trigger (see the README)"
           + ("; *weighted to the population* re-weights the stratified draw to all files of the extension in "
              "Software Heritage" if has_weights else "") + ".", "", *HOW_TO_READ, "", head, sep]
    out += [line(i, r) for i, r in enumerate(rows, 1)]
    if refs:
        out += ["", "## References (not ranked)", "",
                "The ground truth, and the LLM judges whose agreement with it backs the benchmark's labels — "
                "neither is independent of the ground truth.", "", head, sep]
        out += [line("–", r) for r in refs]
    out += ["", "## Entries", ""] + info_table([r["info"] for r in rows + refs])
    return "\n".join(out) + "\n", by_name, [r["info"] for r in rows + refs]


def main() -> int:
    benches = sorted(p for p in (ROOT / "benchmarks").iterdir() if (p / "cases.csv").exists())
    per_bench: dict[str, dict[str, dict]] = {}
    all_infos: dict[str, dict] = {}
    for b in benches:
        text, by_name, infos = bench_board(b)
        (b / "LEADERBOARD.md").write_text(text, encoding="utf-8")
        per_bench[b.name] = by_name
        for i in infos:
            all_infos.setdefault(i["name"], i)
        print(f"{b.name}: {len(by_name)} entries → {(b / 'LEADERBOARD.md').relative_to(ROOT)}")
    rows = []
    for n in sorted({n for d in per_bench.values() for n in d}):
        got = {b: d[n] for b, d in per_bench.items() if n in d}
        right, total = sum(g["right"] for g in got.values()), sum(g["n"] for g in got.values())
        macro = sum(g["accuracy"] for g in got.values()) / len(got)
        rows.append((n, next(iter(got.values()))["kind"], got, right, total, macro))
    ranked = sorted((r for r in rows if r[1] not in REFERENCE_KINDS), key=lambda r: (-r[3] / r[4], -r[5], r[0]))
    refs = sorted((r for r in rows if r[1] in REFERENCE_KINDS), key=lambda r: (r[1] != "ground-truth", r[0]))
    bnames = [b.name for b in benches]
    head = ("| # | entry | kind | benchmarks | right, all cases (micro) | mean accuracy (macro) | "
            + " | ".join(f"[{b}](benchmarks/{b}/LEADERBOARD.md)" for b in bnames) + " |")
    sep = "|---:|---|---|---:|---:|---:|" + "---:|" * len(bnames)

    def line(rank, r):
        n, kind, got, right, total, macro = r
        cells = [f"{got[b]['right']}/{got[b]['n']}" if b in got else "—" for b in bnames]
        return (f"| {rank} | {n} | {KIND.get(kind, kind)} | {len(got)}/{len(bnames)} | **{right}/{total}** "
                f"({pct(right / total)}) | {pct(macro)} | " + " | ".join(cells) + " |")

    out = ["# Leaderboard — all benchmarks", "",
           "Generated by `python3 tools/leaderboard.py`. Each benchmark has its own leaderboard (linked in the "
           "header) with intervals, population weights and failure triggers. An entry is one system and "
           "configuration; *micro* pools the cases of every benchmark it was run on, *macro* averages its "
           "accuracies over those benchmarks.", "", *HOW_TO_READ, "", head, sep]
    out += [line(i, r) for i, r in enumerate(ranked, 1)]
    if refs:
        out += ["", "## References (not ranked)", "", head, sep] + [line("–", r) for r in refs]
    out += ["", "## Entries", ""] + info_table([all_infos[r[0]] for r in ranked + refs])
    (ROOT / "LEADERBOARD.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"overall: {len(ranked)} ranked entries, {len(refs)} references → LEADERBOARD.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
