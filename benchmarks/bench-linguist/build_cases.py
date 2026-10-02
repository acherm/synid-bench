#!/usr/bin/env python3
"""Build bench-linguist: GitHub Linguist's sample files, labelled by the
directory Linguist's maintainers filed them under → cases.csv + files/.

    python3 benchmarks/bench-linguist/build_cases.py

Everything is pinned, so the output is the same on every machine:
- Linguist at LINGUIST_REV, the revision Software Heritage archived on
  2026-09-25 (every sample resolves as a SWHID with that origin);
- Hyperpolyglot at HYPLY_REV: its `samples/` directory, a 2023 copy of
  Linguist's, is the training set of the Bayesian classifier Synid uses
  ("hyplyclassifier") — a sample byte-identical to one of them is tagged
  `seen-in-training`, the others `unseen`.

A case is right when the answer is the sample's language or one of its
Linguist aliases (`accept`; names compare case-, space- and punctuation-
insensitively, see tools/score.py).

The sample files are not stored in this repository (each keeps its own
licence): the script fetches Linguist's `samples/` (a sparse, blob-less clone
in .work/), checks every file against its git blob id, and writes it to
files/<sha1_git>, which run.py reads. Symbolic links are left out.
"""

from __future__ import annotations

import csv
import hashlib
import subprocess
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
WORK = HERE / ".work"
LINGUIST = "https://github.com/github-linguist/linguist"
LINGUIST_REV = "76f88c6d3c22f8560d22d29854f24d9607f9edde"  # 2026-09-25, archived by SWH the same day
HYPLY = "https://github.com/monkslc/hyperpolyglot"
HYPLY_REV = "a55a3b58eaed09b4314ef93d78e50a80cfec36f4"  # 2023-05-17
VERSION = "bench-linguist/1"
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "type", "path"]


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def clone(url: str, rev: str, dest: Path, sparse: list[str] | None) -> None:
    if not dest.exists():
        git("clone", "-q", "--filter=blob:none", "--no-checkout", url, str(dest))
    if sparse is not None:
        git("sparse-checkout", "set", "--no-cone", *sparse, cwd=dest)
        git("checkout", "-q", rev, cwd=dest)
    else:
        git("cat-file", "-e", rev, cwd=dest)


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


def main() -> int:
    WORK.mkdir(exist_ok=True)
    ling, hyply = WORK / "linguist", WORK / "hyperpolyglot"
    clone(LINGUIST, LINGUIST_REV, ling, ["samples", "lib/linguist/languages.yml"])
    clone(HYPLY, HYPLY_REV, hyply, None)
    seen = {sha for _, sha, _ in tree(hyply, HYPLY_REV, "samples")}
    langs = yaml.safe_load((ling / "lib/linguist/languages.yml").read_text(encoding="utf-8"))
    by_dir = {d.get("fs_name") or name: name for name, d in langs.items()}  # a sample directory → its language
    ext_langs: dict[str, set[str]] = defaultdict(set)
    for name, d in langs.items():
        for e in d.get("extensions") or []:
            ext_langs[e.lower()].add(name)

    files = HERE / "files"
    files.mkdir(exist_ok=True)
    rows = []
    for mode, sha, path in sorted(tree(ling, LINGUIST_REV, "samples"), key=lambda t: t[2]):
        if mode == "120000":
            continue
        parts = path.split("/")
        lang, name = by_dir.get(parts[1], parts[1]), parts[-1]
        by_filename = len(parts) > 3 and parts[2] == "filenames"
        data = (ling / path).read_bytes()
        if blob_id(data) != sha:  # checkout filters (line endings) — take the blob itself
            data = subprocess.run(["git", "cat-file", "blob", sha], cwd=ling, check=True, capture_output=True).stdout
        if blob_id(data) != sha:
            raise SystemExit(f"{path}: content does not match its git blob id")
        (files / sha).write_bytes(data)
        ext = "" if by_filename or "." not in name.lstrip(".") else "." + name.rsplit(".", 1)[1]
        tags = ["seen-in-training" if sha in seen else "unseen"]
        if by_filename:
            tags.append("by-filename")
        elif ext and len(ext_langs.get(ext.lower(), ())) > 1:
            tags.append("ambiguous-ext")
        rows.append({
            "case_id": "ling:" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12],
            "tier": "gold", "ext": ext, "sha1_git": sha, "filename": name,
            "qualified_swhid": f"swh:1:cnt:{sha};origin={LINGUIST};path=/{path}",
            "expected": lang, "expected_detail": lang,
            "accept": ";".join(dict.fromkeys([lang, *((langs.get(lang) or {}).get("aliases") or [])])),
            "reference": "Linguist's maintainers (the sample's directory)",
            "provenance": f"linguist@{LINGUIST_REV[:7]}", "frame": "", "stratum": "", "weight": "",
            "tags": ";".join(tags), "type": (langs.get(lang) or {}).get("type", ""), "path": path,
        })
    with (HERE / "cases.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {VERSION} — {len(rows)} sample files of GitHub Linguist ({LINGUIST_REV[:7]}), labelled by "
                "their directory; generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    n_seen = sum("seen-in-training" in r["tags"] for r in rows)
    print(f"{len(rows)} cases in {len({r['expected'] for r in rows})} languages; {n_seen} seen in training, "
          f"{len(rows) - n_seen} unseen; {sum('ambiguous-ext' in r['tags'] for r in rows)} with an ambiguous "
          f"extension; {sum('by-filename' in r['tags'] for r in rows)} identified by file name")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
