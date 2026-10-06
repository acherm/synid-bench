#!/usr/bin/env python3
"""Jev across the benchmarks: where it fails and why, and where it does better than the other
identifiers — Synid first → JEV.md.

    python3 tools/jev_report.py

The entry studied is Jev over Linguist's 836 languages (`jev-linguist836-filename`, with the file name;
`jev-linguist836`, content only), run on every benchmark with the same protocol (tools/jev_linguist.py): a
knockout — the 836 names shuffled with a fixed seed, 4 groups of ~209 each with "none of these", then a
final among the groups' winners. The groups are rebuilt here from the same seed, so each failure can be
traced to the round where the right language was lost:

- *not in the list*: no accepted name of the case is one of Linguist's 836 languages (or their aliases);
- *abstained*: every group answered "none of these";
- *lost in its group*: the right language's group sent another language to the final, or none;
- *lost in the final*: the right language was a finalist, and another one won.

A wrong answer that shares Linguist's `group` with the expected language (a dialect, a parent) is counted
apart as a *neighbour*. Cases are a benchmark's headline cases (the gold tier where the card names one).
The comparison uses Synid 48c3c45 as shipped and with its Pygments step off, GitHub Linguist 9.7.0, the
candidates + Jev cascade, and every identifier that does not call an LLM (its *oracle*: right when one of
them is). Run after the entries exist; reads the raw decisions in <bench>/entries/raw/.
"""

from __future__ import annotations

import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from jev_linguist import GROUPS, SEED  # noqa: E402
from leaderboard import entry_name, home_turf, load_runs, older_release_of, read_card, read_contamination  # noqa: E402
from score import name_key, outcome, pct, read_cases  # noqa: E402

LANGS = HERE / "data" / "linguist_languages_76f88c6.json"
PLU = Path("/Users/mathieuacher/SANDBOX/PL-ultimate-llm")  # PL-ultimate-llm checkout (its taxonomy)
LINGUIST_YML = PLU / "data" / "raw" / "linguist_languages.yml"
TAXONOMY = PLU / "data" / "derived" / "pl_taxonomy"
JEV, JEV_CO = "jev-linguist836-filename", "jev-linguist836"
SYNID, SYNID_OFF, LINGUIST, CASCADE = "48c3c45-default", "48c3c45-no-pygmentsheuristics", "ext-linguist", "jev-cascade"
WIDE = "jev-cascade-wide"  # the cascade with a fallback over 2,140 languages (tools/data/pl_candidates_wide.json)
CAUSES = {"not-in-list": "not in Linguist's list", "abstained": "abstained (every group: none)",
          "lost-group-other": "lost in its group to another language", "lost-group-none": "lost in its group to \"none\"",
          "lost-final": "lost in the final"}
TAGS = ["ambiguous-ext", "misleading-ext", "invented-ext", "no-ext", "human-overrode-linguist", "unseen",
        "seen-in-training", "in-linguist", "not-in-linguist", "tiny", "by-filename", "judge-rules-disagree"]


def languages() -> tuple[dict[str, str], list[list[str]], dict[str, str]]:
    """name key (of a name or an alias) → Linguist name; the knockout's groups; name → Linguist `group`."""
    d = json.loads(LANGS.read_text(encoding="utf-8"))["languages"]
    key = {name_key(x): l["name"] for l in d for x in [l["name"], *l["aliases"]]}
    names = sorted(l["name"] for l in d)
    random.Random(SEED).shuffle(names)
    parent = {}
    if LINGUIST_YML.exists():
        import yaml
        parent = {n: v["group"] for n, v in yaml.safe_load(LINGUIST_YML.read_text(encoding="utf-8")).items()
                  if v.get("group")}
    return key, [names[i::GROUPS] for i in range(GROUPS)], parent


def raw(bench: Path, label: str) -> dict[str, dict]:
    p = bench / "entries" / "raw" / f"{label}.jsonl"
    return {d["case_id"]: d for d in map(json.loads, p.read_text(encoding="utf-8").splitlines())} if p.exists() else {}


