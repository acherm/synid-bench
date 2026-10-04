#!/usr/bin/env python3
"""Run another language identifier over a benchmark → a leaderboard entry.

    python3 tools/external.py benchmarks/bench-linguist --tool pygments
    python3 tools/external.py benchmarks/bench-linguist --tool pygments --content-only
    python3 tools/external.py --list

Each tool lives in tools/external/<tool>/ as a Docker image with a pinned
version (built on first use, tagged synid-bench/<tool>:<version>), so a run
is reproducible on any machine with Docker. The contract is the same for all:
the benchmark's files are mounted read-only as /in/<case>/<file name> (or
/in/<case>/file with --content-only), and the image prints one JSON line per
case, {"dir": <case>, "labels": [<the tool's own label>]} — an empty list
when the tool gives no answer.

The tool's labels are kept as they are, except where tools/external/<tool>/
names.csv maps one to Linguist's name for the same language (the benchmark's
accepted names already include Linguist's aliases); a label mapped to several
languages counts as undecided. The entry is <bench>/entries/ext-<tool>[-content-only].jsonl
(raw answers in entries/raw/).
`--labels` asks the image for every label the tool can output, written to
tools/external/<tool>/labels.json (its coverage). A tool is a directory with a
Dockerfile, a tool.json (version, name, what it is, flags) and optionally
names.csv; adding one needs no change here.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from run import case_dir, materialise, read_cases  # noqa: E402
from score import name_key  # noqa: E402


def read_card(bench: Path) -> dict:
    p = bench / "card.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

def load_tools() -> dict[str, dict]:
    """Every tools/external/<tool>/tool.json: version, name, about, url, family, and flags —
    content_native (reads the bytes only; a run is content-only by nature), content_flag (the image
    takes --content-only), needs_name (answers from the file name only: not run where a benchmark has
    no file names), platform (docker --platform)."""
    return {p.parent.name: json.loads(p.read_text(encoding="utf-8"))
            for p in sorted((HERE / "external").glob("*/tool.json"))}


TOOLS = load_tools()


def image(tool: str) -> str:
    return f"synid-bench/{tool}:{TOOLS[tool]['version']}"


def source_hash(tool: str) -> str:
    """Hash of what the image is built from (Dockerfile, scripts, lockfiles) — not of names.csv, labels.json or
    tool.json, which do not enter the image."""
    h = hashlib.sha256()
    d = HERE / "external" / tool
    for p in sorted(x for x in d.rglob("*") if x.is_file()):
        if p.name not in ("labels.json", "names.csv", "tool.json", ".DS_Store") and "__pycache__" not in p.parts:
            h.update(str(p.relative_to(d)).encode() + b"\0" + p.read_bytes())
    return h.hexdigest()[:12]


def provenance(tool: str) -> dict[str, str]:
    """What an entry was made with, beyond the image tag: the image's sources and the name mapping — an entry
    whose provenance differs from the tool's current one is out of date (tools/run_all.py reruns it)."""
    p = HERE / "external" / tool / "names.csv"
    return {"source": source_hash(tool),
            "names_csv": hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else ""}


def ensure_image(tool: str) -> None:
    """Build the image unless one built from the same sources exists (label synid-bench.source)."""
    want = source_hash(tool)
    p = subprocess.run(["docker", "image", "inspect", "--format", '{{ index .Config.Labels "synid-bench.source" }}',
                        image(tool)], capture_output=True, text=True)
    if p.returncode == 0 and p.stdout.strip() == want:
        return
    plat = ["--platform", TOOLS[tool]["platform"]] if TOOLS[tool].get("platform") else []
    print(f"building {image(tool)} (sources {want}) …", flush=True)
    subprocess.run(["docker", "build", "--quiet", *plat, "--label", f"synid-bench.source={want}", "-t", image(tool),
                    str(HERE / "external" / tool)], check=True)


