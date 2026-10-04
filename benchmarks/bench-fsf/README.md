# bench-fsf — archived `.fsf` files: FEAT designs in Tcl syntax, and what else squats on `.fsf`

Part of [synid-bench](../../README.md). **467 `.fsf` files archived by
[Software Heritage](https://www.softwareheritage.org)**, drawn uniformly from the
21,802 `.fsf` contents of the archive, with real file names, origins and
population weights. Labels come from an LLM judge (**silver**): no human checked
them. The cases come from the `.fsf` extension study of
[PL-ultimate-llm](https://github.com/acherm/PL-ultimate-llm) (branch
`swh-evidence-v1`, commit `274fa4cc8`, `docs/fsf_swh_study.md`).

No language in Linguist claims `.fsf`. In the archive it is, four times in five,
an **FSL FEAT design file**: the configuration of an fMRI analysis, a list of
Tcl commands (`set fmri(level) 1`) that FSL's GUI writes and loads with Tcl's
`source`. The rest is what an unclaimed extension collects: git-annex pointers
(DataLad datasets archive the path of the annexed design, not the design),
XML fractal saves, a GLSL shader, a C++ header, JSON. The benchmark asks what an
identifier does with a file whose extension tells it nothing.

## Where the files and labels come from

- **Population and sample.** The study's population table lists the 21,802
  unique `.fsf` contents of the archive and their origins. Its frame E1 is a
  uniform random sample of 1,000 of them (seed 5), fetched from Software
  Heritage by sha1_git (999 fetched).
- **Labels.** Each file was labelled by Claude Sonnet 4.6 (OpenRouter,
  temperature 0, structured output, schema `fsf-judge/1`: content type, format,
  the notation it is expressed in, related languages, FEAT details). The judge saw
  the bytes, the file name and the study's mechanical indicators. The expected
  language is derived from its verdict (see below). The study's rule — a
  `set fmri(` line makes a FEAT design — agrees with the judge on every case
  (tag `judge-rules-agree`).
- **A FEAT design is Tcl.** The judge says it is "not a programming language" —
  a statement about the file's role — and "expressed in Tcl set-variable
  syntax". synid-bench measures syntax identification: a FEAT design parses, and
  runs, as Tcl, so its expected name is `Tcl` (accepted: `Tcl`, its Linguist
  aliases, `FSL FEAT design`), and `Text` on it counts as `Text` on code. The
  results below also give the score if `Text` were accepted on FEAT designs.
- **Not code (`Text`).** git-annex pointers (a single line, a path into
  `.git/annex/objects/`) and two documentation files (a ChangeLog, an INSTALL).
- **Drawn down.** The uniform sample has 800 FEAT designs, mostly generated per
  subject and run (near-duplicates); a seeded draw keeps 300 (seed 2026). Every
  other labelled file is kept.
- **Left out** of the 1,000: 17 files that are not text and one not fetched
  (never judged), 13 notations Linguist does not name (Altera Nios IDE settings,
  FDT scripts, an L-system DSL, an ML-like test syntax, a FINAN mapping DSL…),
  one binary, one low-confidence verdict.
- **Weights.** `weight` = the label's share of the uniform sample × 21,802 / the
  number of cases with that label: Tcl 58.14 (800 of the sample, 300 kept), the
  others 21.8.
- **Names.** `filename` is the archived file name (none contains its label).
  `qualified_swhid` carries the origin and the path from the study's origin table
  (`fsf_files+origin.csv`, which is not in PL-ultimate-llm's git: read from the
  checkout); the path is omitted in 17 cases where the table's path names another
  file. The contents are archived (fetched by the study from Software Heritage;
  spot-checked with the public API on 2026-10-03).
- **Files** are stored in `files/<sha1_git>` (8.3 MB), checked against their
  sha1_git; each keeps the licence of its origin repository.

## Composition

| expected | files | weight each | what |
|---|---:|---:|---|
| Tcl | 300 | 58.14 | FSL FEAT designs (287 tagged `feat-design`, 12 `melodic`, one verdict without the field) |
| Text | 125 | 21.8 | 123 git-annex pointers, a ChangeLog, an INSTALL |
| XML | 38 | 21.8 | XML fractal saves (37), an XML session file |
| JSON | 2 | 21.8 | a visual flow model |
| GLSL | 1 | 21.8 | a fragment shader |
| C++ | 1 | 21.8 | a header with a GLSL shader in a string |

Tags: `feat-design` 287, `melodic` 12, `git-annex-pointer` 123, `tiny` 123 (fewer
than three lines: the pointers), `non-utf8` 1, `judge-rules-agree` 467. 105
repositories; the largest (`QQXiao/ISR_2015`) has 81 files.

## Strengths and weaknesses

- **Strengths.** Drawn uniformly from the archive, with weights. An extension no
  language claims, so the file name does not help: content-only by nature. Files
  that are not code (pointers) under a name that looks like code. Real names
  and repositories.
- **Weaknesses.** One LLM judge labelled every file; nobody checked the labels.
  LLM labels may favour LLM entries. `Tcl` for a FEAT design is a choice (the
  syntax over the role). The 300 FEAT designs are near-duplicates: in effect a
  handful of distinct shapes. One extension.
- **Home turf.** The study's rule was written after reading the judge's labels on
  these files; PL-ultimate-llm's candidates for the Jev cascade (C++, GLSL, Tcl)
  are exactly what the study observed here, and nothing else claims `.fsf`. See
  `contamination.json`.

## Build and run

```bash
python3 benchmarks/bench-fsf/build_cases.py            # needs PL-ultimate-llm at 274fa4cc8 ($PL_ULTIMATE_LLM)
python3 benchmarks/bench-fsf/export_reference_runs.py  # the study's rule and Jev's stored decisions (no API call)
python3 tools/run.py benchmarks/bench-fsf --synid path/to/synid --label mytest
SYNID=path/to/synid benchmarks/bench-fsf/reproduce.sh   # everything
```

`build_cases.py` reads the study's reports and worklist from PL-ultimate-llm's
git at commit `274fa4cc8` (shared code: `tools/study_cases.py`); a rerun gives
the same `cases.csv`. All cases are silver: `tools/score.py` prints the weighted
accuracy for gold only; the leaderboard weights every benchmark that has weights.

## Results

Every run of 2026-10-03 (Synid binaries `48c3c45` and `9bc1c32`; the other identifiers in their
pinned images, `tools/external.py`; the study's rule and Jev's decisions exported from the study,
no API call). Entries with the same score on the same cases are grouped.

| entries | right | accuracy | weighted to the population |
|---|---:|---:|---:|
| Magika 1.0.3 | 432/467 | 92.5 % | 93.5 % |
| Hand-written .fsf rule (tuned on these files) | 300/467 | 64.2 % | 82.7 % |
| Jev 1.13, study's 63 labels, content only | 152/467 | 32.5 % | 20.0 % |
| Rouge 5.1.0 | 162/467 | 34.7 % | 16.8 % |
| Jev 1.13, study's 63 labels, with file name | 128/467 | 27.4 % | 13.6 % |
| file 5.46 (libmagic) | 127/467 | 27.2 % | 13.1 % |
| Magika 0.5.1 | 86/467 | 18.4 % | 8.9 % |
| Guesslang 2.2.1; vscode-languagedetection 1.0.23 | 40/467 | 8.6 % | 4.1 % |
| Pygments 2.21.0, content only; Synid 48c3c45, comment off | 39/467 | 8.4 % | 4.0 % |
| Synid 48c3c45; Synid 48c3c45, content only; Synid 48c3c45, hyplyclassifier off; Synid 48c3c45, hyplyheuristics off | 3/467 | 0.6 % | 0.3 % |
| flourite 1.3.0 | 2/467 | 0.4 % | 0.2 % |
| Chroma 2.27.0; GitHub Linguist 7.30.0; GitHub Linguist 8.0.0; GitHub Linguist 9.7.0; GitHub Linguist 9.7.0, content only; Hyperpolyglot a55a3b5; Hyperpolyglot a55a3b5, content only; Neovim 0.12.5 filetype; Pygments 2.14.0; Pygments 2.19.2; Pygments 2.21.0; Synid 48c3c45, pygmentsheuristics off; Synid 9bc1c32; Universal Ctags 6.2.1; cloc 2.10; gengo 0.15.0; go-enry 2.8.9; go-enry 2.9.6; go-enry 2.9.6, content only; highlight.js 11.12.0; linguist-js 3.0.4; ohcount 4.0.0 (Debian 4.0.0-5); scc 4.1.0; tokei 15.0.0 | 0/467 | 0.0 % | 0.0 % |

- **Synid answers ALGOL 68 on every FEAT design**, both versions, with or without the name (no
  rule claims `.fsf`, so its default run is a content-only run). The `comment` strategy does it:
  FEAT designs are full of `#` comment lines. Without that strategy (`comment off`), the
  classifier answers Smali (262), Carbon (28) or GDScript (9) — never Tcl. `48c3c45` also answers
  reStructuredText on 122 git-annex pointers and `Text` on 37 of the 38 XML files; `9bc1c32`
  gives no answer on those.
- **Rule-based identifiers abstain on every file** (GitHub Linguist 7–9, go-enry, linguist-js,
  Hyperpolyglot, Pygments with the name, Neovim, cloc, ctags, gengo, ohcount, scc, tokei): no rule claims
  `.fsf`, and none falls back on its classifier for an unknown extension (Neovim names one
  ChangeLog `changelog`). Chroma's content
  analysis names GDScript on every FEAT design.
- **Magika 1.0.3 is the only tool that finds Tcl** (Jev: 25 of 300): `tcl` on 283 of the 300 FEAT designs,
  XML on all 38 XML files, `Text` on 109 of the 125 pointers and documents — 93.5 % weighted.
  Magika 0.5.1 and libmagic say `Text` on every FEAT design.
- Highlighters on content: Rouge says `Text` on everything but 37 XML files (right on those and on
  the 125 pointers and documents); highlight.js names RouterOS Script (299 FEAT
  designs) and Awk (103 pointers); Guesslang names Shell (256) or Julia (31).
- Jev with the study's labels answers `key-value-config` (scored as `Text`) on 275 FEAT designs
  from the content, and on 291 with the name; its `xml-html` is undecided between XML and HTML.
- **If `Text` were accepted on FEAT designs** (the judge's reading: "not a programming
  language"), the weighted accuracies would be: Rouge 99.5 %, Magika 1.0.3 97.3 %, Jev content
  only 95.9 %, libmagic 95.9 %, Jev with name 93.8 %, Magika 0.5.1 91.6 %; Synid unchanged (0.3 %), since it
  names a language.

Not run here: hf-codeberta, hf-framebyframe, hf-philomath and plangrec (slow transformer or memory-heavy tools, left to a later throttled batch).
