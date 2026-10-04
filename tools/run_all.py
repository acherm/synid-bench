#!/usr/bin/env python3
"""Run every identifier on every benchmark — the whole leaderboard matrix — or what is missing of it.

    python3 tools/run_all.py                                 # every external tool, missing runs only
    python3 tools/run_all.py --synid path/to/synid           # + Synid (default, content only) where missing
    python3 tools/run_all.py --tool rouge --tool chroma --force
    python3 tools/run_all.py --bench bench-hljs --dry-run
    python3 tools/run_all.py --skip 'hf-*' --skip plangrec --jobs 3     # the fast tools first

A run is missing when its entry file does not exist, or when it was made with another version of the tool, other
image sources or another name mapping (the entry's `version`, `source`, `names_csv`): a new release of a tool, or a
fix to its script or names.csv, is run everywhere, and
`tools/tool_history.py` / `tools/history.py` show what it fixed and broke. Each external tool is run with the
file name and, unless it reads the content only by nature or answers from the name only, without it
(`--content-only`). A tool that answers from the file name only is not run on a benchmark without names.
Paid models (Jev) and local LLMs are not run here: see each benchmark's reproduce.sh.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from external import TOOLS, image, provenance  # noqa: E402
from leaderboard import read_card  # noqa: E402
from run import synid_version  # noqa: E402


def entry_provenance(p: Path) -> tuple | None:
    if not p.exists():
        return None
    m = json.loads(p.read_text(encoding="utf-8").splitlines()[0])["meta"]
    return m.get("version"), m.get("source"), m.get("names_csv")


def plan(benches: list[Path], tools: list[str], force: bool) -> list[tuple[Path, list[str], str]]:
    jobs = []
    for b in benches:
        no_names = read_card(b).get("names") == "none"
        for t in tools:
            d = TOOLS[t]
            if d.get("needs_name") and no_names:
                continue
            variants = [[]]
            if not d.get("content_native") and not d.get("needs_name") and not no_names:
                variants.append(["--content-only"])
            for v in variants:
                label = f"ext-{t}" + ("-content-only" if v else "")
                pv = provenance(t)
                want = (f"{image(t)} (tools/external/{t})", pv["source"], pv["names_csv"])
                if force or entry_provenance(b / "entries" / f"{label}.jsonl") != want:
                    jobs.append((b, ["--tool", t, *v], label))
    return jobs


def run_synid(benches: list[Path], synid: str, force: bool, dry: bool) -> None:
    commit = synid_version(synid)["commit"] or "head"
    for b in benches:
        for dest, args in ((b / "baselines" / f"{commit}-default.jsonl", []),
                           (b / "entries" / f"{commit}-content-only.jsonl", ["--content-only"])):
            if dest.exists() and not force:
                continue
            print(f"synid {commit} {' '.join(args) or 'default'} on {b.name}", flush=True)
            if dry:
                continue
            subprocess.run([sys.executable, str(HERE / "run.py"), str(b), "--synid", synid,
                            "--label", dest.stem, *args], check=True)
            dest.parent.mkdir(exist_ok=True)
            shutil.copy(b / "results" / f"{dest.stem}.jsonl", dest)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bench", action="append", default=[], help="benchmark name (default: all)")
    ap.add_argument("--tool", action="append", default=[], choices=sorted(TOOLS), help="tool (default: all)")
    ap.add_argument("--skip", action="append", default=[], help="tool not to run; a trailing * matches a prefix (hf-*)")
    ap.add_argument("--synid", help="also run this Synid binary (default configuration, and content only)")
    ap.add_argument("--force", action="store_true", help="rerun even when an entry of this version exists")
    ap.add_argument("--jobs", type=int, default=3, help="tools run at once (default 3)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    benches = sorted(p for p in (ROOT / "benchmarks").iterdir() if (p / "cases.csv").exists()
                     and (not a.bench or p.name in a.bench))
    missing = [b.name for b in benches if not (b / "files").is_dir()]
    if missing:
        raise SystemExit(f"files not fetched for {', '.join(missing)}: run their build_cases.py first")
    if a.synid:
        run_synid(benches, a.synid, a.force, a.dry_run)
    skip = lambda t: any(t.startswith(x[:-1]) if x.endswith("*") else t == x for x in a.skip)  # noqa: E731
    jobs = plan(benches, [t for t in a.tool or sorted(TOOLS) if not skip(t)], a.force)
    for b, args, label in jobs:
        print(f"{label:34} {b.name}", flush=True)
    if a.dry_run or not jobs:
        print(f"{len(jobs)} runs to make")
        return 0

    def go(job):
        b, args, label = job
        p = subprocess.run([sys.executable, str(HERE / "external.py"), str(b), *args], capture_output=True, text=True)
        return label, b.name, p.returncode, (p.stdout.strip().splitlines() or [""])[-1] or p.stderr.strip()[-300:]

    failed = 0
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for label, bench, rc, msg in ex.map(go, jobs):
            failed += rc != 0
            print(f"{'ok ' if rc == 0 else 'ERR'} {bench}: {msg}", flush=True)
    print(f"{len(jobs) - failed}/{len(jobs)} runs made; then: python3 tools/leaderboard.py")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
