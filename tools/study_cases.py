"""Shared by the benchmarks built from PL-ultimate-llm's Software Heritage extension studies
(bench-rpgle, bench-fsf, bench-cobol): pinned reads of the study data, the files' bytes,
qualified SWHIDs, post-stratified weights, and cases.csv.

Not a command: each benchmark's build_cases.py imports it. The study data (per-content
reports, worklists, origin tables) is read from a PL-ultimate-llm checkout ($PL_ULTIMATE_LLM,
by default a sibling of synid-bench) at the pinned commit PL_REV, with `git cat-file`, so
uncommitted edits in the checkout do not change the cases. A few inputs are not in that
repository's git (the byte cache, some origin tables, Jev's re-judging): they are read from
the working tree when present, and each build script says which.

The bytes come from the studies' local cache (.cache/cobol/<sha1_git>.bin in the checkout)
or, when absent, from the Software Heritage API (anonymous, or with $SWH_TOKEN), cached in
the benchmark's .work/; every file is checked against its sha1_git.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
PL = Path(os.environ.get("PL_ULTIMATE_LLM", ROOT.parent / "PL-ultimate-llm")).resolve()
PL_URL = "https://github.com/acherm/PL-ultimate-llm"
PL_REV = "274fa4cc8bcc1bb6b29959d28c9e3120bcd75790"  # swh-evidence-v1, 2026-10-03 (Linguist 76f88c6 import)
PL_BLOB = f"{PL_URL}/blob/{PL_REV[:9]}"
SWH_RAW = "https://archive.softwareheritage.org/api/1/content/sha1_git:{}/raw/"
COLUMNS = ["case_id", "tier", "ext", "sha1_git", "filename", "qualified_swhid", "expected", "expected_detail",
           "accept", "reference", "provenance", "frame", "stratum", "weight", "tags", "path"]


def git(*args: str, data: bytes | None = None) -> bytes:
    return subprocess.run(["git", "-C", str(PL), *args], input=data, check=True, capture_output=True).stdout


def pinned(path: str) -> bytes:
    """A file tracked by PL-ultimate-llm, as of PL_REV."""
    return git("cat-file", "blob", f"{PL_REV}:{path}")


def pinned_dir(prefix: str) -> dict[str, bytes]:
    """Every file tracked under prefix at PL_REV → its bytes (one `git cat-file --batch`)."""
    paths = [p for p in git("ls-tree", "-r", "--name-only", "-z", PL_REV, "--", prefix).decode().split("\0") if p]
    out = git("cat-file", "--batch", data="".join(f"{PL_REV}:{p}\n" for p in paths).encode())
    files, i = {}, 0
    for p in paths:
        j = out.index(b"\n", i)
        size = int(out[i:j].split()[2])
        files[p] = out[j + 1:j + 1 + size]
        i = j + 1 + size + 1
    return files


def pinned_csv(path: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(pinned(path).decode("utf-8"))))


def pinned_jsonl(path: str) -> list[dict]:
    return [json.loads(line) for line in pinned(path).decode("utf-8").splitlines() if line.strip()]


def local(path: str) -> bytes | None:
    """A file of the checkout's working tree that is not in its git (cache, local data), or None."""
    p = PL / path
    return p.read_bytes() if p.is_file() else None


def check_checkout() -> None:
    if not (PL / ".git").exists():
        raise SystemExit(f"no PL-ultimate-llm checkout at {PL} (set PL_ULTIMATE_LLM; clone {PL_URL})")
    try:
        git("cat-file", "-e", f"{PL_REV}^{{commit}}")
    except subprocess.CalledProcessError:
        raise SystemExit(f"{PL} has no commit {PL_REV[:9]}: git -C {PL} fetch origin swh-evidence-v1")


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def content(sha: str, work: Path) -> bytes | None:
    """The bytes of a content, verified: the studies' cache, else .work/swh/, else the SWH API."""
    for p in (PL / ".cache" / "cobol" / f"{sha}.bin", work / "swh" / sha):
        if p.is_file() and blob_id(data := p.read_bytes()) == sha:
            return data
    req = urllib.request.Request(SWH_RAW.format(sha))
    if os.environ.get("SWH_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['SWH_TOKEN']}")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:  # rate limit: anonymous clients get a few hundred requests per hour
                time.sleep(int(e.headers.get("Retry-After") or 60))
                continue
            return None
    else:
        return None
    if blob_id(data) != sha:
        return None
    (work / "swh").mkdir(parents=True, exist_ok=True)
    (work / "swh" / sha).write_bytes(data)
    return data


