#!/usr/bin/env python3
"""Build bench-rouge: Rouge's visual samples (spec/visual/samples/<tag>) and demos
(lib/rouge/demos/<tag>), labelled by the lexer they are named after → cases.csv, labels.csv + files/.

    python3 benchmarks/bench-rouge/build_cases.py [--cache DIR]

Everything is pinned, so the output is the same on every machine:
- Rouge at ROUGE_REV: the samples, the demos, and lib/rouge/lexers/*.rb, which give each lexer's
  tag, title (`title "…"`; Rouge's default is the tag, capitalised) and aliases;
- Linguist at LINGUIST_REV (languages.yml: the names `expected` uses; samples/: a file byte-identical
  to a sample is tagged `linguist-sample`);
- Hyperpolyglot at HYPLY_REV (samples/, the training set of Synid's classifier: `seen-in-training`).

Each file is named by its lexer's tag, without an extension — a name that is the label — so every
case is run without a name (`filename` and `ext` empty): only the content counts. Samples are tagged
`sample`; demos (a few lines each, shown on Rouge's site) `demo`, and a demo byte-identical to the
sample of the same lexer is left out.

A lexer is kept when it names a language: the rule of bench-pygments — excluded (NOT_A_LANGUAGE) are
transcripts of interactive sessions, the output of a program, plain text, and Rouge's `escape`
helper — unless Linguist has a language for them (`console` → ShellSession is kept).

The label crosswalk (labels.csv, title → Linguist name) is: MANUAL first, else the title, then the
tag, equals a Linguist name (`exact`) or a Linguist alias (`alias`), else none — synonyms only, as in
tools/external/*/names.csv. A label that names a family maps to every member Linguist has.

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
ROUGE = "https://github.com/rouge-ruby/rouge"
ROUGE_REV = "16e6ecdb3bc4248cead78375e1b24580ee2352a1"  # 2026-08-28
LINGUIST = "https://github.com/github-linguist/linguist"
LINGUIST_REV = "76f88c6d3c22f8560d22d29854f24d9607f9edde"  # 2026-09-25, as bench-linguist
HYPLY = "https://github.com/monkslc/hyperpolyglot"
HYPLY_REV = "a55a3b58eaed09b4314ef93d78e50a80cfec36f4"  # 2023-05-17
VERSION = "bench-rouge/1"
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "type", "path"]
SETS = {"spec/visual/samples": "sample", "lib/rouge/demos": "demo"}

# lexer tags that are not a language and that Linguist has no language for
NOT_A_LANGUAGE = {
    "irb",  # a transcript of an interactive session
    "irb_output", "tap",  # the output of a program
    "plaintext",  # plain text
    "escape",  # Rouge's helper for escaped content inside another lexer
}

# title → Linguist name(s) (";" = a family: every member is accepted), "" = none.
# Checked before the exact and alias matches, so it also overrides them.
MANUAL = {
    "1C (BSL)": "1C Enterprise",  # BSL, the 1C:Enterprise built-in language
    "Config File": "",  # a generic configuration lexer; Linguist lists conf among INI's aliases
    "Docker": "Dockerfile",
    "DOT": "Graphviz (DOT)",
    "HQL": "HiveQL",  # "Hive Query Language SQL dialect"
    "Plist": "OpenStep Property List",  # the ASCII (OpenStep) plist format, *.pbxproj
    ".properties": "Java Properties",
    "ReasonML": "Reason",
    "Rego": "Open Policy Agent",
    "SSH Config File": "SSH Config",
    "Verilog and System Verilog": "Verilog;SystemVerilog",
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
    """The source's labels (title, then tag) → (Linguist names, how): manual | exact | alias | none."""
    if labels[0] in MANUAL:
        names = [n for n in MANUAL[labels[0]].split(";") if n]
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


def titles(lexers_dir: Path) -> dict[str, str]:
    """Every lexer's tag → title, from the class bodies of lib/rouge/lexers/*.rb."""
    out = {}
    for rb in sorted(lexers_dir.glob("*.rb")):
        for body in re.split(r"\n\s*class\s+\w+\s*<", rb.read_text(encoding="utf-8"))[1:]:
            tag = re.search(r"^\s*tag\s+['\"]([^'\"]+)['\"]", body, re.M)
            if tag:
                title = re.search(r"^\s*title\s+['\"]([^'\"]+)['\"]", body, re.M)
                out[tag.group(1)] = title.group(1) if title else tag.group(1).capitalize()
    return out


