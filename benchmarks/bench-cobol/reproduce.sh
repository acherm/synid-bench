#!/usr/bin/env bash
# Rebuild bench-cobol and every entry of its leaderboard from scratch.
# Needs: git, Python 3 with PyYAML, a PL-ultimate-llm checkout holding commit 274fa4cc8 (PL_ULTIMATE_LLM,
# default: a sibling of synid-bench; its local study data and byte cache, else Software Heritage's API),
# Docker (other tools, pinned images), a Synid build (SYNID=path). No paid API is called.
set -euo pipefail
cd "$(dirname "$0")/../.."
B=benchmarks/bench-cobol
: "${SYNID:?set SYNID to a synid binary (e.g. .../swh-syntax-identification/target/release/synid)}"

python3 $B/build_cases.py                                    # cases.csv, labels.csv, files/ (study at 274fa4cc8)
python3 $B/export_reference_runs.py                          # the study's rules and Jev's stored decisions

# Synid (the version SYNID points to)
python3 tools/run.py $B --synid "$SYNID" --label head-default
python3 tools/run.py $B --synid "$SYNID" --label head-content-only --content-only
for s in pygmentsheuristics comment hyplyclassifier hyplyheuristics; do
  python3 tools/run.py $B --synid "$SYNID" --label head-no-$s --disable $s
done

# other identifiers, each in its pinned Docker image (tools/external/<tool>/): every tool, with the file name
# and without it where that applies — tools/run_all.py decides (not run where it would not apply)
python3 tools/run_all.py --bench bench-cobol --force --jobs 3

# Jev with PL-ultimate-llm's candidates (optional, OpenRouter): its candidates for this extension include
# what the study observed in these files (contamination.json)
if [ -n "${OPENROUTER_API_KEY:-}" ] || [ -f ~/.openrouter_env ]; then
  python3 tools/jev_cascade.py $B --workers 8
  python3 tools/jev_cascade.py $B --workers 8 --content-only
fi

python3 tools/coverage.py $B --synid "$SYNID"
python3 tools/history.py $B
python3 tools/leaderboard.py
