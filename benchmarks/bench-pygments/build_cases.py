#!/usr/bin/env python3
"""Build bench-pygments: Pygments' example files (tests/examplefiles/<lexer alias>/<file>), labelled by
the lexer of their directory → cases.csv, labels.csv + files/.

    python3 benchmarks/bench-pygments/build_cases.py [--cache DIR]

Everything is pinned, so the output is the same on every machine:
- Pygments at PYGMENTS_REV: the example files, and pygments/lexers/_mapping.py, which resolves a
  directory (a lexer alias) to its lexer (name, aliases, file name patterns);
- Linguist at LINGUIST_REV (languages.yml: the names `expected` uses; samples/: a file byte-identical
  to a sample is tagged `linguist-sample`);
- Hyperpolyglot at HYPLY_REV (samples/, the training set of Synid's classifier: `seen-in-training`).

A lexer is kept when it names a language: one Linguist 76f88c6 has (of any type), or, for the others,
a programming, markup, data, configuration, template or grammar language. Excluded (NOT_A_LANGUAGE):
transcripts of interactive sessions (consoles, REPLs), the output of a program (logs, dumps, diffs,
test reports) and plain text — unless Linguist has a language for them (ShellSession, Python console,
Julia REPL, Python traceback and IRC log are kept). The `*.output` files (Pygments' golden token
streams) are left out, and so is tests/examplefiles/conftest.py.

The label crosswalk (labels.csv, Pygments lexer name → Linguist name) is: MANUAL first, else the
lexer name equals a Linguist name (`exact`), else a Linguist alias (`alias`), else none — synonyms
only, as in tools/external/*/names.csv.

A file whose name contains its label (`perl_misc.pl`, `glsl.frag`) is renamed `example<ext>` (tag
`renamed`; the original is in `path`), unless the whole name is one by which Linguist or Pygments
identifies the language (`Makefile`, `nginx.conf`, `meson.build`).

The files are not stored in this repository: the script fetches them (a shallow, blob-less, sparse
fetch of the pinned commit into the cache, by default .work/), checks every file against its git
blob id, and writes it to files/<sha1_git>, which run.py reads.
"""

from __future__ import annotations

import argparse
import ast
import csv
import fnmatch
import hashlib
import os
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PYGMENTS = "https://github.com/pygments/pygments"
PYGMENTS_REV = "156d85fdd18d34427fe893527e71da91dcfb0eb5"  # 2026-09-27
LINGUIST = "https://github.com/github-linguist/linguist"
LINGUIST_REV = "76f88c6d3c22f8560d22d29854f24d9607f9edde"  # 2026-09-25, as bench-linguist
HYPLY = "https://github.com/monkslc/hyperpolyglot"
HYPLY_REV = "a55a3b58eaed09b4314ef93d78e50a80cfec36f4"  # 2023-05-17
VERSION = "bench-pygments/1"
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "type", "path"]

# directories (lexer aliases) whose lexer is not a language and that Linguist has no language for
NOT_A_LANGUAGE = {
    # transcripts of interactive sessions
    "doscon", "dylan-console", "erl", "gap-repl", "iex", "matlabsession", "nodejsrepl", "psql", "psysh",
    "pwsh-session", "rbcon", "rconsole", "sqlite3", "tcshcon",
    # the output of a program: logs, dumps, query plans, diffs, test reports, version-control status
    "hexdump", "kmsg", "notmuch", "objdump-nasm", "output", "postgres-explain", "pypylog", "tap",
    "vctreestatus", "wdiff",
    # plain text
    "text",
}

