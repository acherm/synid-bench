#!/usr/bin/env python3
"""Build bench-hljs: highlight.js' auto-detection test files (test/detect/<language>/<file>), labelled
by their directory → cases.csv, labels.csv + files/.

    python3 benchmarks/bench-hljs/build_cases.py [--cache DIR]

Everything is pinned, so the output is the same on every machine:
- highlight.js at HLJS_REV: the test files, and src/languages/<id>.js, which gives the language's
  name — the `name` highlight.js reports (its id when there is none) — and the header's display
  name (`Language: …`, accepted too);
- Linguist at LINGUIST_REV (languages.yml: the names `expected` uses; samples/: a file byte-identical
  to a sample is tagged `linguist-sample`);
- Hyperpolyglot at HYPLY_REV (samples/, the training set of Synid's classifier: `seen-in-training`).

The files have no names (they are all `default.txt` or a short description of the test): every case
is run without a name (`filename` and `ext` empty), so only the content counts.

A language is kept when it is one: the rule of bench-pygments — excluded (NOT_A_LANGUAGE) are
transcripts of interactive sessions (REPLs), the output of a program (logs, profiles, test reports)
and plain text, unless Linguist has a language for them (Julia REPL, Python console are kept).

The label crosswalk (labels.csv, name → Linguist name) is: MANUAL first, else the name, the display
name, then the id, equals a Linguist name (`exact`) or a Linguist alias (`alias`), else none —
synonyms only, as in tools/external/*/names.csv. A label that names a family (`HTML, XML`) maps to
every member Linguist has.

The files are not stored in this repository: the script fetches them (a shallow, blob-less, sparse
fetch of the pinned commit into the cache, by default .work/), checks every file against its git
blob id, and writes it to files/<sha1_git>, which run.py reads.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import subprocess
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
HLJS = "https://github.com/highlightjs/highlight.js"
HLJS_REV = "fc3f06392f189354eed922973635ab9e9268b983"  # 2026-08-30
LINGUIST = "https://github.com/github-linguist/linguist"
LINGUIST_REV = "76f88c6d3c22f8560d22d29854f24d9607f9edde"  # 2026-09-25, as bench-linguist
HYPLY = "https://github.com/monkslc/hyperpolyglot"
HYPLY_REV = "a55a3b58eaed09b4314ef93d78e50a80cfec36f4"  # 2023-05-17
VERSION = "bench-hljs/1"
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "type", "path"]

# language ids that are not a language and that Linguist has no language for
NOT_A_LANGUAGE = {
    "clojure-repl", "erlang-repl", "node-repl",  # transcripts of interactive sessions
    "accesslog", "profile", "subunit", "tap",  # the output of a program
    "plaintext",  # plain text
}

# name (or display name) → Linguist name(s) (";" = a family: every member is accepted), "" = none.
# Checked before the exact and alias matches, so it also overrides them.
MANUAL = {
    "Arduino": "",  # a dialect of C++ (Linguist files *.ino under C++)
    "Batch file (DOS)": "Batchfile",
    "Caché Object Script": "ObjectScript",  # InterSystems ObjectScript (Caché was the product)
    "GML": "Game Maker Language",
    "HTML, XML": "HTML;XML",
    "TOML, also INI": "INI;TOML",
    "Intel x86 Assembly": "Assembly",  # Linguist's Assembly is x86 assembly (aliases asm, nasm; ace mode assembly_x86)
    "LiveCode": "LiveCode Script",
    "MikroTik RouterOS script": "RouterOS Script",
    "PHP template": "HTML+PHP",  # HTML with <?php … ?> blocks
    "PostgreSQL and PL/pgSQL": "PLpgSQL",  # the display name of `pgsql` (name: PostgreSQL); the one member Linguist has
    ".properties": "Java Properties",
    "Python REPL": "Python console",
    "ReasonML": "Reason",
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


def crosswalk(labels: list[str], langs: dict) -> tuple[list[str], str]:
    """The source's labels (name, display name, id) → (Linguist names, how): manual | exact | alias | none."""
    for label in labels:
        if label in MANUAL:
            names = [n for n in MANUAL[label].split(";") if n]
            for n in names:
                if n not in langs:
                    raise SystemExit(f"MANUAL: {n!r} is not a Linguist language")
            return names, "manual" if names else "none"
    by_name = {key(n): n for n in langs}
    by_alias = {key(a): n for n, d in langs.items() for a in d.get("aliases") or []}
    for label in labels:
        if key(label) in by_name:
            return [by_name[key(label)]], "exact"
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
    hljs, ling, hyply = a.cache / "highlight.js", a.cache / "linguist", a.cache / "hyperpolyglot"
    fetch(HLJS, HLJS_REV, hljs, ["/test/detect/", "/src/languages/"])
    fetch(LINGUIST, LINGUIST_REV, ling, ["/lib/linguist/languages.yml"])
    fetch(HYPLY, HYPLY_REV, hyply, None)
    linguist_samples = {sha for _, sha, _ in tree(ling, LINGUIST_REV, "samples")}
    seen = {sha for _, sha, _ in tree(hyply, HYPLY_REV, "samples")}
    langs = yaml.safe_load((ling / "lib/linguist/languages.yml").read_text(encoding="utf-8"))

    files = HERE / "files"
    files.mkdir(exist_ok=True)
    rows, labels, excluded = [], {}, Counter()
    for mode, sha, path in sorted(tree(hljs, HLJS_REV, "test/detect"), key=lambda t: t[2]):
        parts = path.split("/")
        if len(parts) != 4 or mode == "120000":
            continue  # test/detect/index.js, the test driver
        lang_id = parts[2]
        if lang_id in NOT_A_LANGUAGE:
            excluded[lang_id] += 1
            continue
        src = hljs / "src/languages" / f"{lang_id}.js"
        text = src.read_text(encoding="utf-8") if src.exists() else ""  # json5: an alias of json, no file of its own
        m = (re.search(r"^\s*name:\s*['\"]([^'\"]+)['\"]", text, re.M)
             or re.search(r"\.name\s*=\s*['\"]([^'\"]+)['\"]", text))
        name = m.group(1) if m else lang_id  # highlight.js reports the id when a language has no name
        m = re.search(r"^\s*Language:\s*(.+?)\s*$", text, re.M)
        display = m.group(1) if m else name
        names, how = crosswalk([name, display, lang_id], langs)
        labels.setdefault(name, (names, how, lang_id, Counter()))[3][parts[3]] += 1
        expected = names[0] if names else name
        data = read_blob(hljs, path, sha)
        (files / sha).write_bytes(data)
        tags = ["in-linguist" if names else "not-in-linguist"]
        if non_blank_lines(data) < 5:
            tags.append("tiny")
        if sha in linguist_samples:
            tags.append("linguist-sample")
        if sha in seen:
            tags.append("seen-in-training")
        accept = [*names, *(a for n in names for a in langs[n].get("aliases") or []), name, display, lang_id]
        rows.append({
            "case_id": "hljs:" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12],
            "tier": "gold", "ext": "", "sha1_git": sha, "filename": "",
            "qualified_swhid": f"swh:1:cnt:{sha};origin={HLJS};path=/{path}",
            "expected": expected, "expected_detail": f"{display} (highlight.js `{lang_id}`)",
            "accept": ";".join(dict.fromkeys(accept)),
            "reference": "highlight.js' maintainers (the test's directory: a language id)",
            "provenance": f"highlight.js@{HLJS_REV[:7]}", "frame": "", "stratum": "", "weight": "",
            "tags": ";".join(tags), "type": (langs.get(expected) or {}).get("type", ""), "path": path,
        })
    with (HERE / "cases.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {VERSION} — {len(rows)} auto-detection test files of highlight.js ({HLJS_REV[:7]}), labelled by "
                "their directory, run without a name; generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    with (HERE / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# highlight.js language ({HLJS_REV[:7]}) → Linguist name(s) ({LINGUIST_REV[:7]}); how: exact | alias "
                "| manual | none. Synonyms only (a dialect or a broader/narrower language is not mapped); "
                "generated by build_cases.py\n")
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["source_label", "linguist", "how", "source_id", "cases"])
        for name, (names, how, lang_id, n) in sorted(labels.items(), key=lambda kv: kv[0].lower()):
            w.writerow([name, ";".join(names), how, lang_id, sum(n.values())])
    tag = Counter(t for r in rows for t in r["tags"].split(";"))
    print(f"{len(rows)} cases, {len(labels)} languages ({len({r['expected'] for r in rows})} labels); "
          f"excluded {sum(excluded.values())} files of {len(excluded)} languages that are not languages; tags: "
          + ", ".join(f"{t} {n}" for t, n in sorted(tag.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
