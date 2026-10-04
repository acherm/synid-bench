#!/usr/bin/env python3
"""Leaderboards: one per benchmark (benchmarks/<name>/LEADERBOARD.md) and an
overall one (LEADERBOARD.md), from every recorded run — Synid versions
(baselines/) and other entries (entries/: Synid configurations, other
identifiers, specialised rules, LLM judges, the ground truth itself).

    python3 tools/leaderboard.py

Ranking on a benchmark: accuracy (exactly one syntax, and an accepted one), then
precision of language answers. The ground truth and the LLM judges whose
agreement backs it are listed apart as references, not ranked.

Overall: an entry is the same system and configuration across benchmarks. The
benchmarks differ in what they measure — each has a card (card.json: unit, file
names, who labelled, sampling, home turf, strengths, weaknesses) — and some are
the training or development data of some entries (contamination.json: † — the
entry's *home turf*). Entries are ranked by their mean accuracy over the
benchmarks they were run on that are not their home turf (*held-out mean*); an
entry run on fewer than half of the benchmarks is listed apart. A tool that
answers from the file name only is *not applicable* (n/a) on a benchmark without
file names. The report also says how far the benchmarks agree on the order of
the entries (Kendall's τ), and where each benchmark's home-turf entries rank.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import metrics, pct, read_cases, read_run  # noqa: E402

SYNID_REPO = "https://gitlab.softwareheritage.org/teams/codecommons/swh-syntax-identification"
KIND = {"synid": "Synid", "specialised": "specialised rules", "other-identifier": "other identifier",
        "llm-light": "lightweight LLM", "cascade": "candidates + lightweight LLM", "llm-judge": "LLM judge",
        "ground-truth": "ground truth"}
REFERENCE_KINDS = ("ground-truth", "llm-judge")
KINDS_TEXT = (
    "**Kinds:** *Synid* — a version of Synid, the CodeCommons syntax-identification tool, in its "
    "default configuration or with one strategy turned off (a setting of Synid's configuration file); "
    "*other identifier* — another tool, as a reference point; *specialised rules* — rules written for one "
    "benchmark's problem only, a ceiling for what targeted rules achieve rather than a general identifier; "
    "*lightweight LLM* — a small, cheap model asked the language (not used to build the ground truth); "
    "*candidates + lightweight LLM* — the languages PL-ultimate-llm associates with the file's extension, among "
    "which the model chooses (a broad list when none fits).")


def how_to_read(cards: dict[str, dict]) -> list[str]:
    labels = "; ".join(f"{b}: {c['labels']}" for b, c in cards.items() if c.get("labels"))
    return [
        "**How to read.** Every entry answers, for each file, the language it is written in. A case is right when "
        "the answer is exactly one language and an accepted one; *no answer / undecided* means the entry abstained "
        "or returned several candidates; `Text` means it called a source file plain text. Each benchmark's README "
        "says where its labels come from" + (f" ({labels})" if labels else "") + ". " + KINDS_TEXT]


def read_card(bench: Path) -> dict:
    p = bench / "card.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def read_contamination(bench: Path) -> dict[str, dict]:
    """Entry-name prefix → {"why", "cases"}: the cases that are the entry's home turf (its training or development
    data), or None when the whole benchmark is (a plain text value in contamination.json)."""
    p = bench / "contamination.json"
    if not p.exists():
        return {}
    cases = None
    out = {}
    for k, v in json.loads(p.read_text(encoding="utf-8")).items():
        if k.startswith("_"):
            continue
        if isinstance(v, str):
            out[k] = {"why": v, "cases": None}
            continue
        if v.get("cases_tag"):
            cases = cases or read_cases(bench)
            ids = {i for i, c in cases.items() if v["cases_tag"] in c.get("tags", "").split(";")}
        else:
            ids = set(v.get("cases", []))
        out[k] = {"why": v["why"], "cases": ids}
    return out


def home_turf(name: str, cont: dict[str, dict]) -> tuple[str | None, set[str]]:
    """("full", ∅) when the benchmark is the entry's home turf, ("partial", the cases that are), or (None, ∅)."""
    hits = [v for k, v in cont.items() if name.startswith(k)]
    if any(v["cases"] is None for v in hits):
        return "full", set()
    ids = set().union(*(v["cases"] for v in hits)) if hits else set()
    return ("partial", ids) if ids else (None, set())