def non_blank_lines(data: bytes) -> int:
    return sum(1 for line in data.decode("utf-8", "replace").splitlines() if line.strip())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", type=Path, default=Path(os.environ.get("SYNID_BENCH_CACHE") or HERE / ".work"),
                    help="where the sources are fetched (default: $SYNID_BENCH_CACHE, else .work/)")
    a = ap.parse_args()
    rouge, ling, hyply = a.cache / "rouge", a.cache / "linguist", a.cache / "hyperpolyglot"
    fetch(ROUGE, ROUGE_REV, rouge, [f"/{d}/" for d in SETS] + ["/lib/rouge/lexers/"])
    fetch(LINGUIST, LINGUIST_REV, ling, ["/lib/linguist/languages.yml"])
    fetch(HYPLY, HYPLY_REV, hyply, None)
    linguist_samples = {sha for _, sha, _ in tree(ling, LINGUIST_REV, "samples")}
    seen = {sha for _, sha, _ in tree(hyply, HYPLY_REV, "samples")}
    langs = yaml.safe_load((ling / "lib/linguist/languages.yml").read_text(encoding="utf-8"))
    title_of = titles(rouge / "lib/rouge/lexers")

    files = HERE / "files"
    files.mkdir(exist_ok=True)
    rows, labels, excluded, sample_sha = [], {}, Counter(), {}
    for prefix, kind in SETS.items():
        for mode, sha, path in sorted(tree(rouge, ROUGE_REV, prefix), key=lambda t: t[2]):
            tag = path[len(prefix) + 1:]
            if "/" in tag or mode == "120000":
                continue
            if tag not in title_of:
                raise SystemExit(f"{path}: no lexer has the tag {tag!r}")
            if tag in NOT_A_LANGUAGE:
                excluded[tag] += 1
                continue
            if kind == "sample":
                sample_sha[tag] = sha
            elif sample_sha.get(tag) == sha:
                excluded["demo = sample"] += 1
                continue
            title = title_of[tag]
            names, how = crosswalk([title, tag], langs)
            labels.setdefault(title, (names, how, tag, Counter()))[3][kind] += 1
            expected = names[0] if names else title
            data = read_blob(rouge, path, sha)
            (files / sha).write_bytes(data)
            tags = [kind, "in-linguist" if names else "not-in-linguist"]
            if non_blank_lines(data) < 5:
                tags.append("tiny")
            if sha in linguist_samples:
                tags.append("linguist-sample")
            if sha in seen:
                tags.append("seen-in-training")
            accept = [*names, *(a for n in names for a in langs[n].get("aliases") or []), title, tag]
            rows.append({
                "case_id": "rouge:" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12],
                "tier": "gold", "ext": "", "sha1_git": sha, "filename": "",
                "qualified_swhid": f"swh:1:cnt:{sha};origin={ROUGE};path=/{path}",
                "expected": expected, "expected_detail": f"{title} (Rouge lexer `{tag}`)",
                "accept": ";".join(dict.fromkeys(accept)),
                "reference": f"Rouge's maintainers (the {kind}'s name: a lexer tag)",
                "provenance": f"rouge@{ROUGE_REV[:7]}", "frame": "", "stratum": "", "weight": "",
                "tags": ";".join(tags), "type": (langs.get(expected) or {}).get("type", ""), "path": path,
            })
    with (HERE / "cases.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {VERSION} — {len(rows)} visual samples and demos of Rouge ({ROUGE_REV[:7]}), labelled by the "
                "lexer they are named after, run without a name; generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    with (HERE / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# Rouge lexer title ({ROUGE_REV[:7]}) → Linguist name(s) ({LINGUIST_REV[:7]}); how: exact | alias "
                "| manual | none. Synonyms only (a dialect or a broader/narrower language is not mapped); "
                "generated by build_cases.py\n")
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["source_label", "linguist", "how", "source_id", "cases"])
        for title, (names, how, tag, n) in sorted(labels.items(), key=lambda kv: kv[0].lower()):
            w.writerow([title, ";".join(names), how, tag, sum(n.values())])
    tag = Counter(t for r in rows for t in r["tags"].split(";"))
    print(f"{len(rows)} cases, {len(labels)} lexers ({len({r['expected'] for r in rows})} labels); "
          f"excluded: " + ", ".join(f"{k} {v}" for k, v in sorted(excluded.items())) + "; tags: "
          + ", ".join(f"{t} {n}" for t, n in sorted(tag.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
