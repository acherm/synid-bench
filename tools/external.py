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
tools/external/<tool>/labels.json (its coverage).
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from run import case_dir, materialise, read_cases  # noqa: E402

TOOLS = {
    "linguist": {"version": "9.7.0", "name": "GitHub Linguist 9.7.0",
                 "about": "GitHub's language detector (Ruby gem): file name, extension, shebang, heuristics, "
                          "Bayesian classifier trained on its own samples",
                 "url": "https://github.com/github-linguist/linguist"},
    "enry": {"version": "2.9.6", "name": "go-enry 2.9.6",
             "about": "Go port of Linguist (used to label The Stack v2 / StarCoder2's data)",
             "url": "https://github.com/go-enry/go-enry"},
    "hyperpolyglot": {"version": "a55a3b5", "name": "Hyperpolyglot a55a3b5",
                      "about": "Rust port of Linguist (2023); Synid's heuristics and classifier come from it",
                      "url": "https://github.com/monkslc/hyperpolyglot"},
    "cloc": {"version": "2.10", "name": "cloc 2.10",
             "about": "line counter; recognises languages by extension, file name and shebang",
             "url": "https://github.com/AlDanial/cloc"},
    "pygments": {"version": "2.21.0", "name": "Pygments 2.21.0",
                 "about": "syntax highlighter: `guess_lexer_for_filename` (file name, then content), or "
                          "`guess_lexer` (content only)",
                 "url": "https://pygments.org", "content_flag": True},
    "magika": {"version": "1.0.3", "name": "Magika 1.0.3",
               "about": "Google's deep-learning content-type detector; reads the bytes only (~200 content types)",
               "url": "https://github.com/google/magika", "content_native": True},
    "guesslang": {"version": "2.2.1", "name": "Guesslang 2.2.1",
                  "about": "deep-learning language guesser used by VS Code; reads the text only (54 languages)",
                  "url": "https://github.com/yoeo/guesslang", "content_native": True,
                  "platform": "linux/amd64"},
}


def image(tool: str) -> str:
    return f"synid-bench/{tool}:{TOOLS[tool]['version']}"


def ensure_image(tool: str) -> None:
    if subprocess.run(["docker", "image", "inspect", image(tool)], capture_output=True).returncode == 0:
        return
    plat = ["--platform", TOOLS[tool]["platform"]] if TOOLS[tool].get("platform") else []
    print(f"building {image(tool)} …", flush=True)
    subprocess.run(["docker", "build", *plat, "-t", image(tool), str(HERE / "external" / tool)], check=True)


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
    ensure_image(a.tool)
    t = TOOLS[a.tool]
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
    with tempfile.TemporaryDirectory(prefix=f"synid-bench-{a.tool}-") as tmp:
        work = Path(tmp)
        materialise(bench, cases, work, content_only)
        t0 = time.time()
        out = docker_run(a.tool, ["--content-only"] if (a.content_only and t.get("content_flag")) else [], work)
        secs = time.time() - t0
    raw = {}
    for line in out.splitlines():
        if line.startswith("{"):
            d = json.loads(line)
            raw[d["dir"]] = d["labels"]
    mapping = name_map(a.tool)
    label = "ext-" + a.tool + ("-content-only" if a.content_only and not native else "")
    meta = {"label": label, "kind": "other-identifier", "benchmark": (bench / "cases.csv").read_text(
                encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0],
            "name": t["name"] + (", content only" if a.content_only and not native else ""),
            "version": f"{image(a.tool)} (tools/external/{a.tool})",
            "about": t["about"] + (" — run on the content only (file named `file`)" if a.content_only and not native
                                   else ""),
            "url": t["url"], "date": time.strftime("%Y-%m-%d"), "seconds": round(secs, 1)}
    (bench / "entries" / "raw").mkdir(parents=True, exist_ok=True)
    with (bench / "entries" / "raw" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps({"case_id": c["case_id"], "labels": raw.get(case_dir(c))}) + "\n")
    with (bench / "entries" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": meta}) + "\n")
        for c in cases:
            labs = raw.get(case_dir(c)) or []
            ans = [n for lab in labs for n in mapping.get(lab, [lab])]
            f.write(json.dumps({"case_id": c["case_id"], "answer": ans or None}) + "\n")
    missing = sum(1 for c in cases if case_dir(c) not in raw)
    print(f"{label}: {len(cases) - missing}/{len(cases)} reported in {secs:.0f}s → {bench / 'entries' / (label + '.jsonl')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
