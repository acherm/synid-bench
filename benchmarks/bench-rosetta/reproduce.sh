#!/usr/bin/env bash
# Rebuild bench-rosetta and every entry of its leaderboard from scratch.
# Needs: git, Python 3 with PyYAML, Docker (other tools, pinned images), a Synid build (SYNID=path; SYNID_OLD for
# the previous baseline, optional).
set -euo pipefail
cd "$(dirname "$0")/../.."
B=benchmarks/bench-rosetta
: "${SYNID:?set SYNID to a synid binary (e.g. .../swh-syntax-identification/target/release/synid)}"

python3 $B/build_cases.py                                    # cases.csv + labels.csv + files/, pinned revisions

# Synid (the version SYNID points to), with the file name and without
python3 tools/run.py $B --synid "$SYNID" --label head-default
python3 tools/run.py $B --synid "$SYNID" --label head-content-only --content-only
if [ -n "${SYNID_OLD:-}" ]; then python3 tools/run.py $B --synid "$SYNID_OLD" --label old-default; fi

# other identifiers, each in its pinned Docker image (tools/external/<tool>/): every tool, with the file name
# and without it where that applies — tools/run_all.py decides (not run where it would not apply)
python3 tools/run_all.py --bench bench-rosetta --force --jobs 3

python3 tools/coverage.py $B --synid "$SYNID"
python3 tools/history.py $B
python3 tools/leaderboard.py