def auroc(pos: list[float], neg: list[float]) -> float | None:
    """Probability that a right answer has a higher confidence than a wrong one (ties count half)."""
    if not pos or not neg:
        return None
    vals = sorted([(v, 1) for v in pos] + [(v, 0) for v in neg])
    rank_sum, i = 0.0, 0
    while i < len(vals):
        j = i
        while j < len(vals) and vals[j][0] == vals[i][0]:
            j += 1
        rank_sum += (i + j + 1) / 2 * sum(1 for k in range(i, j) if vals[k][1])
        i = j
    return (rank_sum - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))


def confidence(d: dict, cascade: bool) -> float | None:
    """The probability of the answer given by the question(s) that decided it, as recorded: for the cascade, the
    deciding question's top 1 (decisions among candidates only for runs before 2026-10-04, whose top 5 could be
    stale); for the knockout, the winner's probability in its group times its probability in the final, or the
    final's top 1 alone for runs that did not keep the groups' probabilities."""
    if cascade:
        if d.get("stage") != "candidates" and "candidates_top5" not in d:
            return None
        t = d.get("top5") or []
        return t[0][1] if t else None
    final = d.get("final_top5") or []
    groups = d.get("groups_top5")
    if groups:
        win = next((t[0][1] for t in groups if t and t[0][0] == d.get("choice")), None)
        if win is None:
            return None
        return win * (final[0][1] if final else 1.0)
    return final[0][1] if final else None


def taxonomy_names() -> tuple[set[str], dict[str, int]]:
    """Name keys of every language PL-ultimate-llm knows (names, aliases, each source's name), and the size of
    the lists one could ask Jev to choose from."""
    import csv
    if not (TAXONOMY / "pl.csv").exists():
        return set(), {}
    with (TAXONOMY / "pl.csv").open(encoding="utf-8") as f:
        pl = list(csv.DictReader(f))
    keys = {name_key(r[k]) for r in pl for k in ("canonical_name", "linguist_key", "rosettacode_name",
                                                  "hyperpolyglot_name") if r[k]}
    with (TAXONOMY / "pl_alias.csv").open(encoding="utf-8") as f:
        keys |= {name_key(r["alias"]) for r in csv.DictReader(f)}
    with (TAXONOMY / "ext_claim.csv").open(encoding="utf-8") as f:
        with_ext = {r["pl_id"] for r in csv.DictReader(f)}
    has = lambda r, *ks: any(r.get(f"in_{k}") == "yes" for k in ks)  # noqa: E731
    major = ("linguist", "pygments", "rosettacode", "wikipedia", "wikidata", "hyperpolyglot")
    sizes = {"Linguist (Jev's list)": sum(has(r, "linguist") for r in pl),
             "with a known extension (the cascade's fallback)": sum(r["pl_id"] in with_ext for r in pl),
             "Linguist ∪ Pygments ∪ Rosetta Code ∪ Wikipedia ∪ Wikidata ∪ Hyperpolyglot": sum(has(r, *major) for r in pl),
             "… ∪ PLDB": sum(has(r, *major, "pldb") for r in pl),
             "everything (… ∪ Esolang wiki)": len(pl)}
    return keys, sizes