def docker_run(tool: str, args: list[str], mount: Path | None = None) -> str:
    plat = ["--platform", TOOLS[tool]["platform"]] if TOOLS[tool].get("platform") else []
    vol = ["-v", f"{mount}:/in:ro"] if mount else []
    p = subprocess.run(["docker", "run", "--rm", "--network", "none", *plat, *vol, image(tool), *args],
                       capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit(f"{tool} failed ({p.returncode}): {p.stderr[-2000:]}")
    return p.stdout


def name_map(tool: str) -> dict[str, list[str]]:
    p = HERE / "external" / tool / "names.csv"
    if not p.exists():
        return {}
    with p.open(encoding="utf-8") as f:
        return {r["label"]: [x for x in r["linguist"].split(";") if x] for r in csv.DictReader(
            line for line in f if not line.startswith("#"))}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bench", type=Path, nargs="?")
    ap.add_argument("--tool", choices=sorted(TOOLS))
    ap.add_argument("--content-only", action="store_true", help="files run as `file`, without their name")
    ap.add_argument("--labels", action="store_true", help="write the tool's label set to labels.json")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list or not a.tool:
        for t, d in TOOLS.items():
            print(f"{t:14} {image(t):34} {d['about']}")
        return 0
    t = TOOLS[a.tool]
    if a.content_only and t.get("needs_name"):
        raise SystemExit(f"{a.tool} answers from the file name only: a content-only run is not applicable")
    ensure_image(a.tool)
    if a.labels:
        labels = json.loads(docker_run(a.tool, ["--labels"]))
        (HERE / "external" / a.tool / "labels.json").write_text(json.dumps(labels, indent=0) + "\n", encoding="utf-8")
        print(f"{a.tool}: {len(labels)} labels → tools/external/{a.tool}/labels.json")
        if not a.bench:
            return 0
    bench = a.bench.resolve()
    cases = read_cases(bench)
    native = t.get("content_native", False)
    content_only = a.content_only or native
    # on a benchmark without file names, a tool that has a content mode runs in it: that is what it does
    # with a nameless file (Pygments' guess_lexer rather than guess_lexer_for_filename)
    nameless = read_card(bench).get("names") == "none"
    content_mode = t.get("content_flag") and (a.content_only or nameless)
    with tempfile.TemporaryDirectory(prefix=f"synid-bench-{a.tool}-") as tmp:
        work = Path(tmp)
        materialise(bench, cases, work, content_only)
        t0 = time.time()
        out = docker_run(a.tool, ["--content-only"] if content_mode else [], work)
        secs = time.time() - t0
    raw = {}
    for line in out.splitlines():
        if line.startswith("{"):
            d = json.loads(line)
            raw[d["dir"]] = {k: v for k, v in d.items() if k != "dir"}
    mapping = name_map(a.tool)
    label = "ext-" + a.tool + ("-content-only" if a.content_only and not native else "")
    meta = {"label": label, "kind": "other-identifier", "benchmark": (bench / "cases.csv").read_text(
                encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0],
            "name": t["name"] + (", content only" if a.content_only and not native else ""),
            "version": f"{image(a.tool)} (tools/external/{a.tool})",
            "about": t["about"] + (" — run on the content only (file named `file`)" if a.content_only and not native
                                   else " — in its content mode (this benchmark has no file names)" if content_mode
                                   else ""),
            "url": t["url"], "date": time.strftime("%Y-%m-%d"), "seconds": round(secs, 1), **provenance(a.tool)}
    (bench / "entries" / "raw").mkdir(parents=True, exist_ok=True)
    with (bench / "entries" / "raw" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps({"case_id": c["case_id"], **(raw.get(case_dir(c)) or {"labels": None})}) + "\n")
    with (bench / "entries" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": meta}) + "\n")
        for c in cases:
            labs = (raw.get(case_dir(c)) or {}).get("labels") or []
            # a label is mapped to Linguist's name(s), unless it is itself one of the case's accepted names (a
            # family label such as highlight.js' "HTML, XML" on a benchmark labelled in highlight.js' names)
            accepted = {name_key(x) for x in c["accept"].split(";") if x}
            ans = [n for lab in labs for n in ([lab] if name_key(lab) in accepted else mapping.get(lab, [lab]))]
            f.write(json.dumps({"case_id": c["case_id"], "answer": ans or None}) + "\n")
    missing = sum(1 for c in cases if case_dir(c) not in raw)
    print(f"{label}: {len(cases) - missing}/{len(cases)} reported in {secs:.0f}s → {bench / 'entries' / (label + '.jsonl')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