# Pygments lexer name → Linguist name(s) (";" = a family: every member is accepted), "" = none.
# Checked before the exact and alias matches, so it also overrides them.
MANUAL = {
    "Java Server Page": "Java Server Pages",  # Linguist lists "java server page" as an alias of Groovy Server Pages
    "Fortran": "Fortran Free Form",  # Pygments' Fortran lexer is for free-form Fortran (*.f90, *.f03)
    "FortranFixed": "Fortran",  # Linguist's Fortran is fixed-form (*.f, *.for)
    "aspx-cs": "ASP.NET",  # Linguist has aspx-vb as an alias of ASP.NET; same file type
    "ASCII armored": "Public Key",
    "BST": "BibTeX Style",
    "Csound Orchestra": "Csound",
    "Debian Control file": "Debian Package Control File",
    "Django/Jinja": "Jinja",
    "Docker": "Dockerfile",
    "Graphviz": "Graphviz (DOT)",
    "HTML+Handlebars": "Handlebars",
    "Julia console": "Julia REPL",
    "MQL": "MQL4;MQL5",
    "Nimrod": "Nim",
    "Org Mode": "Org",
    "Pig": "PigLatin",
    "Properties": "Java Properties",
    "Python console session": "Python console",
    "Python 2.x Traceback": "Python traceback",
    "Ragel in CPP Host": "Ragel",
    "ReasonML": "Reason",
    "reg": "Windows Registry Entries",
    "S": "R",  # Pygments' S lexer is its R lexer (aliases splus, s, r; *.R); Linguist has splus as an alias of R
    "TASM": "Assembly",  # Turbo Assembler, x86: Linguist's Assembly is x86 assembly (aliases asm, nasm)
    "Transact-SQL": "TSQL",
    "World of Warcraft TOC": "World of Warcraft Addon Data",
    "Zone": "DNS Zone",
}


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def fetch(url: str, rev: str, dest: Path, sparse: list[str] | None) -> None:
    """A shallow, blob-less fetch of `rev` into dest; checks out the `sparse` paths (None: trees only)."""
    if not (dest / ".git").exists():
        dest.mkdir(parents=True, exist_ok=True)
        git("init", "-q", cwd=dest)
        git("remote", "add", "origin", url, cwd=dest)
    if subprocess.run(["git", "cat-file", "-e", rev + "^{commit}"], cwd=dest, capture_output=True).returncode:
        git("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", rev, cwd=dest)
    if sparse is not None:
        git("sparse-checkout", "set", "--no-cone", *sparse, cwd=dest)
        git("checkout", "-q", "--detach", rev, cwd=dest)


def tree(repo: Path, rev: str, prefix: str) -> list[tuple[str, str, str]]:
    """(mode, sha1_git, path) of every blob under prefix at rev."""
    out = []
    for line in git("ls-tree", "-r", "-z", rev, "--", prefix, cwd=repo).split("\0"):
        if not line:
            continue
        meta, path = line.split("\t", 1)
        mode, kind, sha = meta.split()
        if kind == "blob":
            out.append((mode, sha, path))
    return out


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def read_blob(repo: Path, path: str, sha: str) -> bytes:
    data = (repo / path).read_bytes()
    if blob_id(data) != sha:  # checkout filters (line endings) — take the blob itself
        data = subprocess.run(["git", "cat-file", "blob", sha], cwd=repo, check=True, capture_output=True).stdout
    if blob_id(data) != sha:
        raise SystemExit(f"{path}: content does not match its git blob id")
    return data


def key(name: str) -> str:
    """Names compare as in tools/score.py: without case, spaces or punctuation."""
    return re.sub(r"[^a-z0-9+#*]", "", name.lower())


def crosswalk(label: str, langs: dict) -> tuple[list[str], str]:
    """A source label → (Linguist names, how): manual | exact | alias | none."""
    if label in MANUAL:
        names = [n for n in MANUAL[label].split(";") if n]
        for n in names:
            if n not in langs:
                raise SystemExit(f"MANUAL: {n!r} is not a Linguist language")
        return names, "manual" if names else "none"
    by_name = {key(n): n for n in langs}
    if key(label) in by_name:
        return [by_name[key(label)]], "exact"
    by_alias = {key(a): n for n, d in langs.items() for a in d.get("aliases") or []}
    if key(label) in by_alias:
        return [by_alias[key(label)]], "alias"
    return [], "none"


