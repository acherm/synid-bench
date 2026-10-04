# bench-hljs — highlight.js' auto-detection tests

The **191 auto-detection test files of [highlight.js](https://github.com/highlightjs/highlight.js/tree/fc3f06392f189354eed922973635ab9e9268b983/test/detect)**
(`test/detect/<language>/default.txt`, and a few others), each labelled by its directory: **185
languages**, one file each for nearly all. They are run **without a name** — the files are all
`default.txt` or a description of the test — so every identifier is judged on the content alone.
It is highlight.js' *home turf*: running every identifier on it shows how much a benchmark favours
the tool it was built from. Siblings: [bench-pygments](../bench-pygments/README.md),
[bench-rouge](../bench-rouge/README.md).

| | |
|---|---|
| cases | 191 files, no names; 152 files in 146 languages Linguist has, 39 in 39 languages it does not |
| labels | the directory, a highlight.js language id, resolved to the `name` highlight.js reports (`src/languages/<id>.js`), written as Linguist's name when Linguist has the language ([labels.csv](labels.csv)); a case is right when the answer is that language, one of its Linguist aliases, or highlight.js' name, display name or id |
| source | highlight.js at [`fc3f063`](https://github.com/highlightjs/highlight.js/tree/fc3f06392f189354eed922973635ab9e9268b983) (2026-08-30), BSD-3-Clause |
| files | **not stored here**: `build_cases.py` fetches them at the pinned commit and checks each against its git blob id |

```bash
python3 benchmarks/bench-hljs/build_cases.py          # fetch the files (and rebuild cases.csv, identical)
python3 tools/run.py benchmarks/bench-hljs --synid path/to/synid --label mytest
python3 tools/score.py benchmarks/bench-hljs/results/mytest.jsonl \
    --baseline benchmarks/bench-hljs/baselines/48c3c45-default.jsonl
benchmarks/bench-hljs/reproduce.sh                    # every entry (SYNID=path/to/synid)
```

`build_cases.py` makes a shallow, blob-less, sparse fetch of the pinned commit into `.work/` (or
`--cache DIR`, or `$SYNID_BENCH_CACHE`), plus Linguist `76f88c6` and Hyperpolyglot `a55a3b5` (to tag
files that are Linguist samples: none is). A rerun gives an identical `cases.csv`.

## Whose home turf

**highlight.js', more than any other benchmark here is anyone's.** These files are not examples of
lexing but of *detection*: from 2014 (`test/detect/`) to March 2024 the test suite required
`hljs.highlightAuto` to name every one of them as its directory's language, so grammars and their
relevance scores were tuned until all passed. In commit
[`105a11a`](https://github.com/highlightjs/highlight.js/commit/105a11a13eedbf830c0e80cc052028ceb593837f)
(2024-03-04) the test was commented out — "We are deemphasizing auto-detect - it was never great …
we will no longer fail the test suite based on any auto-detect issues" — and the files were kept; two
were added since. No file is a Linguist sample; one (Lasso) is also a Rouge sample.

The content is archived in Software Heritage (2 of 2 sampled `swh:1:cnt` found, and the revision
`fc3f063`, 2026-10-03).

## Labels: what is kept, and the crosswalk

**Kept: languages**, with the rule of bench-pygments: a language Linguist has (of any type), or
another programming, markup, data, configuration, template or grammar language. **Left out (8 files):**
REPL transcripts with no Linguist language (`clojure-repl`, `erlang-repl`, `node-repl`), the output of
a program (`accesslog`, `profile`, `subunit`, `tap`) and `plaintext`. Kept: `julia-repl` (Julia REPL),
`python-repl` (Python console), `shell` (ShellSession).

**The label** is the `name` highlight.js reports for the directory's language (its id when the
grammar has none: `php`, `python-repl`, `dsconfig`); the header's display name and the id are accepted
too. `json5` is not a language of its own (an alias of `json`): its label is JSON5, Linguist's name.

**Crosswalk** ([labels.csv](labels.csv), name → Linguist name): synonyms only, as in
`tools/external/*/names.csv` (and in agreement with `tools/external/hljs/names.csv`). 122 by the same
name, 11 by a Linguist alias (Bash → Shell, Coq → Rocq Prover, ERB → HTML+ERB), 13 by hand
(Batch file (DOS) → Batchfile, Caché Object Script → ObjectScript, Intel x86 Assembly → Assembly,
PostgreSQL — "PostgreSQL and PL/pgSQL" — → PLpgSQL), 39 none. Two labels are families and accept every
member: `HTML, XML` → HTML;XML (3 files) and `TOML, also INI` → INI;TOML. Not mapped: Arduino (a C++
dialect for Linguist), ARM/AVR/MIPS Assembly, C/AL (Linguist has its successor AL), VBScript in HTML.

## Strengths and weaknesses

- **Content only**, by construction: no identifier can lean on a name or an extension. This is the
  benchmark where content strategies — classifiers, neural guessers, grammar relevance — are compared
  on equal terms.
- **Breadth without a dominant language**: 185 languages, at most 3 files each; 39 files in languages
  Linguist lacks. Independent of Linguist: no file is one of its samples.
- **highlight.js' home turf**: ten years of tests required highlight.js to get each file right.
- **Snippets, not files**: a median of 21 non-blank lines, written to show a grammar's features (often
  every keyword in a few lines), not code from projects. 5 are `tiny`.
- **One file per language**: a per-language figure is a single file.

## Composition

| | files |
|---|---:|
| Linguist type programming / data / markup / prose | 120 / 16 / 14 / 2 |
| not in Linguist | 39 |
| labels with 1 / 2 / 3 files | 181 / 2 (Go, Ruby) / 2 (JavaScript, HTML) |
| non-blank lines: 10th percentile / median / 90th | 10 / 21 / 46 |

| tag | files | |
|---|---:|---|
| `in-linguist` / `not-in-linguist` | 152 / 39 | the label maps to a Linguist language, or not |
| `tiny` | 5 | under 5 non-blank lines |

No file is run with a name: `ambiguous-ext` does not apply, and tools that answer from the name only
(cloc, scc, tokei, gengo: `"needs_name": true`) are not run. For tools without a `--content-only`
flag the default run already sees no name, so no separate content-only run is made; for those with one,
both runs are kept (Pygments' default, `guess_lexer_for_filename`, gives no answer without a name).

## Findings (2026-10-03)

**The strongest home-turf effect of the three, and it fades once the tests stop.**

- **highlight.js 11.12.0 ranks first: 135 / 191 (70.7 %)**, more than twice the next (Magika 1.0.3,
  33.0 %; the ModernBERT classifier FrameByFrame 32.5 %; Guesslang 27.2 %; VS Code's detector 24.6 %).
  On the 39 files outside Linguist's languages, it is right on 32; no other tool on more than 1.
- **While the tests ran, it was near perfect.** highlight.js 11.9.0 (2023-10-09, the last release
  before the detection test was dropped), run the same way in a scratch image (not a leaderboard
  entry): **183 / 191**; its 8 misses are the 4 family files (below), Elixir answered Ruby,
  `.properties` answered LiveScript, and two tests added after its release (JSON5 in 2025, answered
  PostgreSQL; Odin, whose grammar came in August 2026 — after 11.12.0 too — answered Go).
  11.12.0 (2026-08-12) loses 49 of those files and gains 1: **Dart takes 25 files and DNS Zone 20**
  — two grammars whose relevance now outbids most others.
- **Every tool built around names collapses**: the Linguist family 1.6 %, Synid 5.8 % (5.2 % with
  `--content-only`), Rouge 2.1 %, Chroma 1.6 %, Pygments 9.4 % with `guess_lexer`. Content-only
  identifiers do better but stay far from the home tool: Magika and the neural classifiers (Guesslang,
  VS Code's detector, three Hugging Face models) know 6 to about 200 labels, and almost none of the 39
  languages outside Linguist.
- **Four of highlight.js' misses are labels, not mistakes**: on the `xml` and `ini` files it answers
  its own family names `HTML, XML` and `TOML, also INI`; `tools/external/hljs/names.csv` maps each to
  two Linguist languages, which `tools/external.py` counts as undecided.
- **Synid is not deterministic here**: across runs, one HTML file (`xml/default.txt`) comes out HTML
  or ERB (5 runs of 48c3c45: HTML twice, ERB three times); the baseline has HTML, the content-only
  entry ERB — hence 11 vs 10.

| entry | run | right | precision | `in-linguist` | `not-in-linguist` | `tiny` |
|---|---|---:|---:|---:|---:|---:|
| highlight.js 11.12.0 | `ext-hljs` | **135/191** (70.7 %) | 72.2 % | 103/152 | 32/39 | 2/5 |
| Magika 1.0.3 | `ext-magika` | **63/191** (33.0 %) | 43.8 % | 63/152 | 0/39 | 2/5 |
| FrameByFrame/programming-language-identification-100plus da6a18b | `ext-hf-framebyframe` | **62/191** (32.5 %) | 32.5 % | 61/152 | 1/39 | 0/5 |
| Guesslang 2.2.1 | `ext-guesslang` | **52/191** (27.2 %) | 27.2 % | 52/152 | 0/39 | 1/5 |
| vscode-languagedetection 1.0.23 | `ext-vscode-ld` | **47/191** (24.6 %) | 35.6 % | 47/152 | 0/39 | 0/5 |
| Magika 0.5.1 | `ext-magika-v0.5` | **29/191** (15.2 %) | 28.4 % | 29/152 | 0/39 | 2/5 |
| flourite 1.3.0 | `ext-flourite` | **28/191** (14.7 %) | 14.9 % | 28/152 | 0/39 | 2/5 |
| philomath-1209/programming-language-identification 9090d38 | `ext-hf-philomath` | **27/191** (14.1 %) | 14.1 % | 26/152 | 1/39 | 1/5 |
| Pygments 2.21.0, content only | `ext-pygments-content-only` | **18/191** (9.4 %) | 9.5 % | 18/152 | 0/39 | 2/5 |
| Pygments 2.19.2, content only | `ext-pygments-v2.19-content-only` | **18/191** (9.4 %) | 9.5 % | 18/152 | 0/39 | 2/5 |
| Pygments 2.14.0, content only | `ext-pygments-v2.14-content-only` | **17/191** (8.9 %) | 9.3 % | 17/152 | 0/39 | 2/5 |
| file 5.46 (libmagic) | `ext-libmagic` | **13/191** (6.8 %) | 23.6 % | 13/152 | 0/39 | 1/5 |
| Synid 48c3c45 | `48c3c45-default` | **11/191** (5.8 %) | 10.9 % | 11/152 | 0/39 | 0/5 |
| Synid 48c3c45, content only | `48c3c45-content-only` | **10/191** (5.2 %) | 9.9 % | 10/152 | 0/39 | 0/5 |
| huggingface/CodeBERTa-language-id 67e92a9 | `ext-hf-codeberta` | **10/191** (5.2 %) | 5.2 % | 10/152 | 0/39 | 1/5 |
| Synid 9bc1c32 | `9bc1c32-default` | **8/191** (4.2 %) | 9.4 % | 8/152 | 0/39 | 0/5 |
| Neovim 0.12.5 filetype | `ext-nvim` | **6/191** (3.1 %) | 85.7 % | 6/152 | 0/39 | 0/5 |
| Neovim 0.12.5 filetype, content only | `ext-nvim-content-only` | **6/191** (3.1 %) | 85.7 % | 6/152 | 0/39 | 0/5 |
| ohcount 4.0.0 (Debian 4.0.0-5) | `ext-ohcount` | **5/191** (2.6 %) | 45.5 % | 5/152 | 0/39 | 1/5 |
| Rouge 5.1.0 | `ext-rouge` | **4/191** (2.1 %) | 66.7 % | 4/152 | 0/39 | 0/5 |
| Rouge 5.1.0, content only | `ext-rouge-content-only` | **4/191** (2.1 %) | 66.7 % | 4/152 | 0/39 | 0/5 |
| GitHub Linguist 8.0.0 | `ext-linguist-v8` | **3/191** (1.6 %) | 75.0 % | 3/152 | 0/39 | 0/5 |
| go-enry 2.9.6 | `ext-enry` | **3/191** (1.6 %) | 75.0 % | 3/152 | 0/39 | 0/5 |
| Chroma 2.27.0 | `ext-chroma` | **3/191** (1.6 %) | 3.6 % | 3/152 | 0/39 | 0/5 |
| GitHub Linguist 9.7.0 | `ext-linguist` | **3/191** (1.6 %) | 75.0 % | 3/152 | 0/39 | 0/5 |
| go-enry 2.8.9 | `ext-enry-v2.8` | **3/191** (1.6 %) | 75.0 % | 3/152 | 0/39 | 0/5 |
| Hyperpolyglot a55a3b5 | `ext-hyperpolyglot` | **3/191** (1.6 %) | 75.0 % | 3/152 | 0/39 | 0/5 |
| GitHub Linguist 7.30.0 | `ext-linguist-v7` | **3/191** (1.6 %) | 75.0 % | 3/152 | 0/39 | 0/5 |
| Chroma 2.27.0, content only | `ext-chroma-content-only` | **3/191** (1.6 %) | 3.6 % | 3/152 | 0/39 | 0/5 |
| linguist-js 3.0.4 | `ext-linguist-js` | **3/191** (1.6 %) | 75.0 % | 3/152 | 0/39 | 0/5 |
| Universal Ctags 6.2.1 | `ext-ctags` | **1/191** (0.5 %) | 100.0 % | 1/152 | 0/39 | 0/5 |
| Pygments 2.19.2 | `ext-pygments-v2.19` | **0/191** (0.0 %) | — | 0/152 | 0/39 | 0/5 |
| Pygments 2.14.0 | `ext-pygments-v2.14` | **0/191** (0.0 %) | — | 0/152 | 0/39 | 0/5 |
| Pygments 2.21.0 | `ext-pygments` | **0/191** (0.0 %) | — | 0/152 | 0/39 | 0/5 |

## Home turf across the benchmarks

Each benchmark's own tool in bold (bench-linguist figures from its entries as they stand; highlight.js
has not been run there). A tool tops its own benchmark when it was tested there on the task measured —
detection with a name for Pygments and Linguist, detection from content for highlight.js — and not
when its tests only lexed the files and the files carry no name (Rouge). Pygments' and Linguist's leads
go with the name: from the content only, Pygments is at 7–11 % everywhere.

| entry | bench-linguist | bench-pygments | bench-hljs | bench-rouge |
|---|---:|---:|---:|---:|
| GitHub Linguist 9.7.0 | **99.5 %** | 67.3 % | 1.6 % | 2.6 % |
| Pygments 2.21.0 | 32.3 % | **93.4 %** | 0.0 % | 0.0 % |
| Pygments 2.21.0, content only | 10.2 % | 10.5 % | 9.4 % | 7.5 % |
| highlight.js 11.12.0 (content only) | 8.5 % | 13.8 % | **70.7 %** | 18.7 % |
| Rouge 5.1.0 | 26.8 % | 38.3 % | 2.1 % | **6.4 %** |
| Synid 48c3c45 | 76.6 % | 82.1 % | 5.8 % | 4.0 % |
| Magika 1.0.3 (content only) | 25.3 % | 18.8 % | 33.0 % | 27.5 % |


## Files

| file | |
|---|---|
| `cases.csv` | one row per file: path, git blob id, SWHID, expected language, accepted names, Linguist type, tags |
| `labels.csv` | the crosswalk: highlight.js name → Linguist name, how, language id, files |
| `build_cases.py` | fetches highlight.js, Linguist and Hyperpolyglot at pinned commits, writes `cases.csv`, `labels.csv`, `files/` |
| `card.json`, `contamination.json` | the benchmark card; the entries built or tuned on these files |
| `baselines/`, `entries/` | Synid versions (default configuration); other configurations and other identifiers |
| `reproduce.sh` | rebuilds every entry |