def origin_index(text: str, shas: set[str]) -> dict[str, list[dict]]:
    """A study's origin table (swhid, name, SWH browse URL) → sha1_git → [{name, origin, path}]."""
    idx: dict[str, list[dict]] = {}
    rd = csv.reader(io.StringIO(text))
    next(rd, None)
    for row in rd:
        if len(row) < 3:
            continue
        sha = row[0].replace("swh:1:cnt:", "").split(";")[0].strip()
        if sha in shas:
            q = parse_qs(urlparse(row[2]).query)
            idx.setdefault(sha, []).append({"name": row[1].lstrip("/"), "origin": (q.get("origin_url") or [""])[0],
                                            "path": (q.get("path") or [""])[0].lstrip("/")})
    return idx


def locate(sha: str, name: str, rows: list[dict], origin: str = "") -> tuple[str, str, str]:
    """(origin, path, qualified SWHID). The browse URL's path is kept only when it ends with the
    file's name (in a few rows it names another file of the directory); the origin the study
    recorded is preferred when there is one."""
    rows = sorted(rows, key=lambda r: (r["origin"] != origin, r["path"].rsplit("/", 1)[-1] != name,
                                       r["origin"], r["path"]))
    best = rows[0] if rows else {"origin": origin, "path": ""}
    o = best["origin"] or origin
    path = best["path"] if best["path"].rsplit("/", 1)[-1] == name and best["origin"] == o else ""
    swhid = f"swh:1:cnt:{sha}" + (f";origin={o}" if o else "") + (f";path=/{path}" if path else "")
    return o, path, swhid


class Linguist:
    """GitHub Linguist's languages (76f88c6, as imported by PL-ultimate-llm at PL_REV)."""

    def __init__(self):
        self.langs = yaml.safe_load(pinned("data/raw/linguist_languages.yml"))

    def accept(self, expected: str, *own: str) -> str:
        """expected + its Linguist aliases + the source's own names (`;`-separated, no two alike)."""
        aliases = (self.langs.get(expected) or {}).get("aliases") or []
        out: dict[str, str] = {}
        for x in (expected, *aliases, *own):
            if x and name_key(x) not in out:
                out[name_key(x)] = x
        return ";".join(out.values())


def name_key(name: str) -> str:
    return re.sub(r"[^a-z0-9+#*]", "", name.lower())


def neutral_name(name: str, ext: str, labels: list[str]) -> str:
    """The archived name, or `source<ext>` when its stem contains the label (the name would give
    the answer away to a name-based identifier); labels shorter than 3 characters are ignored."""
    stem = name_key(name[: -len(ext)] if ext and name.endswith(ext) else name)
    keys = [name_key(x) for x in labels if len(name_key(x)) >= 3]
    return f"source{ext}" if any(k in stem for k in keys) else name


def text_tags(raw: bytes) -> list[str]:
    t = []
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        t.append("non-utf8")
        text = raw.decode("latin-1")
    if text.count("\n") < 3:
        t.append("tiny")
    return t


def post_stratify(rows: list[dict], sample: Counter, n_sample: int, population: int) -> None:
    """weight = N̂_h / n_h: the stratum's share of the uniform sample (`sample`, over its n_sample
    draws) times the population size, over the number of cases kept in the stratum."""
    kept = Counter(r["stratum"] for r in rows)
    for r in rows:
        r["weight"] = round(population * sample[r["stratum"]] / n_sample / kept[r["stratum"]], 4)


def write_cases(bench: Path, header: str, rows: list[dict]) -> None:
    with (bench / "cases.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {header}; generated by build_cases.py; see README.md\n")
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def write_files(bench: Path, blobs: dict[str, bytes]) -> float:
    """files/<sha1_git>, exactly these; returns the total size in MB."""
    files = bench / "files"
    files.mkdir(exist_ok=True)
    for f in files.iterdir():
        if f.name not in blobs:
            f.unlink()
    for sha, data in blobs.items():
        p = files / sha
        if not p.exists() or p.stat().st_size != len(data):
            p.write_bytes(data)
    return sum(len(d) for d in blobs.values()) / 1e6


def write_labels(bench: Path, rows: list[tuple[str, str, str]]) -> None:
    """labels.csv: the study's label → Linguist name(s) (synonyms only), how."""
    with (bench / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["source_label", "linguist", "how"])
        w.writerows(rows)


