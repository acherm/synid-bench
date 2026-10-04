#!/usr/bin/env bash
# Rebuild bench-pygments and every entry of its leaderboard from scratch.
# Needs: git, Python 3 with PyYAML, Docker (other tools, pinned images), a Synid build (SYNID=path).
set -euo pipefail
cd "$(dirname "$0")/../.."
B=benchmarks/bench-pygments
: "${SYNID:?set SYNID to a synid binary (e.g. .../swh-syntax-identification/target/release/synid)}"

python3 $B/build_cases.py                                    # cases.csv, labels.csv + files/, pinned revisions

# Synid (the version SYNID points to)
python3 tools/run.py $B --synid "$SYNID" --label head-default
python3 tools/run.py $B --synid "$SYNID" --label head-content-only --content-only

# other identifiers, each in its pinned Docker image (tools/external/<tool>/): every tool, with the file name
# and without it where that applies — tools/run_all.py decides (not run where it would not apply)
python3 tools/run_all.py --bench bench-pygments --force --jobs 3

python3 tools/coverage.py $B --synid "$SYNID"
python3 tools/history.py $B
python3 tools/leaderboard.py
