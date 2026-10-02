# bench-m — `.m` files with human-checked languages

Part of [synid-bench](../../README.md). **54 archived `.m` files with
human-checked languages**, to assess
[Software Heritage](https://www.softwareheritage.org)'s syntax identifier, Synid,
version after version: *is this version better or worse than the last one, on
which files, and on which known failure triggers?*

Three properties guide it:

- **Ground truth you can trust.** Every label comes from a blind human review
  (the reviewer saw the file and its provenance, no machine label), and two
  independent LLM judges (Claude Sonnet 4.6, Gemini 3.8 Flash) agree with the
  human on all 54 files. Files labelled by the judges alone are left out.
- **Diverse.** 8 languages from 50 repositories, chosen by a stratified random
  draw that over-samples the files on which identifiers disagree — the hard
  cases — and covering the failure triggers below.
- **Small.** 54 files, 1.1 MB; a run takes well under a second; every failure
  can be read.

`.m` is a hard, realistic test for any identifier: it is shared by
Objective-C, MATLAB/Octave, Wolfram/Mathematica, Mercury, MUMPS, Magma, and
more. The cases come from the `.m` extension study of
[PL-ultimate-llm](https://github.com/acherm/PL-ultimate-llm) (branch
`swh-evidence-v1`, `docs/m_swh_study.md`).

## Composition

| language (expected) | files |
|---|---:|
| MATLAB / Octave | 32 (29 + 3) |
| Objective-C | 8 |
| Wolfram / Mathematica | 4 |
| Magma | 4 |
| MUMPS (M) | 2 |
| Mercury | 2 |
| C (misnamed `.m`) | 1 |
| not code | 1 |

| failure trigger (tag) | files |
|---|---:|
| `comment-free-matlab` — no line starting with `%`, `!` or `function` | 10 |
| `out-of-candidates` — not among Synid's candidates for `.m` (Magma, C) | 5 |
| `objc-format-string` — `%` inside `@"…"` | 4 |
| `non-utf8` — bytes that are not UTF-8 | 2 |
| `comment-free-objc` — Objective-C without `//` or `/*` | 2 |
| `tiny` — fewer than three lines | 1 |

## Files

| path | what |
|---|---|
| `cases.csv` | one row per file: sha1_git, file name, qualified SWHID (origin + path), expected language, the Synid answers that count as right (`accept`), provenance, population weight, tags |
| `files/<sha1_git>` | the files themselves |
| `baselines/` | runs of known Synid versions |
| `HISTORY.md` | every baseline side by side (`tools/history.py`) |
| `build_cases.py` | builds the cases from the study (needs a PL-ultimate-llm checkout); only to release a new version |
| `assessment/` | the assessment of Synid `9bc1c32` on these files, with the mechanism behind each failure |

The files are copies of publicly archived source files, kept for
reproducibility; each keeps the licence of its origin repository (see its
qualified SWHID). They can also be fetched from Software Heritage by sha1_git:
`https://archive.softwareheritage.org/api/1/content/sha1_git:<sha1_git>/raw/`.

## Use

```bash
# build Synid — its repository (SWH GitLab, teams/codecommons/swh-syntax-identification) is access-restricted
(cd path/to/swh-syntax-identification && cargo build --release --bin synid)

# from the root of synid-bench
python3 tools/run.py benchmarks/bench-m --synid path/to/swh-syntax-identification/target/release/synid --label mytest
python3 tools/score.py benchmarks/bench-m/results/mytest.jsonl \
    --baseline benchmarks/bench-m/baselines/48c3c45-default.jsonl --report benchmarks/bench-m/results/mytest.md
```

Python 3.10+, no dependencies. The tools are shared by the collection
(`tools/`, see the top-level README). `run.py` generates the configuration with the
binary itself (`synid info generate-config`), so it follows Synid's options
across versions; it turns off the networked `linguist-api` strategy (the
benchmark measures what Synid infers from a file's name and bytes).
`--disable <strategy>` runs an ablation.

**Scoring.** A case is right when Synid gives exactly one syntax and it is in
`accept`: MATLAB for MATLAB and Octave files (Synid has no Octave), `Text` only
for the file that is not code; names Synid cannot produce yet (Magma, C) are
accepted so that a future version gets credit. Several syntaxes = undecided.
The weighted accuracy re-weights the stratified draw to the population of `.m`
files in Software Heritage.

**A new Synid version.** Run it and score it against the latest baseline; if it
is accepted, copy its run into `baselines/` and run `tools/history.py`.

## Results so far

| Synid | right | weighted | comment-free MATLAB | comment-free Objective-C | non-UTF-8 | out of candidates |
|---|---:|---:|---:|---:|---:|---:|
| `9bc1c32` (2026-06-15) | 32/54 | 81.2 % | 0/10 | 1/2 | 0/2 | 0/5 |
| `48c3c45` (2026-10-02) | 33/54 | 86.1 % | 0/10 | 2/2 | 0/2 | 0/5 |

When Synid names a language, it is right; its failures are non-answers —
`Text`, the default of the Pygments-heuristics strategy, which pre-empts the
classifier, and *undecided* on non-UTF-8 content. Details:
`assessment/m-9bc1c32.md` and `HISTORY.md`.

## Limits, and growing it

MATLAB dominates (32/54) because the draw follows the archive; Mercury and
MUMPS have two files each, Limbo, MUF and Mason none, and only `.m` is covered.
The benchmark grows the way it was made: files reviewed blind on
PL-ultimate-llm's review page — targeting rare languages and other extensions
(its COBOL, `.fsf` and `.rpgle` studies) — released as a new version
(`bench-m/2`) with `build_cases.py`. Cases are frozen within a version so
that results stay comparable.
