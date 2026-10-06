#!/usr/bin/env python3
"""Snapshot PL-ultimate-llm's extension → language mapping into tools/data/pl_candidates.json,
for tools/jev_cascade.py.

    PL_ULTIMATE_LLM=~/SANDBOX/PL-ultimate-llm python3 tools/export_pl_candidates.py

From PL-ultimate-llm's data/derived/pl_taxonomy (github.com/acherm/PL-ultimate-llm):
- ext_claim.csv: which languages claim an extension (Linguist, Pygments, Wikidata, Wikipedia,
  manual reviews), without the claims the encyclopedia marks deprecated or disputed;
- ext_evidence.csv: which languages the extension studies found in Software Heritage under an
  extension (e.g. Magma, MUMPS and C under .m) — observed, whether claimed or not;
- Linguist's file names (data/raw/linguist_languages.yml) for files known by their whole name.
A language is named by its Linguist name when it has one, by its canonical name otherwise.
Records that are the same language under a generic qualifier — "APL (programming language)"
next to Linguist's "APL" — are merged into one, as PL-ultimate-llm's identity layer does
(rule "generic-qualifier"): the qualifier is dropped and the name compared, case- and
punctuation-insensitively, with Linguist's names and aliases, then with the other records.
The fallback list is every language with an extension claim or a Linguist name; with
PL_FALLBACK_SOURCES (comma-separated sources of pl.csv's membership flags, e.g.
linguist,pygments,rosettacode,wikipedia,wikidata,hyperpolyglot), also every language one of those
sources lists — a wider fallback, merged with the same identity rule. The Esolang wiki and PLDB are
best left out: thousands of toy or one-off languages, each one more rival in the knockout.

    PL_FALLBACK_SOURCES=linguist,pygments,rosettacode,wikipedia,wikidata,hyperpolyglot \
    PL_CANDIDATES_OUT=tools/data/pl_candidates_wide.json python3 tools/export_pl_candidates.py
"""

from __future__ import annotations

import csv
import json
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PL = Path(os.environ.get("PL_ULTIMATE_LLM", HERE.parents[1] / "PL-ultimate-llm")).expanduser()
T = PL / "data" / "derived" / "pl_taxonomy"


def main() -> int:
    commit = subprocess.run(["git", "-C", str(PL), "log", "-1", "--format=%h %cs", "--", "data/derived/pl_taxonomy"],
                            capture_output=True, text=True).stdout.strip()
    pl = {r["pl_id"]: r for r in csv.DictReader(open(T / "pl.csv", encoding="utf-8"))}
    ling = yaml.safe_load(open(PL / "data" / "raw" / "linguist_languages.yml", encoding="utf-8"))
    aliases = defaultdict(list)
    for r in csv.DictReader(open(T / "pl_alias.csv", encoding="utf-8")):
        if r["alias"] not in aliases[r["pl_id"]]:
            aliases[r["pl_id"]].append(r["alias"])
    by_ext: dict[str, set[str]] = defaultdict(set)
    exts: dict[str, set[str]] = defaultdict(set)
    observed: dict[str, set[str]] = defaultdict(set)
    for c in csv.DictReader(open(T / "ext_claim.csv", encoding="utf-8")):
        if c["strength"] in ("deprecated", "disputed"):
            continue
        by_ext[c["ext"].lower()].add(c["pl_id"])
        exts[c["pl_id"]].add(c["ext"])
    for e in csv.DictReader(open(T / "ext_evidence.csv", encoding="utf-8")):
        if e["pl_id"]:
            by_ext[e["ext"].lower()].add(e["pl_id"])
            observed[e["ext"].lower()].add(e["pl_id"])
    by_lkey = {r["linguist_key"]: pid for pid, r in pl.items() if r["linguist_key"]}
    by_filename: dict[str, set[str]] = defaultdict(set)
    for name, d in ling.items():
        for f in d.get("filenames") or []:
            if name in by_lkey:
                by_filename[f].add(by_lkey[name])
    # identity: a record that is a Linguist language (or another record) under a generic qualifier
    key = lambda n: re.sub(r"[^a-z0-9+#*-]", "", n.lower())  # noqa: E731 — keeps "-": C-- is not C
    strip = lambda n: re.sub(r"\s*\((?:[^()]*\b(?:programming|language|software|computing)\b[^()]*)\)\s*$", "", n)  # noqa: E731
    canon: dict[str, str] = {}
    for lk, pid in by_lkey.items():
        for n in [lk, *(ling.get(lk, {}).get("aliases") or [])]:
            canon.setdefault(key(n), pid)
    same: dict[str, str] = {}
    for pid in sorted(set().union(*by_ext.values())):
        if pl.get(pid, {}).get("linguist_key"):
            continue
        k = key(strip(pl.get(pid, {}).get("canonical_name") or pid))
        if k in canon:
            same[pid] = canon[k]
        else:
            canon[k] = pid
    for d in (by_ext, observed):
        for e in d:
            d[e] = {same.get(p, p) for p in d[e]}
    for pid, to in same.items():
        exts[to] |= exts.pop(pid, set())
    keep = set().union(*by_ext.values(), *by_filename.values(), by_lkey.values())
    sources = [x for x in os.environ.get("PL_FALLBACK_SOURCES", "").split(",") if x]
    wide = set()
    for pid, r in sorted(pl.items()):
        if pid in keep or not any(r.get(f"in_{x}") == "yes" for x in sources):
            continue
        k = key(strip(r.get("canonical_name") or pid))
        if k in canon:  # the same language as one already in the list
            same.setdefault(pid, canon[k])
            continue
        canon[k] = pid
        wide.add(pid)
    keep |= wide
    langs = {}
    for pid in sorted(keep):
        r = pl.get(pid, {})
        lk = r.get("linguist_key") or ""
        al = [a for a in (ling.get(lk, {}).get("aliases") or []) + aliases.get(pid, []) if a]
        langs[pid] = {"name": lk or r.get("canonical_name") or pid, "linguist": lk or None,
                      "type": ling.get(lk, {}).get("type") if lk else None,
                      "aliases": list(dict.fromkeys(al))[:6], "extensions": sorted(exts.get(pid, ()))[:8]}
    out = {"source": f"PL-ultimate-llm {commit}, data/derived/pl_taxonomy (ext_claim minus deprecated/disputed, "
                     "ext_evidence) and Linguist's file names",
           "languages": langs,
           "by_ext": {e: sorted(v) for e, v in sorted(by_ext.items())},
           "observed_by_ext": {e: sorted(v) for e, v in sorted(observed.items())},
           "by_filename": {f: sorted(v) for f, v in sorted(by_filename.items())},
           "fallback": sorted(keep),
           "merged": dict(sorted(same.items()))}
    if sources:
        out["fallback_name"] = (f"{len(keep):,} languages (with an extension or listed by "
                                + ", ".join(sources) + ")")
    dest = Path(os.environ.get("PL_CANDIDATES_OUT", HERE / "data" / "pl_candidates.json"))
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(f"{len(langs)} languages ({len(same)} qualifier duplicates merged), {len(by_ext)} extensions, "
          f"{len(by_filename)} file names; "
          f"fallback {len(out['fallback'])} → {dest} ({out['source']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