def main() -> int:
    key, groups, parent = languages()
    group_of = {n: i for i, g in enumerate(groups) for n in g}
    benches = sorted(p for p in (ROOT / "benchmarks").iterdir() if (p / "cases.csv").exists())
    per_bench, causes, confusions = [], Counter(), defaultdict(Counter)
    cause_bench = defaultdict(Counter)
    by_tag = defaultdict(lambda: Counter())
    by_synid = defaultdict(Counter)
    unique_wins, synid_only = Counter(), Counter()
    synid_only_cause = Counter()
    neighbours = 0
    cost = {}
    unc = defaultdict(list)
    tax, list_sizes = taxonomy_names()
    outside = Counter()
    for b in benches:
        cases = read_cases(b)
        card = read_card(b)
        tier = card.get("headline_tier")
        ids = [i for i in cases if not tier or cases[i].get("tier") == tier]
        runs = {m.get("label"): (m, a) for m, a, _ in load_runs(b)}
        if JEV not in runs:
            continue
        ans = {k: runs[k][1] for k in (JEV, JEV_CO, SYNID, SYNID_OFF, LINGUIST, CASCADE, WIDE) if k in runs}
        others = [a for lab, (m, a) in runs.items() if m.get("kind") in ("synid", "other-identifier")
                  and not older_release_of(m) and lab != "linguist" and lab != "pygments"]
        right = {k: {i for i in ids if outcome(cases[i], a.get(i)) == "right"} for k, a in ans.items()}
        oracle = {i for i in ids if any(outcome(cases[i], a.get(i)) == "right" for a in others)}
        best_tool = max(((entry_name(m), sum(outcome(cases[i], a.get(i)) == "right" for i in ids))
                         for lab, (m, a) in runs.items() if m.get("kind") in ("synid", "other-identifier")
                         and not older_release_of(m) and lab not in ("linguist", "pygments")), key=lambda x: x[1])
        rj = raw(b, JEV) or raw(b, JEV_CO)
        for lab, src, casc in ((JEV, rj, False), (CASCADE, raw(b, CASCADE) or raw(b, "jev-cascade-content-only"), True),
                               (WIDE, raw(b, WIDE) or raw(b, "jev-cascade-wide-content-only"), True)):
            if lab not in ans:
                continue
            for i in ids:
                d = src.get(i)
                v = confidence(d, casc) if d else None
                if v is not None:
                    unc[lab].append((v, outcome(cases[i], ans[lab].get(i)) == "right",
                                     "not-in-linguist" in cases[i].get("tags", "").split(";")))
        cost[b.name] = sum(float(d.get("cost") or 0) for lab in (JEV, JEV_CO) for d in raw(b, lab).values())
        bc = Counter()
        for i in ids:
            if i in right[JEV]:
                continue
            exp = {key[k] for x in cases[i]["accept"].split(";") if x and (k := name_key(x)) in key}
            d = rj.get(i, {})
            winners = d.get("group_winners") or []
            choice = d.get("choice")
            if not exp:
                c = "not-in-list"
                outside["n"] += 1
                outside["in PL-ultimate-llm"] += any(name_key(x) in tax for x in cases[i]["accept"].split(";") if x)
                if CASCADE in ans:
                    outside["cascade right"] += outcome(cases[i], ans[CASCADE].get(i)) == "right"
                if WIDE in ans:
                    outside["wide right"] += outcome(cases[i], ans[WIDE].get(i)) == "right"
            elif not winners:
                c = "abstained"
            elif exp & set(winners):
                c = "lost-final"
            else:
                g = group_of[sorted(exp)[0]]
                c = "lost-group-other" if any(group_of.get(w) == g for w in winners) else "lost-group-none"
            bc[c] += 1
            causes[c] += 1
            cause_bench[c][b.name] += 1
            exp_name = cases[i]["expected"]
            confusions[c][(exp_name, choice or "—")] += 1
            if choice and exp and (parent.get(choice) in exp or any(parent.get(e) == choice for e in exp)
                                   or (parent.get(choice) and any(parent.get(choice) == parent.get(e) for e in exp))):
                neighbours += 1
        for t in TAGS:
            tids = [i for i in ids if t in cases[i].get("tags", "").split(";")]
            if not tids:
                continue
            by_tag[t]["n"] += len(tids)
            for k in (JEV, JEV_CO, SYNID, SYNID_OFF, LINGUIST):
                if k in right:
                    by_tag[t][k] += len(right[k] & set(tids))
        if SYNID in ans:
            for i in ids:
                o = outcome(cases[i], ans[SYNID].get(i))
                by_synid[o]["n"] += 1
                by_synid[o]["jev"] += i in right[JEV]
            for i in right[SYNID] - right[JEV]:
                synid_only[cases[i]["expected"]] += 1
                d = rj.get(i, {})
                exp = {key[k] for x in cases[i]["accept"].split(";") if x and (k := name_key(x)) in key}
                synid_only_cause["outside" if not exp else "inside"] += 1
        for i in (right[JEV] - oracle):
            unique_wins[cases[i]["expected"]] += 1
        # two ways of combining Synid and Jev: Synid first (its answer when it names exactly one language, not
        # Text; Jev's otherwise), and Jev first (Synid's answer when Jev gives none)
        combo, sent, fallback = 0, 0, 0
        if SYNID in ans:
            for i in ids:
                s = ans[SYNID].get(i)
                if s and len(s) == 1 and s[0] != "Text":
                    combo += outcome(cases[i], s) == "right"
                else:
                    sent += 1
                    combo += i in right[JEV]
                fallback += outcome(cases[i], ans[JEV].get(i) or s) == "right"
        per_bench.append({"bench": b.name, "n": len(ids), "jev": len(right[JEV]), "jev_co": len(right.get(JEV_CO, ())),
                          "cascade": len(right.get(CASCADE, ())), "wide": len(right.get(WIDE, ())),
                          "synid": len(right.get(SYNID, ())),
                          "synid_off": len(right.get(SYNID_OFF, ())), "linguist": len(right.get(LINGUIST, ())),
                          "best": best_tool, "oracle": len(oracle), "jev_only": len(right[JEV] - right.get(SYNID, set())),
                          "synid_only": len(right.get(SYNID, set()) - right[JEV]),
                          "unique": len(right[JEV] - oracle), "missed": len(oracle - right[JEV]),
                          "combo": combo, "sent": sent, "fallback": fallback, "causes": bc, "tier": tier,
                          "best_home": home_turf(best_tool[0], read_contamination(b))[0] is not None})

    def p(k, n):
        return f"{k}/{n} ({pct(k / n if n else None)})"

    out = ["# Jev across the benchmarks — where it fails, where it shines", "",
           "Generated by `python3 tools/jev_report.py` from the stored runs. **Jev** is TypeSafe's lightweight "
           "decision model (`typesafe/jev-1.13`, OpenRouter), asked which of GitHub Linguist's 836 languages "
           "(76f88c6) a file is written in — a knockout over 4 groups of ~209 names, then a final "
           "([tools/jev_linguist.py](tools/jev_linguist.py)). Main entry: with the file name; *content only* in "
           "brackets where it matters. Cases: each benchmark's headline cases (bench-smola: the 1,107 human-checked "
           "files). Synid is 48c3c45 as shipped. See [LEADERBOARD.md](LEADERBOARD.md) for every entry.", "",
           "## At a glance", "",
           "| benchmark | cases | Jev | Jev, content only | cascade | cascade, wide fallback | Synid | Synid, Pygments "
           "step off | Linguist 9.7.0 | best identifier without an LLM | any identifier without an LLM | Jev right, "
           "Synid wrong | Synid right, Jev wrong |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|"]
    T = Counter()
    for r in per_bench:
        n = r["n"]
        out.append(f"| {r['bench']} | {n} | **{pct(r['jev'] / n)}** | {pct(r['jev_co'] / n)} | {pct(r['cascade'] / n)} | "
                   f"{pct(r['wide'] / n) if r['wide'] else '—'} | "
                   f"{pct(r['synid'] / n)} | {pct(r['synid_off'] / n)} | {pct(r['linguist'] / n)} | "
                   f"{r['best'][0]}{' †' if r['best_home'] else ''} {pct(r['best'][1] / n)} | {pct(r['oracle'] / n)} | "
                   f"{r['jev_only']} | {r['synid_only']} |")
        for k in ("n", "jev", "jev_co", "cascade", "wide", "synid", "synid_off", "linguist", "oracle", "jev_only", "synid_only",
                  "unique", "missed", "combo", "sent", "fallback"):
            T[k] += r[k]
    n = T["n"]
    out.append(f"| **all** | {n} | **{pct(T['jev'] / n)}** | {pct(T['jev_co'] / n)} | {pct(T['cascade'] / n)} | "
               f"{pct(T['wide'] / n) if T['wide'] else '—'} | "
               f"{pct(T['synid'] / n)} | {pct(T['synid_off'] / n)} | {pct(T['linguist'] / n)} | — | "
               f"{pct(T['oracle'] / n)} | {T['jev_only']} | {T['synid_only']} |")
    out += ["", "† the benchmark is that tool's home turf (built, trained or tuned on it).", "",
            f"Pooled over the {n} cases of the {len(per_bench)} benchmarks (each benchmark weighs its size; "
            "the leaderboard's held-out mean weighs benchmarks equally). *Any identifier without an LLM* is "
            "right when at least one of the 24 other identifiers or Synid's configurations is — a ceiling no single "
            "tool reaches.", ""]

    tg = lambda t, k: pct(by_tag[t][k] / by_tag[t]["n"]) if by_tag.get(t) else "—"  # noqa: E731
    pb = {r["bench"]: r for r in per_bench}
    fails = n - T["jev"]
    ko = causes["lost-group-other"] + causes["lost-group-none"] + causes["lost-final"]
    fsf = pb.get("bench-fsf")
    out += ["## Key points", "",
            f"- **Overall**: Jev is right on {pct(T['jev'] / n)} of the cases, Synid on {pct(T['synid'] / n)}, Linguist on "
            f"{pct(T['linguist'] / n)}; all the identifiers without an LLM taken together (right when any one is) on "
            f"{pct(T['oracle'] / n)}.",
            f"- **Where it shines**: files a human corrected Linguist on (`human-overrode-linguist`: "
            f"{tg('human-overrode-linguist', JEV)}, Synid {tg('human-overrode-linguist', SYNID)}); files Synid's "
            f"classifier was not trained on (bench-linguist's `unseen`: {tg('unseen', JEV)}, Synid "
            f"{tg('unseen', SYNID)}); tiny files (`tiny`: "
            f"{tg('tiny', JEV)}, Synid {tg('tiny', SYNID)}); files without a name (bench-hljs "
            f"{pct(pb['bench-hljs']['jev'] / pb['bench-hljs']['n'])}, bench-rouge "
            f"{pct(pb['bench-rouge']['jev'] / pb['bench-rouge']['n'])}; Synid "
            f"{pct(pb['bench-hljs']['synid'] / pb['bench-hljs']['n'])} and "
            f"{pct(pb['bench-rouge']['synid'] / pb['bench-rouge']['n'])}).",
            f"- **Where it fails**: the label set first — {causes['not-in-list']} of its {fails} misses are languages "
            f"outside Linguist's 836 (`not-in-linguist`: {tg('not-in-linguist', JEV)}, Synid "
            f"{tg('not-in-linguist', SYNID)}); then the knockout ({ko} lost in a group or in the final, "
            f"{causes['abstained']} with no answer)"
            + (f"; and a name can mislead it — on bench-fsf it is right on {pct(fsf['jev'] / fsf['n'])} with the file "
               f"name and {pct(fsf['jev_co'] / fsf['n'])} without" if fsf and fsf["jev_co"] > fsf["jev"] else "") + ".",
            f"- **Against Synid**: {T['jev_only']} cases Jev right and Synid wrong, {T['synid_only']} the reverse; "
            f"where Synid answers `Text` on code, Jev is right on {pct(by_synid['text']['jev'] / by_synid['text']['n'])}.",
            ""]
    out += ["## Where Jev shines", "",
            f"**Against Synid, case by case.** Jev is right where Synid is wrong on {T['jev_only']} of the {n} "
            f"cases, and the reverse on {T['synid_only']}. By what Synid answered:", "",
            "| Synid's outcome | cases | Jev right |", "|---|---:|---:|"]
    label = {"right": "right", "text": "`Text` on code", "undecided": "several languages (undecided)",
             "none": "no answer", "wrong": "a wrong language"}
    for o in ("right", "wrong", "text", "undecided", "none"):
        if by_synid[o]["n"]:
            out.append(f"| {label[o]} | {by_synid[o]['n']} | {p(by_synid[o]['jev'], by_synid[o]['n'])} |")
    out += ["", "**By kind of case** (tags, pooled over the benchmarks that carry them):", "",
            "| tag | cases | Jev | Jev, content only | Synid | Synid, Pygments step off | Linguist |",
            "|---|---:|---:|---:|---:|---:|---:|"]
    for t in TAGS:
        c = by_tag.get(t)
        if not c:
            continue
        out.append(f"| `{t}` | {c['n']} | **{pct(c[JEV] / c['n'])}** | {pct(c[JEV_CO] / c['n'])} | {pct(c[SYNID] / c['n'])} | "
                   f"{pct(c[SYNID_OFF] / c['n'])} | {pct(c[LINGUIST] / c['n'])} |")
    out += ["", f"**Only Jev.** On {T['unique']} cases Jev is right and no identifier without an LLM is; the "
            "languages most involved:", "",
            ", ".join(f"{lang} ({k})" for lang, k in unique_wins.most_common(20)) + ".", "",
            "**Combining Synid and Jev.** Jev alone is hard to beat: Synid adds about one point as a fallback where "
            "Jev gives no answer. Asking Synid first — its answer when it names one language (not `Text`), Jev "
            "otherwise — saves three quarters of the paid calls but keeps Synid's wrong languages:", "",
            "| policy | right | Jev asked on |", "|---|---:|---:|",
            f"| Synid alone | {p(T['synid'], n)} | 0% |",
            f"| Synid first, then Jev | {p(T['combo'], n)} | {pct(T['sent'] / n)} |",
            f"| Jev alone | {p(T['jev'], n)} | 100% |",
            f"| Jev, then Synid where Jev gives no answer | {p(T['fallback'], n)} | 100% |", "",
            "| benchmark | Synid | Synid first, then Jev | files sent to Jev | Jev | Jev, then Synid |",
            "|---|---:|---:|---:|---:|---:|"]
    for r in per_bench:
        out.append(f"| {r['bench']} | {pct(r['synid'] / r['n'])} | {pct(r['combo'] / r['n'])} | "
                   f"{pct(r['sent'] / r['n'])} | {pct(r['jev'] / r['n'])} | {pct(r['fallback'] / r['n'])} |")

    out += ["", "## Where Jev fails", "",
            f"Jev (with the file name) is wrong or silent on {n - T['jev']} of the {n} cases. Where in its knockout the "
            f"right language was lost — {neighbours} of the wrong answers are a neighbour of the expected language in "
            "Linguist's taxonomy (same `group`):", "",
            "| cause | cases | " + " | ".join(r["bench"].replace("bench-", "") for r in per_bench) + " |",
            "|---|---:|" + "---:|" * len(per_bench)]
    for c, title in CAUSES.items():
        out.append(f"| {title} | {causes[c]} | " + " | ".join(str(cause_bench[c][r['bench']] or "") for r in per_bench) + " |")
    out += ["", "- **Not in the list** is the label set, not the model: Rosetta Code's and hello-world's languages that "
            "Linguist does not have (Jev can only answer one of the 836), and labels Linguist splits or names "
            "differently. A list with more languages — PL-ultimate-llm's candidates in the cascade — recovers "
            "part of them.",
            "- **Lost in its group / in the final**: the knockout's cost — a file must win a group of ~209 names "
            "against \"none of these\", then a final against the other groups' winners.", ""]
    for c, title in CAUSES.items():
        if not confusions[c]:
            continue
        out += [f"### {title[0].upper() + title[1:]} — {causes[c]}", "",
                "| expected → answer | cases |", "|---|---:|"]
        out += [f"| {e} → {a} | {k} |" for (e, a), k in confusions[c].most_common(12)]
        out.append("")
    if list_sizes:
        out += ["## A richer list?", "",
                f"Of the {outside['n']} cases Jev loses because their language is not among Linguist's 836, "
                f"{outside['in PL-ultimate-llm']} ({pct(outside['in PL-ultimate-llm'] / outside['n'])}) are languages "
                "PL-ultimate-llm knows (mostly through the Esolang wiki and PLDB); the cascade — whose candidates and "
                f"fallback come from PL-ultimate-llm — gets {outside['cascade right']} of them right"
                + (f", and {outside['wide right']} with its fallback widened to 2,140 languages (Linguist, Pygments, "
                   "Rosetta Code, Wikipedia, Wikidata and Hyperpolyglot's, plus every language with an extension; "
                   "the Esolang wiki and PLDB left out)" if outside["wide right"] else "") + ". A knockout over a "
                "longer list costs one call per group of ≤254 names, and gives the right language more rivals:", "",
                "| list (PL-ultimate-llm) | languages | groups of ≤254 | calls per file |", "|---|---:|---:|---:|"]
        out += [f"| {k} | {v} | {-(-v // 254)} | {-(-v // 254) + 1} |" for k, v in list_sizes.items()]
        out += ["", "A list built from Rosetta Code's or the Esolang wiki's names would also match bench-rosetta's and "
                "bench-hello's labels by construction — a label-set home turf, to be marked as such.", ""]
    out += ["## Uncertainty: does Jev know when it is wrong?", "",
            "The Decisions API returns a probability for every option; the runs keep the top five. The confidence of "
            "an answer is the probability the deciding question gave it (for the knockout: its probability in its "
            "group × in the final; runs made before 2026-10-04 kept only the final's, so there the analysis covers "
            "the files with two finalists or more). *AUROC*: the chance that a right answer is more confident than "
            "a wrong one (0.5: no signal, 1: perfect). Abstaining below a threshold trades coverage for accuracy:", "",
            "| entry | answers with a confidence | right | AUROC | abstain below 0.9: answered → right | wrong answers avoided | wrong answers at ≥ 0.99 | of which the language is outside Linguist's list |",
            "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for lab, title in ((JEV, "Jev, Linguist's 836 languages"), (CASCADE, "Jev cascade"),
                       (WIDE, "Jev cascade, wide fallback (every probability kept)")):
        v = unc.get(lab) or []
        if not v:
            continue
        r = [x for x in v if x[1]]
        w = [x for x in v if not x[1]]
        kept = [x for x in v if x[0] >= 0.9]
        sure_wrong = [x for x in w if x[0] >= 0.99]
        au = auroc([x[0] for x in r], [x[0] for x in w])
        out.append(f"| {title} | {len(v)} | {pct(len(r) / len(v))} | {au:.2f} | {pct(len(kept) / len(v))} → "
                   f"{pct(sum(x[1] for x in kept) / len(kept) if kept else None)} | "
                   f"{pct(1 - sum(1 for x in kept if not x[1]) / len(w) if w else None)} | "
                   f"{pct(len(sure_wrong) / len(w) if w else None)} | {sum(x[2] for x in sure_wrong)} of {len(sure_wrong)} |")
    out += ["", "| entry | confidence | answers | right |", "|---|---|---:|---:|"]
    for lab, title in ((JEV, "Jev, 836 languages"), (CASCADE, "Jev cascade"), (WIDE, "cascade, wide fallback")):
        for lo, hi in ((0, .5), (.5, .7), (.7, .9), (.9, .99), (.99, 1.01)):
            sel = [x for x in unc.get(lab) or [] if lo <= x[0] < hi]
            if sel:
                out.append(f"| {title} | {lo:.2f}–{min(hi, 1):.2f} | {len(sel)} | {pct(sum(x[1] for x in sel) / len(sel))} |")
    out += ["", "Low confidence does flag many failures, but not the confident ones: most wrong answers given with "
            "≥ 0.99 are files whose language was not among the options (outside Linguist's list, or missing from "
            "the extension's candidates) — Jev then picks the nearest option with conviction (OoRexx → REXX, "
            "Dylan.NET → Dylan) — or names our crosswalks do not accept yet (Fan → Fantom, KQL → Kusto). A "
            "probability ranks the options it was given; it cannot say that the right one was missing. That takes a "
            "richer list, or an explicit \"another language\" option.", ""]
    out += ["## Where Synid beats Jev", "",
            f"{T['synid_only']} cases: Synid right, Jev wrong — {synid_only_cause['outside']} of them in "
            "languages outside Linguist's list (Synid knows ~1,100 syntaxes). The expected languages most involved:", "",
            ", ".join(f"{lang} ({k})" for lang, k in synid_only.most_common(20)) + ".", "",
            "## Cost", "",
            "Jev costs about $1 per 1,000 files and per variant (5 calls per file); the cascade about $0.15 per "
            "1,000 when the extension has candidates, $1 when it falls back to the whole list. Synid is local, "
            "free and fast. What these runs cost (both variants):", "",
            "| benchmark | Jev, 836 languages |", "|---|---:|"]
    out += [f"| {b} | ${c:.2f} |" for b, c in cost.items()]
    out.append(f"| **all** | **${sum(cost.values()):.2f}** |")
    (ROOT / "JEV.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(per_bench)} benchmarks, {n} cases → {ROOT / 'JEV.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
