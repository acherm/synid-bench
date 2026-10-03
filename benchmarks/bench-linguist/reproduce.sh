#!/usr/bin/env bash
# Rebuild bench-linguist and every entry of its leaderboard from scratch.
# Needs: git, Python 3 with PyYAML, Docker (other tools, pinned images), a Synid build (SYNID=path),
# optionally an OpenRouter key (Jev, ~$3.3 per variant) and Ollama (local LLM).
set -euo pipefail
cd "$(dirname "$0")/../.."
B=benchmarks/bench-linguist
: "${SYNID:?set SYNID to a synid binary (e.g. .../swh-syntax-identification/target/release/synid)}"

python3 $B/build_cases.py                                    # cases.csv + files/, pinned revisions

# Synid (the version SYNID points to)
python3 tools/run.py $B --synid "$SYNID" --label head-default
python3 tools/run.py $B --synid "$SYNID" --label head-content-only --content-only
for s in pygmentsheuristics comment hyplyclassifier hyplyheuristics; do
  python3 tools/run.py $B --synid "$SYNID" --label head-no-$s --disable $s
done

# other identifiers, each in its pinned Docker image (tools/external/<tool>/)
for t in linguist enry hyperpolyglot cloc pygments magika guesslang; do
  python3 tools/external.py $B --tool $t --labels
done
python3 tools/external.py $B --tool pygments --content-only
python3 tools/external.py $B --tool linguist --content-only
python3 tools/external.py $B --tool enry --content-only

# lightweight LLMs (optional)
if [ -n "${OPENROUTER_API_KEY:-}" ] || [ -f ~/.openrouter_env ]; then
  python3 tools/jev_linguist.py $B --workers 8
  python3 tools/jev_linguist.py $B --workers 8 --with-filename
  python3 tools/jev_linguist.py $B --workers 8 --label-set study63                   # ~$0.39
  python3 tools/jev_linguist.py $B --workers 8 --label-set study63 --with-filename
  # candidates from PL-ultimate-llm (tools/data/pl_candidates.json; refresh with tools/export_pl_candidates.py)
  python3 tools/jev_cascade.py $B --workers 8                                         # ~$0.62
  python3 tools/jev_cascade.py $B --workers 8 --content-only
fi
# an open decision model, locally: llama.cpp with the /v1/systemone API (commit a4cb4c6 or later)
if [ -n "${LLAMA_SERVER:-}" ] && [ -n "${KEV_GGUF:-}" ]; then   # Kev-4B-Q8_0.gguf from huggingface.co/ggml-org/Kev-4B-GGUF
  "$LLAMA_SERVER" -m "$KEV_GGUF" --port 8091 -c 65536 -b 4096 -ub 1024 -fa on -ngl 99 & srv=$!
  until curl -s 127.0.0.1:8091/health | grep -q ok; do sleep 2; done
  python3 tools/jev_linguist.py $B --endpoint http://127.0.0.1:8091/v1/systemone --model kev-4b-q8_0 \
      --name "Kev-4B Q8_0 (local, llama.cpp)" --label kev-linguist --workers 1 --shuffle   # ~13 s per file
  kill $srv
fi
if curl -s localhost:11434/api/version >/dev/null; then
  ollama pull starcoder2:3b && python3 tools/ollama_llm.py $B --model starcoder2:3b --name StarCoder2-3B
fi

python3 tools/coverage.py $B --synid "$SYNID"
python3 tools/history.py $B
python3 tools/leaderboard.py
