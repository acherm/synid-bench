#!/usr/bin/env python3
"""Build bench-rosetta: Rosetta Code solutions, labelled by the language heading
each contributor filed them under → cases.csv + files/ + labels.csv.

    python3 benchmarks/bench-rosetta/build_cases.py [--cache DIR]

Everything is pinned, so the output is the same on every machine:
- RosettaCodeData (acmeism's dump of rosettacode.org) at ROSETTA_REV:
  Task/<task>/<language>/<task>[-<n>].<ext>, one file per solution; the
  language's own name is in Lang/<language>/00-META.yaml; the extension is the
  one acmeism chose for the language (Conf/lang.yaml), often invented (.0815);
- Linguist's languages.yml at LINGUIST_REV (the revision bench-linguist uses),
  checked against its git blob id: the names, aliases and extensions labels are
  mapped to.

Sampling (seeded, per language): among the language's files of 3+ non-blank
lines and at most 100 KB, up to 2 solutions of 2 different tasks. The file
keeps its name (derived from the label through acmeism's table: the
content-only runs are the fair reading — see README.md).

Labels are mapped to Linguist's names for synonyms only (labels.csv): exact
name (case aside), a Linguist alias, or a hand-checked entry of MANUAL below.
A case is right when the answer is the Linguist name, one of its aliases, or
Rosetta Code's own name for the language.

The files are not stored in this repository (Rosetta Code's content is under
the GNU FDL 1.2): the script fetches the dump (a shallow fetch of one commit
into the cache, default .work/ or $BENCH_CACHE), checks every file against its
git blob id and writes it to files/<sha1_git>, which run.py reads.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import random
import re
import subprocess
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROSETTA = "https://github.com/acmeism/RosettaCodeData"
ROSETTA_REV = "1d475861d7141ef2fafff293d9339f56e4b0f5db"  # 2026-07-16, "Data updates"
LINGUIST = "https://github.com/github-linguist/linguist"
LINGUIST_REV = "76f88c6d3c22f8560d22d29854f24d9607f9edde"  # 2026-09-25, as bench-linguist
LANGUAGES_YML = "1f72a41cd8f04e170b79d95aea99a4bf1df54458"  # git blob id of lib/linguist/languages.yml there
VERSION = "bench-rosetta/1"
SEED = 20261003
PER_LANGUAGE, MIN_LINES, TINY_LINES, MAX_BYTES = 2, 3, 5, 100 * 1024
SOURCE = "Rosetta Code"
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "path", "population"]

# Rosetta Code name → (Linguist name(s), ";"-separated, "" = not mapped; why). Checked one by one; the rule is
# synonyms only: another name or spelling of the same language, a Linguist alias, a version (XSLT 2.0), or a
# shell Linguist files under a name by its interpreter (ksh → Shell). Dialects, implementations and broader or
# narrower names (X86 Assembly vs Assembly, Free Pascal vs Pascal) are not mapped. The second group overrides
# a match by name or alias that would be wrong (false friends).
MANUAL = {
    "1C": ("1C Enterprise", "1C:Enterprise's language"),
    "68000 Assembly": ("Motorola 68K Assembly", "m68k is the Linguist alias"),
    "Apache Ant": ("Ant Build System", ""),
    "AutoHotKey V2": ("AutoHotkey", "a version"),
    "Brainf***": ("Brainfuck", "the name, censored"),
    "C Shell": ("Tcsh", "Linguist's Tcsh lists csh as interpreter and .csh as extension"),
    "C sharp": ("C#", "via PL-ultimate-llm's crosswalk"),
    "Clipper/XBase++": ("xBase", "clipper is a Linguist alias of xBase"),
    "F Sharp": ("F#", "via PL-ultimate-llm's crosswalk"),
    "Fortran": ("Fortran;Fortran Free Form", "Linguist splits Fortran by source form (fixed, free); the label "
                "covers both"),
    "Friendly interactive shell": ("fish", "fish's full name"),
    "GML": ("Game Maker Language", "Rosetta Code: Game Maker Language (GML)"),
    "Ksh": ("Shell", "Linguist's Shell lists ksh as interpreter and .ksh as extension"),
    "Lean": ("Lean;Lean 4", "the category holds Lean 3 and Lean 4 code, two languages in Linguist"),
    "LiveCode": ("LiveCode Script", ""),
    "MIRC Scripting Language": ("mIRC Script", ""),
    "MOO": ("Moocode", "LambdaMOO's language"),
    "N/t/roff": ("Roff", "nroff and troff are Linguist aliases"),
    "Nu": ("Nushell", "Rosetta Code's Nu is Nushell's language, not Linguist's Nu (a Lisp on Objective-C)"),
    "OpenEdge/Progress": ("OpenEdge ABL", "progress and openedge are Linguist aliases"),
    "PlainTeX": ("TeX", "TeX with its plain format; Linguist's TeX also covers LaTeX (an alias)"),
    "Q Sharp": ("Q#", "via PL-ultimate-llm's crosswalk"),
    "Sass/SCSS": ("Sass;SCSS", "the category names both syntaxes"),
    "Spin": ("Propeller Spin", ""),
    "TI-83 BASIC": ("TI Program", "Linguist's TI Program is TI-83/84 BASIC (.8xp)"),
    "Transact-SQL": ("TSQL", ""),
    "UNIX Shell": ("Shell", "Bourne-family shells; sh and bash are Linguist aliases"),
    "V (Vlang)": ("V", "vlang is the Linguist alias"),
    "Visual Basic": ("Visual Basic 6.0", "classic VB (VB.NET has its own category); Linguist's alias "
                     "'visual basic' points to VB.NET, 'visual basic classic' to Visual Basic 6.0"),
    "Visual FoxPro": ("xBase", "foxpro is a Linguist alias of xBase"),
    "XSLT 1.0": ("XSLT", "a version"),
    "XSLT 2.0": ("XSLT", "a version"),
    # false friends
    "Astro": ("", "a programming language; Linguist's Astro is the web framework's component format"),
    "Bird": ("", "a language written in batch; Linguist's BIRD2 (alias bird) is a routing daemon's configuration"),
    "Blade": ("", "a programming language; Linguist's Blade is Laravel's template language"),
    "Go!": ("", "another language than Go"),
    "S-lang": ("", "Linguist's Slang is a shading language"),
    "V": ("", "the concatenative V (Vlang is V (Vlang))"),
}


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def fetch(url: str, rev: str, dest: Path) -> None:
    """One commit, shallow, no checkout: files are read from git objects (an existing clone at rev will do)."""
    if not dest.exists():
        git("init", "-q", str(dest))
        git("remote", "add", "origin", url, cwd=dest)
    if subprocess.run(["git", "cat-file", "-e", rev + "^{commit}"], cwd=dest, capture_output=True).returncode:
        print(f"fetching {url} at {rev[:7]} …", flush=True)
        git("fetch", "-q", "--depth", "1", "origin", rev, cwd=dest)


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def linguist_languages(cache: Path) -> dict:
    p = cache / f"languages-{LINGUIST_REV[:7]}.yml"
    if not p.exists():
        with urllib.request.urlopen(f"{LINGUIST.replace('github.com', 'raw.githubusercontent.com')}/"
                                    f"{LINGUIST_REV}/lib/linguist/languages.yml") as r:
            p.write_bytes(r.read())
    data = p.read_bytes()
    if blob_id(data) != LANGUAGES_YML:
        raise SystemExit(f"{p}: does not match Linguist's languages.yml at {LINGUIST_REV[:7]}")
    return yaml.safe_load(data.decode("utf-8"))


def name_key(name: str) -> str:
    """As tools/score.py: no case, spaces or punctuation."""
    return re.sub(r"[^a-z0-9+#*]", "", name.lower())


def crosswalk(label: str, langs: dict) -> tuple[list[str], str, str]:
    """A source label → (Linguist names, how: exact / alias / manual / none, note)."""
    if label in MANUAL:
        names, note = MANUAL[label]
        return names.split(";") if names else [], "manual" if names else "none", note
    k = name_key(label)
    by_key = {n for n in langs if name_key(n) == k}
    if len(by_key) == 1:
        return sorted(by_key), "exact", "" if label in langs else "spelling"
    by_alias = {n for n, d in langs.items() if k in {name_key(x) for x in d.get("aliases") or []}}
    if len(by_alias) == 1:
        return sorted(by_alias), "alias", ""
    return [], "none", ""


def expected_names(label: str, names: list[str], langs: dict) -> tuple[str, list[str]]:
    """The expected name and the accepted ones: the Linguist names and their aliases, and the label itself unless
    it is the name or alias of another Linguist language (a false friend: `Nu` for Nushell). An unmapped false
    friend is qualified with the source, so that the other language's answer is not accepted."""
    owners = {n for n, d in langs.items() if name_key(label) in {name_key(x) for x in [n, *(d.get("aliases") or [])]}}
    if names:
        accept = [x for n in names for x in [n, *(langs[n].get("aliases") or [])]]
        return names[0], list(dict.fromkeys(accept + ([label] if owners <= set(names) else [])))
    own = f"{label} ({SOURCE})" if owners else label
    return own, [own]