def needs_name(meta: dict) -> bool:
    """An external tool that answers from the file name only (tools/external/<tool>/tool.json)."""
    label = meta.get("label", "")
    if not label.startswith("ext-"):
        return False
    p = ROOT / "tools" / "external" / label.removeprefix("ext-").removesuffix("-content-only") / "tool.json"
    return p.exists() and json.loads(p.read_text(encoding="utf-8")).get("needs_name", False)


def older_release_of(meta: dict) -> str | None:
    """An older release of an external tool (tool.json `older_release_of`), kept for non-regression."""
    label = meta.get("label", "")
    if not label.startswith("ext-"):
        return None
    p = ROOT / "tools" / "external" / label.removeprefix("ext-").removesuffix("-content-only") / "tool.json"
    return json.loads(p.read_text(encoding="utf-8")).get("older_release_of") if p.exists() else None


def not_applicable(meta: dict, card: dict) -> str | None:
    if card.get("names") == "none" and needs_name(meta):
        return "answers from the file name only; this benchmark has no file names"
    return None


def entry_name(meta: dict) -> str:
    if meta.get("name"):
        return meta["name"]
    dis = meta.get("disabled") or []
    return (f"Synid {meta.get('commit') or '?'}" + (f", {' + '.join(dis)} off" if dis else "")
            + (", content only" if meta.get("content_only") else ""))


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


def card_lines(card: dict) -> list[str]:
    """The benchmark card, as a few lines at the top of its leaderboard."""
    if not card:
        return []
    out = [f"**What it is.** {card.get('title', '')} — {card.get('cases', '?')} cases ({card.get('unit', '?')}), "
           f"{card.get('languages', '?')} languages · labels: {card.get('labels', '?')} · file names: "
           f"{card.get('names', '?')} · sampling: {card.get('sampling', '?')} · source: {card.get('source', '?')}."]
    if card.get("strengths"):
        out.append("**Strengths.** " + "; ".join(card["strengths"]) + ".")
    if card.get("weaknesses"):
        out.append("**Weaknesses.** " + "; ".join(card["weaknesses"]) + ".")
    return [" ".join(out), ""]


def load_runs(bench: Path) -> list[tuple[dict, dict, str]]:
    runs = []
    for sub in ("baselines", "entries"):
        for p in sorted((bench / sub).glob("*.jsonl")) if (bench / sub).is_dir() else []:
            meta, ans = read_run(p)
            runs.append((meta, ans, sub))
    return runs


