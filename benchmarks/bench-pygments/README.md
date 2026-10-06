# bench-pygments — Pygments' example files

The **637 example files of [Pygments](https://github.com/pygments/pygments/tree/156d85fdd18d34427fe893527e71da91dcfb0eb5/tests/examplefiles)**
(`tests/examplefiles/<lexer alias>/<file>`), each labelled by the lexer of its directory: **431 lexers,
428 labels**. It is Pygments' *home turf*, the way [bench-linguist](../bench-linguist/README.md) is
Linguist's: running every identifier on it shows how much a benchmark favours the tool it was built
from. Its siblings are [bench-hljs](../bench-hljs/README.md) and [bench-rouge](../bench-rouge/README.md).

| | |
|---|---|
| cases | 637 files under their real names, in 431 lexers; 461 files in 279 languages Linguist has, 176 in 149 languages it does not |
| labels | the lexer whose alias is the directory name (Pygments' `pygments/lexers/_mapping.py`), written as Linguist's name when Linguist has the language ([labels.csv](labels.csv)); a case is right when the answer is that language, one of its Linguist aliases, or the Pygments lexer name |
| source | Pygments at [`156d85f`](https://github.com/pygments/pygments/tree/156d85fdd18d34427fe893527e71da91dcfb0eb5) (2026-09-27), BSD-2-Clause |
| files | **not stored here**: `build_cases.py` fetches them at the pinned commit and checks each against its git blob id |

```bash
python3 benchmarks/bench-pygments/build_cases.py          # fetch the files (and rebuild cases.csv, identical)
python3 tools/run.py benchmarks/bench-pygments --synid path/to/synid --label mytest
python3 tools/score.py benchmarks/bench-pygments/results/mytest.jsonl \
    --baseline benchmarks/bench-pygments/baselines/48c3c45-default.jsonl
benchmarks/bench-pygments/reproduce.sh                    # every entry (SYNID=path/to/synid)
```

`build_cases.py` makes a shallow, blob-less, sparse fetch of the pinned commit into `.work/` (or
`--cache DIR`, or `$SYNID_BENCH_CACHE`), plus Linguist `76f88c6` (`languages.yml`, the tree of
`samples/`) and Hyperpolyglot `a55a3b5` (the tree of `samples/`). A rerun gives an identical `cases.csv`.

## Whose home turf

**Pygments'.** Its test suite lexes every one of these files and compares the tokens with a stored
golden output (`*.output`, left out here): the lexers were written and fixed against them, and the file
names were chosen by the same maintainers who wrote the lexers' file name patterns. Whether
`analyse_text` — the content guesser — was tuned on them is not known; the tests do not check
guessing. The runs below suggest it was not (content only, Pygments scores the same here as on
bench-linguist).

Others, by blob id ([contamination.json](contamination.json)): 15 files are byte-identical to Linguist
samples that are in Hyperpolyglot's 2023 copy too (tags `linguist-sample`, `seen-in-training`: the
classifiers of Linguist, go-enry, Hyperpolyglot and Synid were trained on them); 5 are inputs of
Chroma's lexer tests. And **Synid's catalogue includes Pygments' lexers** with their file name patterns:
it names 134 of the 176 files in languages Linguist does not have — the taxonomy is its home turf
too, without the files.

The content is archived in Software Heritage (3 of 3 sampled `swh:1:cnt` found, 2026-10-03), but the
revision `156d85f` itself is not yet: the `origin` and `path` qualifiers of `qualified_swhid` point to
a revision the archive does not have today.

## Labels: what is kept, and the crosswalk

**Kept: languages.** A lexer is kept when Linguist 76f88c6 has a language for it (of any type), or,
for the others, when it is a programming, markup, data, configuration, template or grammar language.
**Left out (35 files, 25 lexers):** transcripts of interactive sessions with no Linguist language
(`doscon`, `dylan-console`, `erl`, `gap-repl`, `iex`, `matlabsession`, `nodejsrepl`, `psql`, `psysh`,
`pwsh-session`, `rbcon`, `rconsole`, `sqlite3`, `tcshcon`), the output of a program (`hexdump`, `kmsg`,
`notmuch`, `objdump-nasm`, `output`, `postgres-explain`, `pypylog`, `tap`, `vctreestatus`, `wdiff`),
and plain text (`text`). Sessions and outputs Linguist has a language for stay: `console`
(ShellSession), `pycon` (Python console), `jlcon` (Julia REPL), `pytb`/`py2tb` (Python traceback),
`irc` (IRC log). Also left out: the golden `*.output` files and `conftest.py`.

**Crosswalk** ([labels.csv](labels.csv), Pygments lexer name → Linguist name): synonyms only, as in
`tools/external/*/names.csv`. 235 lexers by the same name, 19 by a Linguist alias (Bash → Shell,
VB.net → Visual Basic .NET), 28 by hand (Nimrod → Nim, TASM → Assembly, Pygments' `Fortran` → Fortran
Free Form since it is the free-form lexer, `Java Server Page` → Java Server Pages although Linguist
lists the singular as an alias of Groovy Server Pages, `MQL` → MQL4;MQL5 as a family), 149 none. A
dialect is not mapped: Arduino (Linguist files `*.ino` under C++), JSX, ClojureScript, PostgreSQL SQL
dialect, Gosu Template, `ca65 assembler` and MIPS keep Pygments' name, and an answer of C++, JavaScript
or Clojure counts as wrong.

**Names.** A file whose name contains its label (`perl_misc.pl`, `glsl.frag`, `docker.docker`) is run
as `example<ext>` (tag `renamed`, 103 files; the original is in `path`), unless the whole name is one
the language is known by in Linguist or Pygments (`Makefile`, `nginx.conf`, `meson.build`). Two pairs
of files have the same content under different names (`syntax_error.py2tb` / `.pytb`).

## Strengths and weaknesses

- **Wide and independent of Linguist**: 431 lexers, 176 files in languages Linguist lacks, only 15
  files from Linguist's samples. Real names chosen by maintainers; 114 files have an extension two or
  more Linguist languages claim (`ambiguous-ext`: `.pl` ×8, `.toc`, `.as`, `.bas`, `.v`, `.pro`, `.m`).
- **Pygments' home turf**: its lexers are tested on these files and its taxonomy is the label set; a
  tool that does not know a niche lexer (Debian Sourcelist, cplint, Tera Term macro) cannot be right.
- **Test files**: many exercise a lexer's corners (`evil_regex.js`, `fucked_up.rb`, 26 Scala files
  for syntax edge cases) rather than typical code; 45 are `tiny` (under 5 non-blank lines).
- **Thin per language**: 323 labels have one file; per-language figures are anecdotes.

## Composition

| | files |
|---|---:|
| Linguist type programming / data / markup / prose | 372 / 61 / 21 / 7 |
| not in Linguist | 176 |
| most files: Scala, GraphQL, Python traceback, Ruby, C++, C, cplint, JavaScript, Makefile | 26, 14, 10, 8, 6, 5, 5, 5, 5 |
| labels with 1 / 2 / 3–5 / more files | 323 / 69 / 31 / 5 |

| tag | files | |
|---|---:|---|
| `in-linguist` / `not-in-linguist` | 461 / 176 | the label maps to a Linguist language, or not |
| `ambiguous-ext` | 114 | the extension is claimed by two or more Linguist languages |
| `renamed` | 103 | the name contained the label; run as `example<ext>` |
| `tiny` | 45 | under 5 non-blank lines |
| `linguist-sample` / `seen-in-training` | 15 / 15 | byte-identical to a Linguist 76f88c6 sample / to Hyperpolyglot's training samples |

## Findings (2026-10-03)

> Figures in this README come from the runs made when the benchmark was built (2026-10-03). Entries were rerun since (pinned images, updated name mappings) and Jev was added: [LEADERBOARD.md](LEADERBOARD.md), regenerated from the stored runs, is the reference.

**The home-turf effect is real, and it is in the names and the taxonomy, not in the content.**

- **Pygments 2.21.0 ranks first: 595 / 637 (93.4 %)**, against 32.3 % on bench-linguist. Pygments
  2.19.2 and 2.14.0 follow (92.6 %, 84.6 %); then Synid 48c3c45 (82.1 %).
- **On the 461 files Linguist can name, Pygments and Linguist are close**: 440 vs 429 (95.4 % vs
  93.1 %). The 26-point gap overall is the 176 files in languages only Pygments names: 155 for
  Pygments, at most 1 for the Linguist family.
- **From the content only, Pygments gets 67 / 637 (10.5 %)** — the same as on bench-linguist (10.2 %):
  its guesser shows no sign of having been tuned on its own examples.
- **Synid is second (82.1 %) because its catalogue contains Pygments' lexers**: right on 134 of the
  176 files outside Linguist. Its weak spot is the ambiguous extensions (60 / 114, against 96 for Pygments
  and 87 for Linguist). Without the name, 4.6 %.
- **Chroma, a Go port of many Pygments lexers, 48.5 %**; Rouge 38.3 %; highlight.js 13.8 %
  (content only by design).

| entry | run | right | precision | `in-linguist` | `not-in-linguist` | `ambiguous-ext` | `renamed` | `tiny` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Pygments 2.21.0 | `ext-pygments` | **595/637** (93.4 %) | 96.6 % | 440/461 | 155/176 | 96/114 | 82/103 | 42/45 |
| Pygments 2.19.2 | `ext-pygments-v2.19` | **590/637** (92.6 %) | 96.6 % | 437/461 | 153/176 | 96/114 | 82/103 | 42/45 |
| Pygments 2.14.0 | `ext-pygments-v2.14` | **539/637** (84.6 %) | 95.9 % | 397/461 | 142/176 | 91/114 | 78/103 | 42/45 |
| Synid 48c3c45 | `48c3c45-default` | **523/637** (82.1 %) | 91.8 % | 389/461 | 134/176 | 60/114 | 70/103 | 36/45 |
| Synid 9bc1c32 | `9bc1c32-default` | **515/637** (80.8 %) | 83.3 % | 386/461 | 129/176 | 58/114 | 68/103 | 36/45 |
| GitHub Linguist 9.7.0 | `ext-linguist` | **429/637** (67.3 %) | 91.1 % | 429/461 | 0/176 | 87/114 | 56/103 | 33/45 |
| go-enry 2.9.6 | `ext-enry` | **425/637** (66.7 %) | 90.4 % | 425/461 | 0/176 | 83/114 | 54/103 | 32/45 |
| GitHub Linguist 8.0.0 | `ext-linguist-v8` | **422/637** (66.2 %) | 90.9 % | 422/461 | 0/176 | 83/114 | 54/103 | 33/45 |
| linguist-js 3.0.4 | `ext-linguist-js` | **422/637** (66.2 %) | 89.6 % | 422/461 | 0/176 | 80/114 | 55/103 | 31/45 |
| go-enry 2.8.9 | `ext-enry-v2.8` | **419/637** (65.8 %) | 90.9 % | 419/461 | 0/176 | 82/114 | 54/103 | 32/45 |
| GitHub Linguist 7.30.0 | `ext-linguist-v7` | **419/637** (65.8 %) | 90.9 % | 419/461 | 0/176 | 83/114 | 54/103 | 33/45 |
| Hyperpolyglot a55a3b5 | `ext-hyperpolyglot` | **389/637** (61.1 %) | 90.7 % | 388/461 | 1/176 | 79/114 | 49/103 | 31/45 |
| Chroma 2.27.0 | `ext-chroma` | **309/637** (48.5 %) | 59.7 % | 287/461 | 22/176 | 55/114 | 43/103 | 25/45 |
| Neovim 0.12.5 filetype | `ext-nvim` | **299/637** (46.9 %) | 75.3 % | 280/461 | 19/176 | 49/114 | 33/103 | 22/45 |
| cloc 2.10 | `ext-cloc` | **273/637** (42.9 %) | 83.5 % | 268/461 | 5/176 | 56/114 | 40/103 | 23/45 |
| scc 4.1.0 | `ext-scc` | **267/637** (41.9 %) | 85.3 % | 261/461 | 6/176 | 51/114 | 39/103 | 21/45 |
| tokei 15.0.0 | `ext-tokei` | **254/637** (39.9 %) | 84.7 % | 248/461 | 6/176 | 50/114 | 36/103 | 19/45 |
| Rouge 5.1.0 | `ext-rouge` | **244/637** (38.3 %) | 79.5 % | 241/461 | 3/176 | 46/114 | 29/103 | 20/45 |
| gengo 0.15.0 | `ext-gengo` | **189/637** (29.7 %) | 87.9 % | 188/461 | 1/176 | 34/114 | 24/103 | 17/45 |
| ohcount 4.0.0 (Debian 4.0.0-5) | `ext-ohcount` | **174/637** (27.3 %) | 77.3 % | 173/461 | 1/176 | 40/114 | 30/103 | 19/45 |
| Universal Ctags 6.2.1 | `ext-ctags` | **143/637** (22.4 %) | 76.1 % | 140/461 | 3/176 | 38/114 | 24/103 | 10/45 |
| FrameByFrame/programming-language-identification-100plus da6a18b | `ext-hf-framebyframe` | **140/637** (22.0 %) | 22.0 % | 140/461 | 0/176 | 29/114 | 17/103 | 13/45 |
| Magika 1.0.3 | `ext-magika` | **120/637** (18.8 %) | 29.1 % | 120/461 | 0/176 | 24/114 | 18/103 | 8/45 |
| Guesslang 2.2.1 | `ext-guesslang` | **99/637** (15.5 %) | 15.5 % | 99/461 | 0/176 | 23/114 | 15/103 | 7/45 |
| highlight.js 11.12.0 | `ext-hljs` | **88/637** (13.8 %) | 14.1 % | 85/461 | 3/176 | 18/114 | 16/103 | 7/45 |
| vscode-languagedetection 1.0.23 | `ext-vscode-ld` | **83/637** (13.0 %) | 19.3 % | 83/461 | 0/176 | 19/114 | 13/103 | 2/45 |
| Magika 0.5.1 | `ext-magika-v0.5` | **72/637** (11.3 %) | 24.6 % | 72/461 | 0/176 | 14/114 | 10/103 | 2/45 |
| Pygments 2.14.0, content only | `ext-pygments-v2.14-content-only` | **68/637** (10.7 %) | 11.6 % | 50/461 | 18/176 | 26/114 | 18/103 | 5/45 |
| Pygments 2.21.0, content only | `ext-pygments-content-only` | **67/637** (10.5 %) | 11.3 % | 54/461 | 13/176 | 21/114 | 19/103 | 5/45 |
| Pygments 2.19.2, content only | `ext-pygments-v2.19-content-only` | **67/637** (10.5 %) | 11.3 % | 54/461 | 13/176 | 21/114 | 19/103 | 5/45 |
| philomath-1209/programming-language-identification 9090d38 | `ext-hf-philomath` | **66/637** (10.4 %) | 10.4 % | 66/461 | 0/176 | 8/114 | 7/103 | 4/45 |
| flourite 1.3.0 | `ext-flourite` | **47/637** (7.4 %) | 7.7 % | 46/461 | 1/176 | 12/114 | 3/103 | 3/45 |
| file 5.46 (libmagic) | `ext-libmagic` | **45/637** (7.1 %) | 21.4 % | 45/461 | 0/176 | 14/114 | 7/103 | 4/45 |
| Synid 48c3c45, content only | `48c3c45-content-only` | **29/637** (4.6 %) | 7.5 % | 29/461 | 0/176 | 10/114 | 5/103 | 4/45 |
| GitHub Linguist 9.7.0, content only | `ext-linguist-content-only` | **23/637** (3.6 %) | 82.1 % | 23/461 | 0/176 | 7/114 | 3/103 | 2/45 |
| go-enry 2.9.6, content only | `ext-enry-content-only` | **23/637** (3.6 %) | 85.2 % | 23/461 | 0/176 | 7/114 | 3/103 | 2/45 |
| huggingface/CodeBERTa-language-id 67e92a9 | `ext-hf-codeberta` | **21/637** (3.3 %) | 3.3 % | 21/461 | 0/176 | 1/114 | 2/103 | 2/45 |
| Rouge 5.1.0, content only | `ext-rouge-content-only` | **21/637** (3.3 %) | 44.7 % | 21/461 | 0/176 | 6/114 | 3/103 | 1/45 |
| Hyperpolyglot a55a3b5, content only | `ext-hyperpolyglot-content-only` | **17/637** (2.7 %) | 89.5 % | 17/461 | 0/176 | 6/114 | 2/103 | 2/45 |
| Neovim 0.12.5 filetype, content only | `ext-nvim-content-only` | **16/637** (2.5 %) | 50.0 % | 15/461 | 1/176 | 2/114 | 3/103 | 2/45 |
| Chroma 2.27.0, content only | `ext-chroma-content-only` | **7/637** (1.1 %) | 2.1 % | 7/461 | 0/176 | 1/114 | 1/103 | 0/45 |

Of Pygments' own 42 misses, 19 are files whose name its patterns do not match (no answer, or `Text
only` for a `.txt`), 21 are another language (5 cplint files answered Prolog, cplint being a Prolog
dialect; `.css` answered CSS+Lasso; `.pro` answered Visual Prolog for IDL), and 2 are the
`MQL` files: Pygments names the family, which `tools/external/pygments/names.csv` maps to MQL4 and
MQL5 — two answers, counted undecided.

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
| `labels.csv` | the crosswalk: Pygments lexer name → Linguist name, how, directory, files |
| `build_cases.py` | fetches Pygments, Linguist and Hyperpolyglot at pinned commits, writes `cases.csv`, `labels.csv`, `files/` |
| `card.json`, `contamination.json` | the benchmark card; the entries built or trained on these files |
| `baselines/`, `entries/` | Synid versions (default configuration); other configurations and other identifiers |
| `reproduce.sh` | rebuilds every entry |