# ---------------------------------------------------------------- reference entries
# Jev 1.13 (TypeSafe's lightweight decision model, OpenRouter's Decisions API), run by the studies
# on every judged file with 63 labels designed for them: data/derived/jev/<study>/<probe>.jsonl in
# PL-ultimate-llm (not in its git). Its labels → Linguist names; a family label → its members
# (several names = undecided); the labels for content that is not code → Text.
JEV_NAME = {
    "abap": ["ABAP"], "ada": ["Ada"], "assembly": ["Assembly"], "basic": ["BASIC"], "c": ["C"], "cpp": ["C++"],
    "csharp": ["C#"], "dart": ["Dart"], "forth": ["Forth"], "fortran": ["Fortran"], "glsl": ["GLSL"], "go": ["Go"],
    "haskell": ["Haskell"], "ibm-cl": ["IBM CL"], "java": ["Java"], "javascript": ["JavaScript"], "jcl": ["JCL"],
    "julia": ["Julia"], "kotlin": ["Kotlin"], "limbo": ["Limbo"], "lua": ["Lua"], "magma": ["Magma"],
    "maple": ["Maple"], "matlab": ["MATLAB"], "mercury": ["Mercury"], "mumps": ["M"], "natural": ["Natural"],
    "objective-c": ["Objective-C"], "pascal": ["Pascal"], "perl": ["Perl"], "php": ["PHP"], "pli": ["PL/I"],
    "prolog": ["Prolog"], "python": ["Python"], "r": ["R"], "rpg": ["RPGLE"], "ruby": ["Ruby"], "rust": ["Rust"],
    "scala": ["Scala"], "scilab": ["Scilab"], "shell": ["Shell"], "smalltalk": ["Smalltalk"], "sql": ["SQL"],
    "swift": ["Swift"], "tcl": ["Tcl"], "tex": ["TeX"], "wolfram": ["Wolfram Language"], "cobol": ["COBOL"],
    "xml-html": ["XML", "HTML"], "json-yaml": ["JSON", "YAML"]}
JEV_NOT_CODE = {"binary-or-garbled", "empty", "key-value-config", "placeholder-text", "prose", "tabular-data"}
JEV_ENTRIES = {
    "langid": ("Jev 1.13, study's 63 labels, content only",
               "TypeSafe's lightweight decision model (OpenRouter's Decisions API), asked which of 63 labels the "
               "file is written in, from its content only (no file name). Its label set was designed for "
               "PL-ultimate-llm's extension studies; its `rpg` is mapped to RPGLE, `xml-html` and `json-yaml` "
               "count as undecided, `key-value-config`, `placeholder-text`, `prose`, … as Text"),
    "langid_ext": ("Jev 1.13, study's 63 labels, with file name", "the same question, the file name shown as well"),
}


def read_entries_cases(bench: Path) -> tuple[str, list[dict]]:
    text = (bench / "cases.csv").read_text(encoding="utf-8")
    cases = list(csv.DictReader(line for line in text.splitlines() if not line.startswith("#")))
    return text.splitlines()[0].lstrip("# ").split(" —")[0], cases


def write_entry(bench: Path, label: str, meta: dict, answers: dict[str, list[str] | None]) -> None:
    version, cases = read_entries_cases(bench)
    (bench / "entries").mkdir(exist_ok=True)
    with (bench / "entries" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": {"label": label, **meta, "benchmark": version}}) + "\n")
        for c in cases:
            f.write(json.dumps({"case_id": c["case_id"], "answer": answers.get(c["sha1_git"])}) + "\n")
    n = sum(1 for c in cases if answers.get(c["sha1_git"]))
    print(f"{label}: {n}/{len(cases)} answered → {bench.name}/entries/{label}.jsonl")


def export_jev(bench: Path, study: str) -> None:
    """The study's two Jev probes on these files, as entries (jev-langid, jev-langid_ext)."""
    for probe, (name, about) in JEV_ENTRIES.items():
        raw = local(f"data/derived/jev/{study}/{probe}.jsonl")
        if raw is None:
            print(f"jev-{probe}: data/derived/jev/{study}/{probe}.jsonl absent — skipped")
            continue
        last = {}
        for line in raw.decode("utf-8").splitlines():
            d = json.loads(line)
            if d.get("ok"):
                last[d["sha1_git"]] = d
        model = next(iter(last.values())).get("model", "typesafe/jev-1.13")
        ans = {}
        for sha, d in last.items():
            ch = d["answers"]["language"]["choice"]
            ans[sha] = ["Text"] if ch in JEV_NOT_CODE else JEV_NAME.get(ch, ["Other"])
        write_entry(bench, f"jev-{probe}", {
            "name": name, "kind": "llm-light", "version": f"{model}, probe jev-probe/1 `{probe}`", "about": about,
            "source": f"stored decisions of the {study} study (PL-ultimate-llm, data/derived/jev/{study}, not in "
                      f"its git)"}, ans)