def bench_board(bench: Path, cards: dict[str, dict],
                elsewhere: dict[str, dict] | None = None) -> tuple[str, dict[str, dict], list[dict]]:
    """elsewhere: entries run on other benchmarks (name → meta), listed when not run on this one."""
    cases = read_cases(bench)
    card = cards.get(bench.name, {})
    # a benchmark whose card names a headline tier (e.g. gold: the labels a human checked) is ranked on those
    # cases; the other tiers are shown beside it
    head_tier = card.get("headline_tier")
    every = list(cases)
    ids = [i for i in every if cases[i].get("tier") == head_tier] if head_tier else every
    tags: dict[str, list[str]] = {}
    for cid, c in cases.items():
        for t in filter(None, c.get("tags", "").split(";")):
            tags.setdefault(t, []).append(cid)
    tag_names = sorted(tags, key=lambda t: -len(tags[t]))
    has_weights = any(c.get("weight") for c in cases.values())
    version = (bench / "cases.csv").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0]
    rows, refs, by_name, infos = [], [], {}, []
    cont = read_contamination(bench)
    for meta, ans, sub in load_runs(bench):
        m = metrics(cases, ans, ids, weighted=has_weights)
        info = entry_info(meta)
        rec = {"name": info["name"], "meta": meta, "m": m, "baseline": sub == "baselines", "info": info,
               "tags": {t: metrics(cases, ans, tags[t])["right"] for t in tag_names},
               "all": metrics(cases, ans, every) if head_tier else None}
        (refs if meta.get("kind") in REFERENCE_KINDS else rows).append(rec)
        turf, turf_ids = home_turf(info["name"], cont)
        held = metrics(cases, ans, [i for i in ids if i not in turf_ids]) if turf == "partial" else m
        by_name[info["name"]] = {"right": m["right"], "n": m["n"], "accuracy": m["accuracy"],
                                 "kind": meta.get("kind", "synid"), "meta": meta, "home": turf,
                                 "held_accuracy": None if turf == "full" else held["accuracy"], "held_n": held["n"]}
        infos.append(info)
    rows.sort(key=lambda r: (-(r["m"]["accuracy"] or 0), -(r["m"]["precision"] or 0), r["name"]))

    def contaminated(name: str) -> str | None:
        return next((v["why"] for k, v in cont.items() if name.startswith(k)), None)
    refs.sort(key=lambda r: (r["meta"].get("kind") != "ground-truth", r["name"]))

    def line(rank, r):
        m, o = r["m"], r["m"]["outcomes"]
        w = f" | {pct(m['weighted']['accuracy'])}" if has_weights else ""
        w += f" | {r['all']['right']}/{r['all']['n']} ({pct(r['all']['accuracy'])})" if head_tier else ""
        dag = " †" if contaminated(r["name"]) else ""
        return (f"| {rank} | {r['name']}{' (baseline)' if r['baseline'] else ''}{dag} | {r['info']['kind']} | "
                f"**{m['right']}/{m['n']}** ({pct(m['accuracy'])}) [{pct(m['ci'][0])}, {pct(m['ci'][1])}]{w} | "
                f"{pct(m['precision'])} | {o.get('text', 0)} | {o.get('undecided', 0) + o.get('none', 0)} | "
                f"{o.get('wrong', 0)} | " + " | ".join(f"{r['tags'][t]}/{len(tags[t])}" for t in tag_names) + " |")

    head = ("| # | entry | kind | right (accuracy) [95 % CI]" + (f", {head_tier} tier" if head_tier else "")
            + (" | weighted to the population" if has_weights else "") + (" | all tiers" if head_tier else "")
            + " | precision of language answers | `Text` on code | no answer / undecided | wrong language | "
            + " | ".join(f"`{t}`" for t in tag_names) + " |")
    sep = ("|---:|---|---|---:|" + ("---:|" if has_weights else "") + ("---:|" if head_tier else "")
           + "---:|---:|---:|---:|" + "---:|" * len(tag_names))
    hist = " · [history of Synid versions](HISTORY.md)" if (bench / "HISTORY.md").exists() else ""
    out = [f"# Leaderboard — {bench.name}", "",
           f"Generated by `python3 tools/leaderboard.py` · benchmark `{version}`, {len(every)} cases "
           f"([README](README.md){hist}). Ranked by accuracy"
           + (f" on the {len(ids)} cases of the *{head_tier}* tier (the other tiers' labels are less sure: see the "
              "README; *all tiers* counts every case)" if head_tier else "") + ", then precision of "
           "language answers. Tag columns: right / cases carrying that tag, over all tiers (see the README)"
           + ("; *weighted to the population* re-weights the stratified draw to the population it was drawn from"
              if has_weights else "") + ".", "", *card_lines(card), *how_to_read({bench.name: card} if card else {}),
           "", head, sep]
    out += [line(i, r) for i, r in enumerate(rows, 1)]
    marked = sorted({k: v["why"] + ("" if v["cases"] is None else f" ({len(v['cases'])} cases)")
                     for r in rows for k, v in cont.items() if r["name"].startswith(k)}.items())
    if marked:
        out += ["", "† Home turf — built, trained or tuned on (part of) this benchmark: the score is partly accuracy on "
                "the entry's own data (read the tag columns); where only some cases are, the overall leaderboard "
                "counts the entry on the others: " + "; ".join(f"*{k}*: {v}" for k, v in marked) + "."]
    if refs:
        out += ["", "## References (not ranked)", "",
                "The ground truth, and the LLM judges whose agreement with it backs the benchmark's labels — "
                "neither is independent of the ground truth.", "", head, sep]
        out += [line("–", r) for r in refs]
    missing = {n: m for n, m in (elsewhere or {}).items() if n not in by_name}
    if missing:
        prog_p = bench / "in_progress.json"
        prog = json.loads(prog_p.read_text(encoding="utf-8")) if prog_p.exists() else {}
        out += ["", "## Not run on this benchmark", "",
                "Entries of other benchmarks, and why they are not here.", "", "| entry | kind | why |", "|---|---|---|"]
        for n, m in sorted(missing.items(), key=lambda kv: (KIND.get(kv[1].get("kind", "synid"), ""), kv[0])):
            why = not_applicable(m, card) or m.get("scope") or prog.get(n) or "not run yet"
            out.append(f"| {n} | {KIND.get(m.get('kind', 'synid'), m.get('kind'))} | {why} |")
    out += ["", "## Entries", ""] + info_table([r["info"] for r in rows + refs])
    return "\n".join(out) + "\n", by_name, [r["info"] for r in rows + refs]