def scan(repo: Path) -> tuple[dict[str, str], list[tuple[str, str, int]]]:
    """Language directory → Rosetta Code name; every solution file (path, sha1_git, size)."""
    names, files = {}, []
    for line in git("ls-tree", "-r", "-z", "-l", ROSETTA_REV, "--", "Lang", "Task", cwd=repo).split("\0"):
        if not line:
            continue
        meta, path = line.split("\t", 1)
        mode, kind, sha, size = meta.split()
        parts = path.split("/")
        if parts[0] == "Lang" and len(parts) == 3 and parts[2] == "00-META.yaml":
            url = yaml.safe_load(git("cat-file", "blob", sha, cwd=repo))["from"]
            names[parts[1]] = urllib.parse.unquote(url.split("Category:", 1)[1]).replace("_", " ")
        elif parts[0] == "Task" and len(parts) == 4 and kind == "blob":
            files.append((path, sha, int(size)))
    return names, sorted(files)


def read_blobs(repo: Path, shas: list[str]):
    """(sha, bytes) for each blob, through one `git cat-file --batch`."""
    p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=repo, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for sha in shas:
        p.stdin.write(sha.encode() + b"\n")
        p.stdin.flush()
        head = p.stdout.readline().split()
        data = p.stdout.read(int(head[2]))
        p.stdout.read(1)
        yield sha, data
    p.stdin.close()
    p.wait()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", type=Path, default=Path(os.environ.get("BENCH_CACHE", HERE / ".work")),
                    help="where the sources are fetched (default .work/, or $BENCH_CACHE)")
    a = ap.parse_args()
    a.cache.mkdir(parents=True, exist_ok=True)
    repo = a.cache / "RosettaCodeData"
    fetch(ROSETTA, ROSETTA_REV, repo)
    langs = linguist_languages(a.cache)
    ext_langs: dict[str, set[str]] = defaultdict(set)
    for name, d in langs.items():
        for e in d.get("extensions") or []:
            ext_langs[e.lower()].add(name)

    names, files = scan(repo)
    small = [(p, s) for p, s, size in files if size <= MAX_BYTES]
    lines = {}
    for sha, data in read_blobs(repo, sorted({s for _, s in small})):
        lines[sha] = sum(1 for ln in data.split(b"\n") if ln.strip())
    by_lang: dict[str, list[tuple[str, str]]] = defaultdict(list)
    population: dict[str, int] = defaultdict(int)
    for path, sha, size in files:
        d = path.split("/")[2]
        population[d] += 1
        if size <= MAX_BYTES and lines[sha] >= MIN_LINES:
            by_lang[d].append((path, sha))

    rows, xwalk = [], {}
    for d in sorted(population, key=lambda d: names[d].lower()):
        label = names[d]
        linguist, how, note = crosswalk(label, langs)
        expected, accept = expected_names(label, linguist, langs)
        pool = list(by_lang[d])
        random.Random(f"{SEED}/{label}").shuffle(pool)
        picked, tasks = [], set()
        for path, sha in pool:
            task = path.split("/")[1]
            if task not in tasks:
                picked.append((path, sha))
                tasks.add(task)
            if len(picked) == PER_LANGUAGE:
                break
        xwalk[label] = {"source_label": label, "linguist": ";".join(linguist), "how": how, "note": note,
                        "files": population[d], "eligible": len(by_lang[d]), "cases": len(picked)}
        for path, sha in sorted(picked):
            name = path.rsplit("/", 1)[1]
            ext = "." + name.rsplit(".", 1)[1]
            claimants = ext_langs.get(ext.lower(), set())
            tags = ["in-linguist" if linguist else "not-in-linguist"]
            if not claimants:
                tags.append("invented-ext")
            elif not claimants & set(linguist):
                tags.append("misleading-ext")
            if len(claimants) > 1:
                tags.append("ambiguous-ext")
            if lines[sha] < TINY_LINES:
                tags.append("tiny")
            rows.append({
                "case_id": "rosetta:" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12],
                "tier": "gold", "ext": ext, "sha1_git": sha, "filename": name,
                "qualified_swhid": f"swh:1:cnt:{sha};origin={ROSETTA};path=/{path}",
                "expected": expected, "expected_detail": label, "accept": ";".join(accept),
                "reference": "the contributor (the language heading the solution is filed under on rosettacode.org)",
                "provenance": f"RosettaCodeData@{ROSETTA_REV[:7]}", "frame": "", "stratum": "", "weight": "",
                "tags": ";".join(tags), "path": path, "population": population[d],
            })
    files_dir = HERE / "files"
    files_dir.mkdir(exist_ok=True)
    for sha, data in read_blobs(repo, sorted({r["sha1_git"] for r in rows})):
        if blob_id(data) != sha:
            raise SystemExit(f"{sha}: content does not match its git blob id")
        if not (files_dir / sha).exists() or (files_dir / sha).read_bytes() != data:
            (files_dir / sha).write_bytes(data)
    with (HERE / "cases.csv.tmp").open("w", encoding="utf-8", newline="") as f:  # replaced at once, below
        f.write(f"# {VERSION} — {len(rows)} Rosetta Code solutions (RosettaCodeData {ROSETTA_REV[:7]}), up to "
                f"{PER_LANGUAGE} per language, labelled by the contributor's language heading; generated by "
                "build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    os.replace(HERE / "cases.csv.tmp", HERE / "cases.csv")
    with (HERE / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# Rosetta Code language → Linguist name(s) at {LINGUIST_REV[:7]}; synonyms only (see README.md); "
                "files = solutions in the dump, eligible = of 3+ non-blank lines and at most 100 KB, cases = sampled; "
                "generated by build_cases.py\n")
        w = csv.DictWriter(f, fieldnames=["source_label", "linguist", "how", "note", "files", "eligible", "cases"],
                           lineterminator="\n")
        w.writeheader()
        w.writerows(xwalk[k] for k in sorted(xwalk, key=str.lower))
    n_in = sum("in-linguist" in r["tags"].split(";") for r in rows)
    print(f"{len(rows)} cases in {len({r['expected_detail'] for r in rows})} languages (of {len(population)} with "
          f"solutions); {n_in} in a Linguist language; "
          + ", ".join(f"{sum(t in r['tags'].split(';') for r in rows)} {t}"
                      for t in ("invented-ext", "misleading-ext", "ambiguous-ext", "tiny")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
