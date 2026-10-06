# bench-rpgle — archived `.rpgle` files, drawn from the archive with weights

Part of [synid-bench](../../README.md). **760 `.rpgle` files archived by
[Software Heritage](https://www.softwareheritage.org)**, drawn uniformly from the
13,002 `.rpgle` contents of the archive, with real file names, origins and
population weights. Labels come from an LLM judge (**silver**): no human checked
them. The cases come from the `.rpgle` extension study of
[PL-ultimate-llm](https://github.com/acherm/PL-ultimate-llm) (branch
`swh-evidence-v1`, commit `274fa4cc8`, `docs/rpgle_swh_study.md`).

`.rpgle` is ILE RPG (RPG IV), IBM i's business language, and the extension is
clean: 99 % of the files are RPG. The benchmark asks two things: does an
identifier recognise RPG *from its content* (no other benchmark has RPG beyond a
handful of samples), and does it notice the few files that are not RPG (DDS, REXX,
data) although their name says `.rpgle`?

## Where the files and labels come from

- **Population and sample.** The study's population table lists the 13,002
  unique `.rpgle` contents of the archive and their origins (graph-derived). Its
  frame E1 is a uniform random sample of 1,000 of them (seed 5), fetched from
  Software Heritage by sha1_git.
- **Labels.** Each file was labelled by Claude Sonnet 4.6 (OpenRouter,
  temperature 0, structured output, schema `rpgle-judge/1`: content type, whether
  it is a programming language, which language if not RPG, source format, unit
  kind…). The judge saw the bytes, the file name and the study's mechanical
  indicators. The expected language is derived from its verdict: RPG source or
  copy member → `RPGLE`; another language → that language (`REXX`, `DDS`); data
  or documentation → `Text`.
- **Held out from the rules.** The study's hand-written rules (`tools/rpgle/reclassify.py`)
  were frozen after reading the judge's labels on 326 files (the tuning split);
  bench-rpgle keeps only uniform-sample files judged *after* the freeze. The
  rules' answer to "is it RPG?" is recorded beside the judge's in `reference`
  and as a tag: they agree on 725 cases and disagree on 35 (all 35: the judge
  says RPG, the rules see no RPG signal — small fragments, unusual layouts). The
  35 are kept and tagged `judge-rules-disagree`, not left out: leaving them out
  would keep only the files simple rules recognise.
- **Left out** of the 1,000: the 230 files of the tuning split, 4 files that are
  not text (never judged), 5 the judge called `ambiguous` (two RPG III programs,
  a tutorial, preprocessor directives, a snippet) and 1 low-confidence verdict.
- **Weights.** `weight` = the label's share of the uniform sample × 13,002 / the
  number of cases with that label (post-stratification): RPGLE 16.96, the others
  13.0. The weighted accuracy estimates the accuracy on `.rpgle` contents in the
  archive (version history included: one content per archived byte-state).
- **Names.** `filename` is the archived file name; the one name that contains
  the label (`FREERPG1-RPGLE_Free.pgm.rpgle`) is run as `source.rpgle` (tag
  `renamed`, original in `path`). `qualified_swhid` carries the origin and the
  path from the study's origin table; the path is omitted in 18 cases where the
  table's path names another file. The contents are archived: the study fetched
  each from Software Heritage by sha1_git, and a spot check of two per benchmark
  with the public API (2026-10-03) returned them.
- **Files** are stored in `files/<sha1_git>` (8.6 MB), checked against their
  sha1_git. They are copies of publicly archived files, each under the licence of
  its origin repository.

**Accepted answers.** `accept` = the expected Linguist name and its aliases
(`RPGLE;ile rpg;sqlrpgle`). RPG IV's three source formats — fixed-format
(column-oriented specifications), hybrid-free (`/free` blocks) and fully-free
(`**FREE` on line 1) — are one language for Linguist: they are tags, and RPGLE is
right for all three. DDS has no Linguist name: its expected name is `DDS`, so
that a future identifier gets credit. `labels.csv` maps the study's labels to
Linguist's names (synonyms only; DDS: none).

## Composition

| expected | files | weight each |
|---|---:|---:|
| RPGLE | 755 | 16.96 |
| DDS (IBM i display file description) | 2 | 13.0 |
| Text (a token list, a data member) | 2 | 13.0 |
| REXX | 1 | 13.0 |

| tag | files | what |
|---|---:|---|
| `fixed-format` / `hybrid-free` / `fully-free` | 293 / 283 / 149 | the source format, decided by the study's indicator (`**FREE` directive, column-6 specifications); 30 RPGLE files have none |
| `tooling-repo` | 156 | from jariko, antlr4-rpgle or rpgleparser: test fixtures of RPG parsers and an interpreter |
| `copy-member` | 141 | a `/copy` member: declarations only (prototypes, constants) |
| `judge-rules-disagree` | 35 | the judge says RPG, the rules do not |
| `embedded-sql` | 13 | `EXEC SQL` |
| `non-utf8` | 12 | bytes that are not UTF-8 |
| `tiny` | 10 | fewer than three lines |
| `renamed` | 1 | the archived name contains the label |

171 repositories; the largest (jariko, an RPG interpreter's test suite) has 130 files.

## Strengths and weaknesses

- **Strengths.** Drawn uniformly from the archive, with weights: the score is an
  estimate for `.rpgle` files as they are archived, not for a curated set. Real
  names and repositories. A legacy language no other benchmark covers, in its
  three source formats. Held out from the study's rules.
- **Weaknesses.** One LLM judge labelled every file, and it saw the rules'
  indicators; nobody checked the labels. LLM labels may favour LLM entries (Jev
  agrees with the same kind of reader). 755 of 760 files are RPGLE: an identifier
  that trusts the extension scores 99 %; the benchmark discriminates *without*
  the name (content-only runs) and on the five files that are not RPG. One
  extension; three parser repositories hold a fifth of the files.
- **Home turf.** PL-ultimate-llm's candidates for the Jev cascade include what
  the study observed in this population (here only RPGLE, also Linguist's claim);
  see `contamination.json`. The study's rules were frozen before these files were
  judged.

## Build and run

```bash
python3 benchmarks/bench-rpgle/build_cases.py            # needs PL-ultimate-llm at 274fa4cc8 ($PL_ULTIMATE_LLM)
python3 benchmarks/bench-rpgle/export_reference_runs.py  # the study's rules and Jev's stored decisions (no API call)
python3 tools/run.py benchmarks/bench-rpgle --synid path/to/synid --label mytest
python3 tools/external.py benchmarks/bench-rpgle --tool linguist
SYNID=path/to/synid benchmarks/bench-rpgle/reproduce.sh   # everything
```

`build_cases.py` reads the study's reports, worklist, tuning split and origin
table from PL-ultimate-llm's git at commit `274fa4cc8` (shared code:
`tools/study_cases.py`), so a rerun gives the same `cases.csv`; the bytes come
from the checkout's cache, else from the Software Heritage API (`$SWH_TOKEN`
optional). Scoring is the collection's (`tools/score.py`): one answer, in
`accept`. All cases are silver: `tools/score.py` prints the weighted accuracy for
gold only; the leaderboard (`tools/leaderboard.py`) weights every benchmark that
has weights.

## Results

> Figures in this README come from the runs made when the benchmark was built (2026-10-03). Entries were rerun since (pinned images, updated name mappings) and Jev was added: [LEADERBOARD.md](LEADERBOARD.md), regenerated from the stored runs, is the reference.

Every run of 2026-10-03 (Synid binaries `48c3c45` and `9bc1c32`; the other identifiers in their
pinned images, `tools/external.py`; the study's rules and Jev's decisions exported from the study,
no API call). Entries with the same score on the same cases are grouped.

| entries | right | accuracy | weighted to the population |
|---|---:|---:|---:|
| Chroma 2.27.0; GitHub Linguist 7.30.0; GitHub Linguist 8.0.0; GitHub Linguist 9.7.0; Jev 1.13, study's 63 labels, with file name; Neovim 0.12.5 filetype; Synid 48c3c45; Synid 48c3c45, comment off; Synid 48c3c45, hyplyclassifier off; Synid 48c3c45, hyplyheuristics off; Synid 48c3c45, pygmentsheuristics off; Synid 9bc1c32; go-enry 2.8.9; go-enry 2.9.6; linguist-js 3.0.4 | 755/760 | 99.3 % | 99.5 % |
| Jev 1.13, study's 63 labels, content only | 755/760 | 99.3 % | 99.5 % |
| Hand-written .rpgle rules (frozen before these files) | 720/760 | 94.7 % | 94.9 % |
| Magika 0.5.1; Magika 1.0.3; Rouge 5.1.0; file 5.46 (libmagic) | 2/760 | 0.3 % | 0.2 % |
| Synid 48c3c45, content only | 1/760 | 0.1 % | 0.1 % |
| GitHub Linguist 9.7.0, content only; Guesslang 2.2.1; Hyperpolyglot a55a3b5; Hyperpolyglot a55a3b5, content only; Pygments 2.14.0; Pygments 2.19.2; Pygments 2.21.0; Pygments 2.21.0, content only; Universal Ctags 6.2.1; cloc 2.10; flourite 1.3.0; gengo 0.15.0; go-enry 2.9.6, content only; highlight.js 11.12.0; ohcount 4.0.0 (Debian 4.0.0-5); scc 4.1.0; tokei 15.0.0; vscode-languagedetection 1.0.23 | 0/760 | 0.0 % | 0.0 % |

- **With the file name the benchmark is solved by the extension.** Every identifier that knows
  `.rpgle` — Synid `48c3c45` and `9bc1c32` (and `48c3c45` with any one strategy off), GitHub
  Linguist 7.30.0 / 8.0.0 / 9.7.0, go-enry, linguist-js, Chroma, Neovim — answers RPGLE on all 760 files:
  right on the 755 RPG files, the 35 the rules miss included, and wrong on the five that are not
  RPG (two DDS display files, a REXX program, two data members).
- **No identifier recognises RPG from its content**, except Jev with the study's labels. Without
  the name, Synid `48c3c45` is right once in 760 (`Text` on 517, Slim 84, Stata 55, Assembly 35);
  Linguist, go-enry and Hyperpolyglot give no answer; Pygments names GDScript (221), Carbon (161),
  scdoc (128); Guesslang, which has no RPG, says Pascal (121) or COBOL (107); Magika says `Text`
  (468), MATLAB (75), C (65); Rouge says `Text` on every file, libmagic on 745. Jev, asked among 63 labels designed
  for these studies (`rpg` among them), gets 755/760 from the content alone — the same score as
  with the name; its five misses are the two DDS files, the REXX program (IBM CL), a data member
  and one RPG file (BASIC).
- **Tools without RPGLE** give no answer at all: Hyperpolyglot `a55a3b5` (2023 data), Pygments
  2.14–2.21, cloc, ctags, gengo, ohcount, scc, tokei.
- The study's rules, frozen before these files, never name a wrong language: they answer RPGLE on
  720 files and abstain on 40 (the 35 fragments the judge calls RPG, and the five files
  that are not RPG, which they cannot name).
- The source format does not matter to the identifiers that answer RPGLE (they read the
  extension); for content-only runs, every format fails alike.

Not run here: hf-codeberta, hf-framebyframe, hf-philomath and plangrec (slow transformer or memory-heavy tools, left to a later throttled batch).