def kendall_tau(xs: list[float], ys: list[float]) -> float | None:
    """Kendall's τ-b between two lists of scores of the same entries."""
    c = d = tx = ty = 0
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            a = (xs[i] > xs[j]) - (xs[i] < xs[j])
            b = (ys[i] > ys[j]) - (ys[i] < ys[j])
            if a == 0 and b == 0:
                continue
            if a == 0:
                tx += 1
            elif b == 0:
                ty += 1
            elif a == b:
                c += 1
            else:
                d += 1
    den = ((c + d + tx) * (c + d + ty)) ** 0.5
    return (c - d) / den if den else None


def benchmarks_table(benches: list[Path], cards: dict[str, dict], conts: dict[str, dict]) -> list[str]:
    out = ["| benchmark | cases | languages | unit | file names | labels | sampling | home turf (†) | strengths | "
           "weaknesses |", "|---|---:|---:|---|---|---|---|---|---|---|"]
    for b in benches:
        c = cards.get(b.name, {})
        turf = ", ".join(sorted(conts.get(b.name, {}))) or "—"
        out.append(f"| [{b.name}](benchmarks/{b.name}/README.md) | {c.get('cases', len(read_cases(b)))} | "
                   f"{c.get('languages', '?')} | {c.get('unit', '?')} | {c.get('names', '?')} | {c.get('labels', '?')} | "
                   f"{c.get('sampling', '?')} | {turf} | {'; '.join(c.get('strengths', [])) or '—'} | "
                   f"{'; '.join(c.get('weaknesses', [])) or '—'} |")
    return out


