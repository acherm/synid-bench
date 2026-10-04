#!/usr/bin/env python3
"""Build bench-hello: the hello-world programs of leachim6/hello-world, one per
language, labelled by the language their file is named after → cases.csv +
files/ + labels.csv.

    python3 benchmarks/bench-hello/build_cases.py [--cache DIR]

Everything is pinned, so the output is the same on every machine:
- leachim6/hello-world at HELLO_REV: <initial>/<Language>.<ext>, the file name
  chosen by the contributor (the stem is the language, with the substitutions
  of the repository's update_list.py: ∗ for *, ˸ for :, …);
- Linguist's languages.yml at LINGUIST_REV (the revision bench-linguist uses),
  checked against its git blob id: the names, aliases and extensions labels are
  mapped to.

Every program is a case (README, licence and the images under t/ are not
programs). Since the stem is the label, each file is renamed hello<ext> (the
original path is kept in `path`); a file without extension is run as `hello`.

Labels are mapped to Linguist's names for synonyms only (labels.csv): exact
name (case and punctuation aside), a Linguist alias, or a hand-checked entry
of MANUAL below. A case is right when the answer is the Linguist name, one of
its aliases, or the label itself.

The files are not stored in this repository (they are MIT-licensed, but kept
out like every benchmark's): the script fetches the repository (a shallow
fetch of one commit into the cache, default .work/ or $BENCH_CACHE), checks
every file against its git blob id and writes it to files/<sha1_git>.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import subprocess
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
HELLO = "https://github.com/leachim6/hello-world"
HELLO_REV = "a152253b102999bf31988fef077101022e2ad1a5"  # 2026-01-20, "Add Koka (#1763)"
LINGUIST = "https://github.com/github-linguist/linguist"
LINGUIST_REV = "76f88c6d3c22f8560d22d29854f24d9607f9edde"  # 2026-09-25, as bench-linguist
LANGUAGES_YML = "1f72a41cd8f04e170b79d95aea99a4bf1df54458"  # git blob id of lib/linguist/languages.yml there
VERSION = "bench-hello/1"
SOURCE = "hello-world"
# update_list.py: the characters a file name cannot hold, and what they stand for
SUBSTITUTIONS = {"∕": "/", "＼": "\\", "˸": ":", "∗": "*", "？": "?", "＂": '"', "﹤": "<", "﹥": ">", "❘": "|"}
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "path"]

# Label → (Linguist name(s), ";"-separated, "" = not mapped; why). Checked one by one, file in hand; the rule is
# synonyms only: another name or spelling of the same language, a Linguist alias, a version (Python 2), or a
# shell Linguist files under a name by its interpreter (ksh → Shell). Dialects, implementations, frameworks,
# platforms and broader or narrower names (Assembler MASM DOS vs Assembly, Node.js vs JavaScript) are not mapped.
# The second group overrides a match by name or alias that would be wrong (false friends).
MANUAL = {
    "4th Dimension": ("4D", ""),
    "ActionScript 2": ("ActionScript", "a version"),
    "ActionScript flashmx": ("ActionScript", "a version (Flash MX)"),
    **{f"Assembler NASM {os_}": ("Assembly", "nasm is a Linguist alias of Assembly")
       for os_ in ("FreeBSD", "Linux", "Linux64", "Macho64", "Win32", "Win64")},
    "Assembler m68000 amigaos": ("Motorola 68K Assembly", "68000 assembly"),
    "C Shell": ("Tcsh", "Linguist's Tcsh lists csh as interpreter and .csh as extension"),
    "Cache ObjectScript": ("ObjectScript", "InterSystems Caché's ObjectScript"),
    "Cil": ("IL Assembly", ".NET's Common Intermediate Language (Linguist's CIL is SELinux's)"),
    "CypherNeo4j": ("Cypher", "Neo4j's Cypher"),
    "DreamMaker": ("DM", "BYOND's Dream Maker language"),
    "EBuild": ("Gentoo Ebuild", ""),
    "Erlang EScript": ("Erlang", "an Erlang script"),
    "Fortran": ("Fortran;Fortran Free Form", "Linguist splits Fortran by source form (fixed, free); the label "
                "covers both"),
    "Fortran77": ("Fortran", "a version (fixed form)"),
    "GML": ("Game Maker Language", "the file is Game Maker Language"),
    "Il": ("IL Assembly", ".NET's intermediate language"),
    "Inform": ("Inform 7", "the file is Inform 7, Linguist's only Inform"),
    "Jade": ("Pug", "Jade's new name"),
    "KSH": ("Shell", "Linguist's Shell lists ksh as interpreter and .ksh as extension"),
    "Kotlin Script": ("Kotlin", "Kotlin's script form (.kts is a Kotlin extension)"),
    "Kv": ("kvlang", "Kivy's language"),
    "Lean": ("Lean;Lean 4", "the label covers Lean 3 and Lean 4, two languages in Linguist"),
    "LiveCode": ("LiveCode Script", ""),
    "MATLAB 1.0": ("MATLAB", "a version"),
    "Mirc": ("mIRC Script", ""),
    "Moo": ("Moocode", "LambdaMOO's language"),
    "Org-mode": ("Org", ""),
    "Pig": ("PigLatin", "Apache Pig's language"),
    "PostScript Page": ("PostScript", ""),
    "Python 2": ("Python", "a version"),
    "RPG IV": ("RPGLE", "ile rpg is a Linguist alias"),
    "Visual Basic Script": ("VBScript", ""),
    "VisualFoxPro": ("xBase", "foxpro is a Linguist alias of xBase"),
    "XBase++": ("xBase", "Linguist's xBase gathers the dBase dialects (clipper, foxpro, advpl)"),
    "Z Shell": ("Shell", "zsh is a Linguist alias"),
    "daScript": ("Daslang", "daScript's new name"),
    "dBase": ("xBase", "the language xBase is named after"),
    "dos": ("Batchfile", "DOS batch (dosbatch is a Linguist alias)"),
    # false friends
    "@text": ("", "an esoteric language, not plain text"),
    "C--": ("", "another language than C"),
    "Cω": ("", "an extension of C#, not C"),
    "D♭♭": ("", "another language than D"),
    "Django": ("", "a web framework (the file is Python); Linguist's alias django is Jinja's"),
    "HTTP": ("", "a protocol (the file is Python); Linguist's HTTP is request/response text"),
    "IRC": ("", "an mIRC command; Linguist's IRC log is a chat log"),
    "Monkey": ("", "the Monkey of 'Writing an Interpreter in Go' (puts), not Monkey X"),
    "OX": ("", "the file is Oz; Linguist's Ox is an econometrics language"),
    "Tea": ("", "a scripting language (echo); Linguist's Tea is a template language"),
}
# labels that name a framework, library, platform, runtime, implementation or protocol rather than a language: the
# file is written in another language, often the one its extension names (Flask.py is Python) — tag `not-a-language`
NOT_A_LANGUAGE = {
    "Android", "Angular", "Ansible", "Arduino", "Blender", "Bottle", "CGI", "CherryPy", "CLISP", "Deno", "Django",
    "Express", "FastAPI", "Flask", "Flutter", "GitHub Actions", "Google Apps Script", "HTTP", "Hubot", "IronScheme",
    "Jenkinsfile", "Jython", "Kivy", "Koa", "libavg", "Löve", "LWC", "Manim", "Mathematica Online", "MicroPython",
    "Minecraft", "Mongo", "Mozart", "Node.js", "PyQt4", "PyQt5", "PySide2", "PySimpleGUI", "Pygame", "React",
    "React Native", "React360", "Redis", "Ruby on Rails", "Sidekiq", "SmallTalk GNU", "Swift Playgrounds", "Tk",
    "Tkinter", "WSH", "wxPython", "zx",
}
# one file of a label used twice for two languages
PATHS = {"v/V": ("", "an esoteric V (iHello World); the other file labelled V, V.v, is Vlang")}


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


def crosswalk(label: str, langs: dict, manual: tuple[str, str] | None = None) -> tuple[list[str], str, str]:
    """A source label → (Linguist names, how: exact / alias / manual / none, note)."""
    if manual or label in MANUAL:
        names, note = manual or MANUAL[label]
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
    repo = a.cache / "hello-world"
    fetch(HELLO, HELLO_REV, repo)
    langs = linguist_languages(a.cache)
    ext_langs: dict[str, set[str]] = defaultdict(set)
    for name, d in langs.items():
        for e in d.get("extensions") or []:
            ext_langs[e.lower()].add(name)

    progs = []  # (path, sha1_git): <initial>/<file>, the programs
    for line in git("ls-tree", "-r", "-z", HELLO_REV, cwd=repo).split("\0"):
        if line:
            meta, path = line.split("\t", 1)
            if re.fullmatch(r"[a-z#]/[^/]+", path) and meta.split()[1] == "blob":
                progs.append((path, meta.split()[2]))
    data = dict(read_blobs(repo, sorted({sha for _, sha in progs})))
    by_bytes = defaultdict(set)
    rows, xwalk = [], {}
    for path, sha in sorted(progs):
        stem, ext = os.path.splitext(path.split("/", 1)[1])
        label = stem
        for x, y in SUBSTITUTIONS.items():
            label = label.replace(x, y)
        linguist, how, note = crosswalk(label, langs, PATHS.get(path))
        expected, accept = expected_names(label, linguist, langs)
        entry = xwalk.setdefault(label, {"source_label": label, "note": "", "files": 0})
        if path in PATHS:
            entry["except"] = f"except {path}: {PATHS[path][1]}"
        else:
            entry.update(linguist=";".join(linguist), how=how, note=note)
        entry["files"] += 1
        claimants = ext_langs.get(ext.lower(), set())
        tags = ["in-linguist" if linguist else "not-in-linguist"]
        if not ext:
            tags.append("no-ext")
        elif claimants and not claimants & set(linguist):
            tags.append("misleading-ext")
        if len(claimants) > 1:
            tags.append("ambiguous-ext")
        if label in NOT_A_LANGUAGE:
            tags.append("not-a-language")
        if b"\0" in data[sha][:8000]:
            tags.append("binary")
        by_bytes[sha].add(expected)
        rows.append({
            "case_id": "hello:" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12],
            "tier": "gold", "ext": ext, "sha1_git": sha, "filename": "hello" + ext,
            "qualified_swhid": f"swh:1:cnt:{sha};origin={HELLO};path=/{path}",
            "expected": expected, "expected_detail": label, "accept": ";".join(accept),
            "reference": "the contributor (the language the file is named after)",
            "provenance": f"hello-world@{HELLO_REV[:7]}", "frame": "", "stratum": "", "weight": "",
            "tags": ";".join(tags), "path": path,
        })
    for r in rows:  # the same bytes filed under two languages: no reading of the content can get both
        if len(by_bytes[r["sha1_git"]]) > 1:
            r["tags"] += ";shared-bytes"
    files_dir = HERE / "files"
    files_dir.mkdir(exist_ok=True)
    for sha, b in data.items():
        if blob_id(b) != sha:
            raise SystemExit(f"{sha}: content does not match its git blob id")
        if not (files_dir / sha).exists() or (files_dir / sha).read_bytes() != b:
            (files_dir / sha).write_bytes(b)
    with (HERE / "cases.csv.tmp").open("w", encoding="utf-8", newline="") as f:  # replaced at once, below
        f.write(f"# {VERSION} — {len(rows)} hello-world programs (leachim6/hello-world {HELLO_REV[:7]}), labelled by "
                "the language their file is named after; generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    os.replace(HERE / "cases.csv.tmp", HERE / "cases.csv")
    with (HERE / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# hello-world label → Linguist name(s) at {LINGUIST_REV[:7]}; synonyms only (see README.md); "
                "files = programs with that label; generated by build_cases.py\n")
        w = csv.DictWriter(f, fieldnames=["source_label", "linguist", "how", "note", "files"], lineterminator="\n")
        w.writeheader()
        for k in sorted(xwalk, key=str.lower):
            e = xwalk[k]
            w.writerow({**{c: e[c] for c in w.fieldnames}, "note": "; ".join(x for x in (e["note"], e.get("except")) if x)})
    n_in = sum("in-linguist" in r["tags"].split(";") for r in rows)
    print(f"{len(rows)} cases, {len(xwalk)} labels; {n_in} in a Linguist language; "
          + ", ".join(f"{sum(t in r['tags'].split(';') for r in rows)} {t}"
                      for t in ("misleading-ext", "ambiguous-ext", "no-ext", "not-a-language", "binary",
                                "shared-bytes")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