def non_blank_lines(data: bytes) -> int:
    return sum(1 for line in data.decode("utf-8", "replace").splitlines() if line.strip())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", type=Path, default=Path(os.environ.get("SYNID_BENCH_CACHE") or HERE / ".work"),
                    help="where the sources are fetched (default: $SYNID_BENCH_CACHE, else .work/)")
    a = ap.parse_args()
    pyg, ling, hyply = a.cache / "pygments", a.cache / "linguist", a.cache / "hyperpolyglot"
    fetch(PYGMENTS, PYGMENTS_REV, pyg, ["/tests/examplefiles/", "/pygments/lexers/_mapping.py"])
    fetch(LINGUIST, LINGUIST_REV, ling, ["/lib/linguist/languages.yml"])
    fetch(HYPLY, HYPLY_REV, hyply, None)
    linguist_samples = {sha for _, sha, _ in tree(ling, LINGUIST_REV, "samples")}
    seen = {sha for _, sha, _ in tree(hyply, HYPLY_REV, "samples")}
    langs = yaml.safe_load((ling / "lib/linguist/languages.yml").read_text(encoding="utf-8"))
    ext_langs: dict[str, set[str]] = defaultdict(set)
    for name, d in langs.items():
        for e in d.get("extensions") or []:
            ext_langs[e.lower()].add(name)
    linguist_filenames = {f for d in langs.values() for f in d.get("filenames") or []}

    src = (pyg / "pygments/lexers/_mapping.py").read_text(encoding="utf-8")
    lexers = ast.literal_eval(src[src.index("{"):src.rindex("}") + 1])  # class → (module, name, aliases, files, mimes)
    by_alias = {al: cls for cls, (_, _, aliases, _, _) in lexers.items() for al in aliases}

    files = HERE / "files"
    files.mkdir(exist_ok=True)
    rows, labels, excluded = [], {}, Counter()
    for mode, sha, path in sorted(tree(pyg, PYGMENTS_REV, "tests/examplefiles"), key=lambda t: t[2]):
        parts = path.split("/")
        if len(parts) != 4 or path.endswith(".output") or mode == "120000":
            continue
        alias, name = parts[2], parts[3]
        if alias not in by_alias:
            raise SystemExit(f"{path}: no lexer has the alias {alias!r}")
        if alias in NOT_A_LANGUAGE:
            excluded[alias] += 1
            continue
        _, lexer, aliases, patterns, _ = lexers[by_alias[alias]]
        names, how = crosswalk(lexer, langs)
        labels.setdefault(lexer, (names, how, alias, Counter()))[3][alias] += 1
        expected = names[0] if names else lexer
        data = read_blob(pyg, path, sha)
        (files / sha).write_bytes(data)

        # a name that gives the label away is renamed, unless it is a name the language is known by
        tokens = {key(t) for t in [lexer, *aliases, *names, *(a for n in names for a in langs[n].get("aliases") or [])]}
        stem = key(name.rsplit(".", 1)[0] if "." in name.lstrip(".") else name)
        whole = name in linguist_filenames or any(fnmatch.fnmatchcase(name, p) for p in patterns if p[0] != "*")
        renamed = not whole and any(len(t) >= 3 and t in stem for t in tokens)
        ext = "" if "." not in name.lstrip(".") else "." + name.rsplit(".", 1)[1]
        filename = "example" + ext if renamed else name

        tags = ["in-linguist" if names else "not-in-linguist"]
        if ext and len(ext_langs.get(ext.lower(), ())) > 1:
            tags.append("ambiguous-ext")
        if non_blank_lines(data) < 5:
            tags.append("tiny")
        if renamed:
            tags.append("renamed")
        if sha in linguist_samples:
            tags.append("linguist-sample")
        if sha in seen:
            tags.append("seen-in-training")
        accept = [*names, *(a for n in names for a in langs[n].get("aliases") or []), lexer]
        rows.append({
            "case_id": "pyg:" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12],
            "tier": "gold", "ext": ext, "sha1_git": sha, "filename": filename,
            "qualified_swhid": f"swh:1:cnt:{sha};origin={PYGMENTS};path=/{path}",
            "expected": expected, "expected_detail": f"{lexer} (Pygments lexer `{alias}`)",
            "accept": ";".join(dict.fromkeys(accept)),
            "reference": "Pygments' maintainers (the example's directory: a lexer alias)",
            "provenance": f"pygments@{PYGMENTS_REV[:7]}", "frame": "", "stratum": "", "weight": "",
            "tags": ";".join(tags), "type": (langs.get(expected) or {}).get("type", ""), "path": path,
        })
    with (HERE / "cases.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {VERSION} — {len(rows)} example files of Pygments ({PYGMENTS_REV[:7]}), labelled by the lexer "
                "of their directory; generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    with (HERE / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# Pygments lexer name ({PYGMENTS_REV[:7]}) → Linguist name(s) ({LINGUIST_REV[:7]}); how: exact | alias "
                "| manual | none. Synonyms only (a dialect or a broader/narrower language is not mapped); "
                "generated by build_cases.py\n")
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["source_label", "linguist", "how", "source_id", "cases"])
        for lexer, (names, how, alias, n) in sorted(labels.items(), key=lambda kv: kv[0].lower()):
            w.writerow([lexer, ";".join(names), how, ";".join(sorted(n)), sum(n.values())])
    tag = Counter(t for r in rows for t in r["tags"].split(";"))
    print(f"{len(rows)} cases, {len(labels)} lexers ({len({r['expected'] for r in rows})} labels); "
          f"excluded {sum(excluded.values())} files of {len(excluded)} lexers that are not languages; tags: "
          + ", ".join(f"{t} {n}" for t, n in sorted(tag.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