def main() -> int:
    benches = sorted(p for p in (ROOT / "benchmarks").iterdir() if (p / "cases.csv").exists())
    cards = {b.name: read_card(b) for b in benches}
    conts = {b.name: read_contamination(b) for b in benches}
    per_bench: dict[str, dict[str, dict]] = {}
    all_infos: dict[str, dict] = {}
    metas = {b.name: {entry_name(m): m for m, _, _ in load_runs(b)} for b in benches}
    for b in benches:
        elsewhere = {n: m for o, d in metas.items() if o != b.name for n, m in d.items()}
        text, by_name, infos = bench_board(b, cards, elsewhere)
        (b / "LEADERBOARD.md").write_text(text, encoding="utf-8")
        per_bench[b.name] = by_name
        for i in infos:
            all_infos.setdefault(i["name"], i)
        print(f"{b.name}: {len(by_name)} entries → {(b / 'LEADERBOARD.md').relative_to(ROOT)}")
    bnames = [b.name for b in benches]

    def home(name: str, b: str) -> bool:
        """The whole benchmark is the entry's home turf."""
        return per_bench[b].get(name, {}).get("home") == "full"

    rows = []
    for n in sorted({n for d in per_bench.values() for n in d}):
        got = {b: d[n] for b, d in per_bench.items() if n in d}
        meta = next(iter(got.values()))["meta"]
        clean = [b for b in got if not home(n, b)]
        held = sum(got[b]["held_accuracy"] for b in clean) / len(clean) if clean else None
        rows.append({"name": n, "kind": next(iter(got.values()))["kind"], "got": got, "clean": clean, "held": held,
                     "mean": sum(g["accuracy"] for g in got.values()) / len(got),
                     "right": sum(g["right"] for g in got.values()), "n": sum(g["n"] for g in got.values()),
                     "na": [b for b in bnames if b not in got and not_applicable(meta, cards[b])],
                     "older": older_release_of(meta)})
    older = sorted((r for r in rows if r["older"]), key=lambda r: (r["older"], r["name"]))
    general = [r for r in rows if r["kind"] not in REFERENCE_KINDS and not r["older"]]
    # an entry run on fewer than half of the benchmarks is not ranked with the others: its mean rests on
    # one or two benchmarks, often the one it was written for
    quorum = min(len(bnames), max(2, (len(bnames) + 1) // 2))
    ranked = sorted((r for r in general if len(r["got"]) >= quorum and r["clean"]),
                    key=lambda r: (-r["held"], -r["mean"], r["name"]))
    partial = sorted((r for r in general if r not in ranked), key=lambda r: (-r["mean"], r["name"]))
    refs = sorted((r for r in rows if r["kind"] in REFERENCE_KINDS), key=lambda r: (r["kind"] != "ground-truth",
                                                                                 r["name"]))
    head = ("| # | entry | kind | held-out mean | benchmarks (held out / run) | mean, all run | right, all cases | "
            + " | ".join(f"[{b}](benchmarks/{b}/LEADERBOARD.md)" for b in bnames) + " |")
    sep = "|---:|---|---|---:|---:|---:|---:|" + "---:|" * len(bnames)

    def cell(r, b):
        if b in r["got"]:
            g = r["got"][b]
            if g["home"] == "partial":
                return f"{pct(g['accuracy'])} (‡ {pct(g['held_accuracy'])})"
            return pct(g["accuracy"]) + (" †" if g["home"] == "full" else "")
        return "n/a" if b in r["na"] else "—"

    def line(rank, r):
        return (f"| {rank} | {r['name']} | {KIND.get(r['kind'], r['kind'])} | **{pct(r['held'])}** | "
                f"{len(r['clean'])} / {len(r['got'])} | {pct(r['mean'])} | {r['right']}/{r['n']} | "
                + " | ".join(cell(r, b) for b in bnames) + " |")

    out = ["# Leaderboard — all benchmarks", "",
           "Generated by `python3 tools/leaderboard.py`. Each benchmark has its own leaderboard (linked in the header) "
           "with intervals, population weights and failure triggers.", "",
           "## The benchmarks", "",
           "They measure different things: whole files or snippets, with or without a real file name, labelled by "
           "humans, by authors, by a tool's maintainers or by an LLM, curated or sampled from a population — and some "
           "are the training or development data of some entries (their *home turf*, †). Each benchmark's README "
           "details its strengths and weaknesses.", "", *benchmarks_table(benches, cards, conts), "",
           "## Ranking", "",
           "An entry is one system and configuration. Ranked by its **held-out mean**: the mean of its accuracies over "
           "the benchmarks it was run on, leaving out its home turf (†) — a tool is not credited for recognising its "
           f"own training files. Entries run on fewer than {quorum} benchmarks, or only on their home turf, are listed "
           "after the ranking. "
           "*Mean, all run* includes the home turf; *right, all cases* pools the cases of every benchmark run "
           "(dominated by the largest). *n/a*: the tool answers from the file name only and the benchmark has no "
           "file names; *—*: not run.", "", *how_to_read(cards), "", head, sep]
    out += [line(i, r) for i, r in enumerate(ranked, 1)]
    if partial:
        out += ["", f"### Run on fewer than {quorum} benchmarks, or only on their home turf (not ranked)", "", head, sep]
        out += [line("–", r) for r in partial]
    if older:
        out += ["", "### Older releases of other identifiers (not ranked)", "",
                "Kept to show what a tool's releases fixed and broke — non-regression for tools other than Synid: "
                "see [TOOL-HISTORY.md](TOOL-HISTORY.md) (`tools/tool_history.py`).", "", head, sep]
        out += [line("–", r) for r in older]
    turf = sorted({(b, k, v["why"] + ("" if v["cases"] is None else f" ({len(v['cases'])} cases)"))
                   for b in bnames for k, v in conts.get(b, {}).items()})
    if turf:
        out += ["", "† The benchmark is the entry's home turf: left out of its held-out mean. ‡ Only some cases are "
                "(their count below): the held-out mean counts the entry's accuracy on the other cases, shown in "
                "brackets. Home turf: " + "; ".join(f"*{k}* on {b}: {v}" for b, k, v in turf) + "."]

    # do the benchmarks agree on the order of the entries?
    acc = {r["name"]: {b: g["held_accuracy"] for b, g in r["got"].items() if g["held_accuracy"] is not None}
           for r in ranked}
    pairs = []
    for i, b1 in enumerate(bnames):
        for b2 in bnames[i + 1:]:
            common = [n for n, a in acc.items() if b1 in a and b2 in a and not home(n, b1) and not home(n, b2)]
            if len(common) >= 6:
                tau = kendall_tau([acc[n][b1] for n in common], [acc[n][b2] for n in common])
                pairs.append((b1, b2, tau, len(common)))
    if pairs:
        out += ["", "## Do the benchmarks agree?", "",
                "Kendall's τ between the orders two benchmarks give to the ranked entries run on both, home-turf "
                "entries left out (1: the same order; 0: unrelated; negative: reversed). Low agreement means a single "
                "benchmark's ranking does not carry over to another kind of file.", "",
                "| | " + " | ".join(bnames[1:]) + " |", "|---|" + "---:|" * (len(bnames) - 1)]
        for b1 in bnames[:-1]:
            cells = []
            for b2 in bnames[1:]:
                p = next((x for x in pairs if x[0] == b1 and x[1] == b2), None)
                cells.append(f"{p[2]:+.2f} ({p[3]})" if p and p[2] is not None else "")
            out.append(f"| {b1} | " + " | ".join(cells) + " |")
        out += ["", "Leaders and home turf — the three best entries on each benchmark (all entries, home turf "
                "included), and where the benchmark's own home-turf entries rank on it:", "",
                "| benchmark | 1st | 2nd | 3rd | home-turf entries: rank on this benchmark (of N) |",
                "|---|---|---|---|---|"]
        for b in bnames:
            order = sorted(((n, g["accuracy"]) for n, g in per_bench[b].items()
                            if g["kind"] not in REFERENCE_KINDS), key=lambda x: (-x[1], x[0]))
            mark = {"full": " †", "partial": " ‡"}
            top = [f"{n}{mark.get(per_bench[b][n]['home'], '')} ({pct(a)})" for n, a in order[:3]] + [""] * 3
            mine = [f"{n}: {i}" for i, (n, _) in enumerate(order, 1) if home(n, b)]
            out.append(f"| {b} | " + " | ".join(top[:3]) + f" | {'; '.join(mine[:6]) or '—'}"
                       + (f" … ({len(mine)} entries)" if len(mine) > 6 else "") + f" (of {len(order)}) |")
    if refs:
        out += ["", "## References (not ranked)", "", head, sep] + [line("–", r) for r in refs]
    out += ["", "## Entries", ""] + info_table([all_infos[r["name"]] for r in ranked + partial + older + refs])
    (ROOT / "LEADERBOARD.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"overall: {len(ranked)} ranked entries, {len(partial)} not ranked, {len(refs)} references → LEADERBOARD.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
