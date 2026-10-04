# bench-rouge — Rouge's visual samples and demos

The **visual samples and demos of [Rouge](https://github.com/rouge-ruby/rouge/tree/16e6ecdb3bc4248cead78375e1b24580ee2352a1)**,
the Ruby highlighter of GitLab and Jekyll: `spec/visual/samples/<tag>` (230 files, a page or more of
code exercising a lexer) and `lib/rouge/demos/<tag>` (225 distinct files of a few lines, shown on
Rouge's site), each labelled by the lexer it is named after — **455 files, 230 lexers, 229 labels**.
Each file is named by its lexer's tag without an extension — a name that is the label — so every case
is run **without a name**. It is Rouge's *home turf*: running every identifier on it shows how much a
benchmark favours the tool it was built from. Siblings: [bench-pygments](../bench-pygments/README.md),
[bench-hljs](../bench-hljs/README.md).

| | |
|---|---|
| cases | 455 files, no names: 230 samples (tag `sample`) and 225 demos (`demo`; 5 demos byte-identical to their lexer's sample are left out); 373 files in 187 languages Linguist has, 82 in 42 it does not |
| labels | the lexer whose tag names the file (its `title` in `lib/rouge/lexers/*.rb`; Rouge's default, the tag capitalised, when there is none), written as Linguist's name when Linguist has the language ([labels.csv](labels.csv)); a case is right when the answer is that language, one of its Linguist aliases, or Rouge's title or tag |
| source | Rouge at [`16e6ecd`](https://github.com/rouge-ruby/rouge/tree/16e6ecdb3bc4248cead78375e1b24580ee2352a1) (2026-08-28), MIT |
| files | **not stored here**: `build_cases.py` fetches them at the pinned commit and checks each against its git blob id |

```bash
python3 benchmarks/bench-rouge/build_cases.py          # fetch the files (and rebuild cases.csv, identical)
python3 tools/run.py benchmarks/bench-rouge --synid path/to/synid --label mytest
python3 tools/score.py benchmarks/bench-rouge/results/mytest.jsonl \
    --baseline benchmarks/bench-rouge/baselines/48c3c45-default.jsonl
benchmarks/bench-rouge/reproduce.sh                    # every entry (SYNID=path/to/synid)
```

`build_cases.py` makes a shallow, blob-less, sparse fetch of the pinned commit into `.work/` (or
`--cache DIR`, or `$SYNID_BENCH_CACHE`), plus Linguist `76f88c6` and Hyperpolyglot `a55a3b5` (to tag
files that are Linguist samples). A rerun gives an identical `cases.csv`.

## Whose home turf

**Rouge's, for lexing.** Its test suite (`spec/lexers_spec.rb`) lexes every sample — the tokens must
give the sample back unchanged — and every demo, which must lex without an error token: the lexers were
written against these files. **Its guessing is not tested on them**: the guessing specs use file
names, MIME types and short sources written in the spec. Others, by blob id
([contamination.json](contamination.json)): the Fluent demo is a Linguist sample (since v7.15.0, so in
every Linguist and go-enry release run here); the YANG sample is an input of Chroma's lexer tests; the YANG and
Visual Basic samples are also Pygments examples; the Lasso sample is also highlight.js' Lasso detection test.

The content is archived in Software Heritage (3 of 3 sampled `swh:1:cnt` found, and the revision
`16e6ecd`, 2026-10-03).

## Labels: what is kept, and the crosswalk

**Kept: languages**, with the rule of bench-pygments: a language Linguist has (of any type), or
another programming, markup, data, configuration, template or grammar language. **Left out (10
files, 5 lexers):** `irb` (a session transcript), `irb_output` and `tap` (the output of a program),
`plaintext`, and `escape` (Rouge's helper for escaped content inside another lexer). Kept: `console`
(ShellSession), `http`, `email`, `diff`.

**Crosswalk** ([labels.csv](labels.csv), title → Linguist name): synonyms only, as in
`tools/external/*/names.csv` (and in agreement with `tools/external/rouge/names.csv`). 157 by the same
title (or tag), 21 by a Linguist alias (Make → Makefile, Nasm → Assembly, Terraform → HCL, Visual
Basic → Visual Basic .NET, Jsp → Java Server Pages), 10 by hand (1C (BSL) → 1C Enterprise, DOT →
Graphviz (DOT), HQL → HiveQL, Plist → OpenStep Property List, SSH Config File → SSH Config, Rego → Open
Policy Agent; `Verilog and System Verilog` → Verilog;SystemVerilog as a family), 42 none. Not mapped:
`Config File` (a generic lexer, although Linguist lists `conf` among INI's aliases), Systemd (Linguist
files unit files under INI), JSX, Json-doc, CFScript, ArmAsm, NesAsm, KickAssembler.

## Strengths and weaknesses

- **Content only**, by construction, as bench-hljs; and **two sizes per language**: a sample (median
  87 non-blank lines) and a demo (median 8; all 50 `tiny` files are demos) — the same languages, short
  and long.
- **Independent of Linguist**: one file is a Linguist sample; 82 files in 42 languages Linguist lacks
  (AddmusicK, Cisco IOS, Syzlang, TTCN3 …).
- **Rouge's home turf for lexing and taxonomy**, though not for guessing (below).
- **Written for a lexer**: samples are often lists of edge cases (every literal form, odd escapes);
  demos are a few lines picked to look good.
- **Two files per language**: per-language figures are anecdotes.

## Composition

| | files |
|---|---:|
| Linguist type programming / data / markup / prose | 285 / 49 / 37 / 2 |
| not in Linguist | 82 |
| labels with 1 / 2 / 4 files | 5 / 223 / 1 (HCL: `hcl` and `terraform`) |
| non-blank lines: 10th percentile / median / 90th | 4 / 22 / 211 |

| tag | files | |
|---|---:|---|
| `sample` / `demo` | 230 / 225 | a visual sample / a demo |
| `in-linguist` / `not-in-linguist` | 373 / 82 | the label maps to a Linguist language, or not |
| `tiny` | 50 | under 5 non-blank lines |
| `linguist-sample` | 1 | byte-identical to a Linguist 76f88c6 sample |

No file is run with a name: `ambiguous-ext` does not apply, and tools that answer from the name only
(cloc, scc, tokei, gengo: `"needs_name": true`) are not run. For tools without a `--content-only`
flag the default run already sees no name, so no separate content-only run is made; for those with one,
both runs are kept (Pygments' default, `guess_lexer_for_filename`, gives no answer without a name).

## Findings (2026-10-03)

**No home-turf effect for Rouge itself: a benchmark favours its tool only on the task the tool was
tested on.**

- **Rouge 5.1.0 is right on 29 / 455 (6.4 %)**, twelfth (tied). Without a name its guesser rarely
  concludes: it answers plain text on 417 files. When it does name a language it is right 78.4 % of the time.
  Its tests lex these files; nothing tuned its guessing on them.
- **Content guessers lead**: Magika 1.0.3 125 (27.5 %), the ModernBERT classifier FrameByFrame 116
  (25.5 %), Guesslang 93 (20.4 %), highlight.js 11.12.0 85 (18.7 %), VS Code's detector 70 (15.4 %).
  Of the 82 files in languages outside Linguist, they get 0–2; Rouge and Pygments' `guess_lexer` 5
  each, Neovim 4.
- **Synid 18 (4.0 %)**, Synid 9bc1c32 11; the Linguist family 12 (2.6 %), Hyperpolyglot 7.
- **Short demos are harder than samples** for most tools (Magika 58 / 225 vs 67 / 230; VS Code's
  detector 20 vs 50; Rouge 10 vs 19), not for highlight.js (42 vs 43) nor FrameByFrame (61 vs 55).


| entry | run | right | precision | `sample` | `demo` | `in-linguist` | `not-in-linguist` | `tiny` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Magika 1.0.3 | `ext-magika` | **125/455** (27.5 %) | 39.7 % | 67/230 | 58/225 | 123/373 | 2/82 | 15/50 |
| FrameByFrame/programming-language-identification-100plus da6a18b | `ext-hf-framebyframe` | **116/455** (25.5 %) | 25.5 % | 55/230 | 61/225 | 116/373 | 0/82 | 17/50 |
| Guesslang 2.2.1 | `ext-guesslang` | **93/455** (20.4 %) | 20.4 % | 50/230 | 43/225 | 93/373 | 0/82 | 14/50 |
| highlight.js 11.12.0 | `ext-hljs` | **85/455** (18.7 %) | 19.1 % | 43/230 | 42/225 | 84/373 | 1/82 | 10/50 |
| vscode-languagedetection 1.0.23 | `ext-vscode-ld` | **70/455** (15.4 %) | 27.1 % | 50/230 | 20/225 | 70/373 | 0/82 | 1/50 |
| Magika 0.5.1 | `ext-magika-v0.5` | **51/455** (11.2 %) | 22.8 % | 25/230 | 26/225 | 49/373 | 2/82 | 13/50 |
| philomath-1209/programming-language-identification 9090d38 | `ext-hf-philomath` | **46/455** (10.1 %) | 10.1 % | 22/230 | 24/225 | 46/373 | 0/82 | 7/50 |
| flourite 1.3.0 | `ext-flourite` | **35/455** (7.7 %) | 8.0 % | 19/230 | 16/225 | 35/373 | 0/82 | 5/50 |
| Pygments 2.21.0, content only | `ext-pygments-content-only` | **34/455** (7.5 %) | 7.9 % | 19/230 | 15/225 | 29/373 | 5/82 | 2/50 |
| Pygments 2.19.2, content only | `ext-pygments-v2.19-content-only` | **34/455** (7.5 %) | 7.9 % | 19/230 | 15/225 | 29/373 | 5/82 | 2/50 |
| file 5.46 (libmagic) | `ext-libmagic` | **30/455** (6.6 %) | 20.5 % | 16/230 | 14/225 | 30/373 | 0/82 | 5/50 |
| Rouge 5.1.0 | `ext-rouge` | **29/455** (6.4 %) | 78.4 % | 19/230 | 10/225 | 24/373 | 5/82 | 3/50 |
| Pygments 2.14.0, content only | `ext-pygments-v2.14-content-only` | **29/455** (6.4 %) | 6.9 % | 16/230 | 13/225 | 26/373 | 3/82 | 0/50 |
| Rouge 5.1.0, content only | `ext-rouge-content-only` | **29/455** (6.4 %) | 78.4 % | 19/230 | 10/225 | 24/373 | 5/82 | 3/50 |
| Synid 48c3c45 | `48c3c45-default` | **18/455** (4.0 %) | 7.7 % | 11/230 | 7/225 | 17/373 | 1/82 | 1/50 |
| Synid 48c3c45, content only | `48c3c45-content-only` | **18/455** (4.0 %) | 7.7 % | 11/230 | 7/225 | 17/373 | 1/82 | 1/50 |
| Neovim 0.12.5 filetype | `ext-nvim` | **17/455** (3.7 %) | 77.3 % | 11/230 | 6/225 | 13/373 | 4/82 | 1/50 |
| Neovim 0.12.5 filetype, content only | `ext-nvim-content-only` | **17/455** (3.7 %) | 77.3 % | 11/230 | 6/225 | 13/373 | 4/82 | 1/50 |
| GitHub Linguist 8.0.0 | `ext-linguist-v8` | **12/455** (2.6 %) | 85.7 % | 10/230 | 2/225 | 12/373 | 0/82 | 1/50 |
| go-enry 2.9.6 | `ext-enry` | **12/455** (2.6 %) | 85.7 % | 10/230 | 2/225 | 12/373 | 0/82 | 1/50 |
| GitHub Linguist 9.7.0 | `ext-linguist` | **12/455** (2.6 %) | 85.7 % | 10/230 | 2/225 | 12/373 | 0/82 | 1/50 |
| go-enry 2.8.9 | `ext-enry-v2.8` | **12/455** (2.6 %) | 85.7 % | 10/230 | 2/225 | 12/373 | 0/82 | 1/50 |
| GitHub Linguist 7.30.0 | `ext-linguist-v7` | **12/455** (2.6 %) | 85.7 % | 10/230 | 2/225 | 12/373 | 0/82 | 1/50 |
| Synid 9bc1c32 | `9bc1c32-default` | **11/455** (2.4 %) | 5.3 % | 8/230 | 3/225 | 11/373 | 0/82 | 0/50 |
| huggingface/CodeBERTa-language-id 67e92a9 | `ext-hf-codeberta` | **11/455** (2.4 %) | 2.4 % | 6/230 | 5/225 | 11/373 | 0/82 | 1/50 |
| linguist-js 3.0.4 | `ext-linguist-js` | **10/455** (2.2 %) | 100.0 % | 9/230 | 1/225 | 10/373 | 0/82 | 0/50 |
| ohcount 4.0.0 (Debian 4.0.0-5) | `ext-ohcount` | **9/455** (2.0 %) | 33.3 % | 5/230 | 4/225 | 9/373 | 0/82 | 2/50 |
| Hyperpolyglot a55a3b5 | `ext-hyperpolyglot` | **7/455** (1.5 %) | 100.0 % | 6/230 | 1/225 | 7/373 | 0/82 | 0/50 |
| Universal Ctags 6.2.1 | `ext-ctags` | **7/455** (1.5 %) | 100.0 % | 5/230 | 2/225 | 7/373 | 0/82 | 1/50 |
| Chroma 2.27.0 | `ext-chroma` | **5/455** (1.1 %) | 2.2 % | 2/230 | 3/225 | 5/373 | 0/82 | 0/50 |
| Chroma 2.27.0, content only | `ext-chroma-content-only` | **5/455** (1.1 %) | 2.2 % | 2/230 | 3/225 | 5/373 | 0/82 | 0/50 |
| Pygments 2.19.2 | `ext-pygments-v2.19` | **0/455** (0.0 %) | — | 0/230 | 0/225 | 0/373 | 0/82 | 0/50 |
| Pygments 2.14.0 | `ext-pygments-v2.14` | **0/455** (0.0 %) | — | 0/230 | 0/225 | 0/373 | 0/82 | 0/50 |
| Pygments 2.21.0 | `ext-pygments` | **0/455** (0.0 %) | — | 0/230 | 0/225 | 0/373 | 0/82 | 0/50 |

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
| `labels.csv` | the crosswalk: Rouge lexer title → Linguist name, how, tag, files |
| `build_cases.py` | fetches Rouge, Linguist and Hyperpolyglot at pinned commits, writes `cases.csv`, `labels.csv`, `files/` |
| `card.json`, `contamination.json` | the benchmark card; the entries built or tested on these files |
| `baselines/`, `entries/` | Synid versions (default configuration); other configurations and other identifiers |
| `reproduce.sh` | rebuilds every entry |
