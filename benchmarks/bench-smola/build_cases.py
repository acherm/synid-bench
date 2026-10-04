#!/usr/bin/env python3
"""Build bench-smola: the samples of smola/language-dataset — whole files from
GitHub repositories, 1,280 of them labelled by a human → cases.csv + files/ +
labels.csv + excluded.csv.

    python3 benchmarks/bench-smola/build_cases.py [--cache DIR]

Everything is pinned, so the output is the same on every machine:
- language-dataset at DATASET_REV (2022-07-15): data/dataset.yml lists 4,047
  samples `github.com/<owner>/<repo>/<commit>/<path>` with their annotations
  (`human-<user>`, `linguist`, `linguist-<strategy>`, `pygments-filename`,
  `vote`), and data/github.com/ holds their bytes;
- Linguist at LINGUIST_REV (76f88c6, the revision bench-linguist uses): its
  languages.yml gives the names, aliases and extension claims; at
  LINGUIST_META_REV (v7.22.0, the revision the dataset's meta.yml was generated
  from) it gives the names the dataset's labels map to — a language whose
  `language_id` has another name at LINGUIST_REV was renamed since;
- the sample files of Linguist (at LINGUIST_REV and at the releases the
  Linguist-family entries were built from, LINGUIST_TRAINED) and of
  Hyperpolyglot (HYPLY_REV): a sample byte-identical to one of them is tagged
  `in-linguist-samples` (training data of the Linguist family).

Tier and label: `gold` when a human annotated the sample (expected = the human
label), `silver` otherwise (expected = the dataset's `vote`, which without a
human is Linguist's own answer of 2019–2022 in all but two samples). Samples
whose label is `Unknown` (not a language: the human found none, or the vote
is undecided) and the two whose human annotators disagree are not cases in
this version: they are written to excluded.csv.

A case is right when the answer is the expected Linguist name, one of its
Linguist aliases, or the dataset's own name (`accept`); where the dataset's
label groups several Linguist languages (FAMILY), each of them.

The files are not stored in this repository (each keeps its own licence): the
script fetches language-dataset (a sparse, blob-less clone in the cache),
checks every file against its git blob id, and writes it to files/<sha1_git>,
which run.py reads. The cache is --cache, or $SYNID_BENCH_CACHE, or .work/.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DATASET = "https://github.com/smola/language-dataset"
DATASET_REV = "4d1827d1018b922e03a48a5de5cb921a6762dda3"  # 2022-07-15
LINGUIST = "https://github.com/github-linguist/linguist"
LINGUIST_REV = "76f88c6d3c22f8560d22d29854f24d9607f9edde"  # 2026-09-25, as bench-linguist
LINGUIST_META_REV = "c0b49c1cc6e1667484c291aabd50c21340ddc9ef"  # v7.22.0, 2022-07-13: the dataset's meta.yml
# releases the Linguist family was built from: Linguist 9.7.0, 8.0.0, 7.30.0; go-enry 2.9.6, 2.8.9
LINGUIST_TRAINED = ["v9.7.0", "v9.5.0", "v8.0.0", "v7.30.0"]
HYPLY = "https://github.com/monkslc/hyperpolyglot"
HYPLY_REV = "a55a3b58eaed09b4314ef93d78e50a80cfec36f4"  # 2023-05-17
VERSION = "bench-smola/1"
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "type", "path", "commit",
           "source_label", "dataset_linguist"]
NOT_A_LANGUAGE = {"Unknown"}
# dataset labels that group several Linguist languages (data/meta.yml maps them to each): all accepted
FAMILY = {"Fortran": ["Fortran", "Fortran Free Form"]}


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


def load_yaml(text: str):
    return yaml.load(text, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))


def name_key(name: str) -> str:
    """As tools/score.py: names compare without case, spaces or punctuation."""
    return re.sub(r"[^a-z0-9+#*]", "", name.lower())


def crosswalk(label: str, meta: dict, langs: dict, old: dict) -> tuple[str, str, str]:
    """A dataset label → (Linguist name at LINGUIST_REV or "", how, note). The dataset's meta.yml
    maps each label to Linguist names of v7.22.0; a name is followed to LINGUIST_REV by its
    language_id. A label meta.yml maps to no Linguist language is mapped only to a language
    Linguist added since under the same name (up to case and punctuation). Synonyms only."""
    if label in NOT_A_LANGUAGE:
        return "", "none", "not a language"
    if label in FAMILY:
        return label, "exact", "the dataset's label groups " + " and ".join(FAMILY[label]) + ": all accepted"
    by_id = {d["language_id"]: n for n, d in langs.items()}
    name = ((meta.get(label) or {}).get("maps_to", {}).get("linguist") or [""])[0]
    now = by_id.get((old.get(name) or {}).get("language_id")) or (name if name in langs else "")
    if not now:
        same = [n for n in langs if name_key(n) == name_key(label)]
        if same:
            return same[0], "exact" if same[0] == label else "alias", "a Linguist language since v7.22.0"
        return "", "none", (f"{name} is no longer a Linguist language" if name else
                            "no Linguist language in the dataset's meta.yml")
    note = f"renamed in Linguist: {name} → {now}" if now != name else ""
    if now == label:
        return now, "exact", note
    keys = {name_key(now), *(name_key(a) for a in langs[now].get("aliases") or [])}
    return now, "alias" if name_key(label) in keys else "manual", note


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", type=Path, default=Path(os.environ.get("SYNID_BENCH_CACHE") or HERE / ".work"))
    a = ap.parse_args()
    cache = a.cache.resolve()
    cache.mkdir(parents=True, exist_ok=True)
    ds, ling, hyply = cache / "language-dataset", cache / "linguist", cache / "hyperpolyglot"
    clone(DATASET, DATASET_REV, ds, ["data"])
    clone(LINGUIST, LINGUIST_REV, ling, None)
    clone(HYPLY, HYPLY_REV, hyply, None)

    langs = load_yaml(git("show", f"{LINGUIST_REV}:lib/linguist/languages.yml", cwd=ling))
    old = load_yaml(git("show", f"{LINGUIST_META_REV}:lib/linguist/languages.yml", cwd=ling))
    meta = load_yaml((ds / "data/meta.yml").read_text(encoding="utf-8"))["languages"]
    samples = load_yaml((ds / "data/dataset.yml").read_text(encoding="utf-8"))["files"]
    ext_langs: dict[str, set[str]] = defaultdict(set)
    for name, d in langs.items():
        for e in d.get("extensions") or []:
            ext_langs[e.lower()].add(name)
    trained = {LINGUIST_REV[:7]: {s for _, s, _ in tree(ling, LINGUIST_REV, "samples")}}
    trained |= {rev: {s for _, s, _ in tree(ling, rev, "samples")} for rev in LINGUIST_TRAINED}
    trained["hyperpolyglot@" + HYPLY_REV[:7]] = {s for _, s, _ in tree(hyply, HYPLY_REV, "samples")}
    blobs = {path[len("data/"):]: sha for _, sha, path in tree(ds, DATASET_REV, "data/github.com")}

    files = HERE / "files"
    files.mkdir(exist_ok=True)
    rows, excluded, walk = [], [], {}
    for key in sorted(samples):
        ann, note = samples[key]["annotations"], samples[key].get("notes") or ""
        _, owner, repo, commit, *rest = key.split("/")
        path, name = "/".join(rest), rest[-1]
        sha = blobs[key]
        data = (ds / "data" / key).read_bytes()
        if blob_id(data) != sha:  # checkout filters (line endings) — take the blob itself
            data = subprocess.run(["git", "cat-file", "blob", sha], cwd=ds, check=True, capture_output=True).stdout
        if blob_id(data) != sha:
            raise SystemExit(f"{key}: content does not match its git blob id")
        humans = {k[len("human-"):]: v for k, v in ann.items() if k.startswith("human-")}
        label = ann["vote"] if not humans else next(iter(humans.values()))
        if len(set(humans.values())) > 1 or label in NOT_A_LANGUAGE:
            excluded.append({"sample": key, "sha1_git": sha,
                             "why": "humans disagree" if len(set(humans.values())) > 1 else
                                    "human: Unknown" if humans else "vote: Unknown",
                             "annotations": "; ".join(f"{k}: {v}" for k, v in sorted(ann.items()) if k != "vote"),
                             "note": note})
            continue
        (files / sha).write_bytes(data)
        if label not in walk:
            walk[label] = crosswalk(label, meta, langs, old)
        linguist, how, _ = walk[label]
        expected = linguist or label
        ext = "" if "." not in name.lstrip(".") else "." + name.rsplit(".", 1)[1]
        tags = []
        if humans and ann.get("linguist") and ann["linguist"] != label:
            tags.append("human-overrode-linguist")
        if ext and len(ext_langs.get(ext.lower(), ())) > 1:
            tags.append("ambiguous-ext")
        if any(sha in s for s in trained.values()):
            tags.append("in-linguist-samples")
        if walk[label][2].startswith("renamed"):
            tags.append("label-renamed")
        rows.append({
            "case_id": "smola:" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:12],
            "tier": "gold" if humans else "silver", "ext": ext, "sha1_git": sha, "filename": name,
            "qualified_swhid": f"swh:1:cnt:{sha};origin=https://github.com/{owner}/{repo};path=/{path}",
            "expected": expected, "expected_detail": label + (f" — note: {note}" if note else ""),
            "accept": ";".join(dict.fromkeys([*(FAMILY.get(label) or [expected]),
                                              *((langs.get(expected) or {}).get("aliases") or []), label])),
            "reference": ("human annotation (" + ", ".join(sorted(humans)) + ")" if humans else
                          "the dataset's vote (Linguist's answer)" if ann["vote"] == ann.get("linguist") else
                          "the dataset's vote (" + ", ".join(k for k in sorted(ann) if ann[k] == label and k != "vote")
                          + ")"),
            "provenance": f"language-dataset@{DATASET_REV[:7]}", "frame": "", "stratum": "", "weight": "",
            "tags": ";".join(tags), "type": (langs.get(expected) or {}).get("type", ""), "path": path,
            "commit": commit, "source_label": label, "dataset_linguist": ann.get("linguist", ""),
        })
    with (HERE / "cases.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {VERSION} — {len(rows)} files from GitHub repositories, the samples of smola/language-dataset "
                f"({DATASET_REV[:7]}), labelled by a human (gold) or by the dataset's vote (silver); generated by "
                "build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    with (HERE / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# language-dataset's labels ({DATASET_REV[:7]}) → Linguist's names at {LINGUIST_REV[:7]}; "
                "synonyms only (how: exact | alias | manual | none); generated by build_cases.py\n")
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["source_label", "linguist", "how", "note"])
        walk.setdefault("Unknown", crosswalk("Unknown", meta, langs, old))
        for label in sorted(walk, key=str.lower):
            w.writerow([label, *walk[label]])
    with (HERE / "excluded.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {VERSION} — samples of language-dataset ({DATASET_REV[:7]}) not scored: label `Unknown` or "
                "human annotators disagree; generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=["sample", "sha1_git", "why", "annotations", "note"], lineterminator="\n")
        w.writeheader()
        w.writerows(excluded)

    n = Counter(r["tier"] for r in rows)
    tags = Counter(t for r in rows for t in r["tags"].split(";") if t)
    print(f"{len(rows)} cases ({n['gold']} gold, {n['silver']} silver) in {len({r['expected'] for r in rows})} "
          f"languages; {len(excluded)} samples excluded ({Counter(e['why'] for e in excluded)}); tags {dict(tags)}")
    for src, s in trained.items():
        hits = [r for r in rows if r["sha1_git"] in s]
        print(f"  identical to a sample of {src}: {len(hits)} cases {[r['path'] for r in hits]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
