# bench-rosetta — Rosetta Code solutions, up to two per language

A benchmark of breadth whose labels no identifier produced: **1,589 solutions from
[Rosetta Code](https://rosettacode.org) in 848 languages**, up to two per language, each labelled by the
language heading its contributor filed it under. Where [bench-linguist](../bench-linguist/README.md)'s labels
are Linguist's and its files the Linguist family's training set, here the labels come from the authors — and
two thirds of the cases are in languages Linguist does not know.

| | |
|---|---|
| cases | 1,589 solutions, 848 languages (883 have solutions in the dump; 35 have none of 3+ non-blank lines) |
| labels | the language heading of the solution on rosettacode.org (author-declared); mapped to Linguist's name for synonyms only ([`labels.csv`](labels.csv)); a case is right when the answer is that name, one of its Linguist aliases, or Rosetta Code's own name |
| source | [acmeism/RosettaCodeData](https://github.com/acmeism/RosettaCodeData) at [`1d475861d7141ef2fafff293d9339f56e4b0f5db`](https://github.com/acmeism/RosettaCodeData/tree/1d475861d7141ef2fafff293d9339f56e4b0f5db) (2026-07-16): `Task/<task>/<language>/<task>[-<n>].<ext>`; Linguist's `languages.yml` at `76f88c6` for the crosswalk |
| sampling | per language, seeded (20261003): up to 2 solutions of 2 different tasks, among the files of 3+ non-blank lines and at most 100 KB |
| files | **not stored here**: Rosetta Code's content is under the GNU Free Documentation License ([v1.2](https://rosettacode.org/wiki/Rosetta_Code:Copyrights) per the site's copyright page, 1.3 per its footer); `build_cases.py` fetches the dump at the pinned commit and checks each file against its git blob id |

```bash
python3 benchmarks/bench-rosetta/build_cases.py          # fetch the files (and rebuild cases.csv, identical)
python3 tools/run.py benchmarks/bench-rosetta --synid path/to/synid --label mytest --content-only
python3 tools/score.py benchmarks/bench-rosetta/results/mytest.jsonl \
    --baseline benchmarks/bench-rosetta/entries/48c3c45-content-only.jsonl
```

`build_cases.py --cache DIR` (or `$BENCH_CACHE`) sets where the dump is fetched (a shallow fetch of one commit,
~130 MB; default `.work/`). Every case has a SWHID with the dump as origin; the contents are archived by
Software Heritage (6 of 6 checked through its API).

## Read it with care

**The file name gives the label away.** acmeism names every solution `<task>[-<n>].<ext>`, the extension
taken from a table of one extension per language (`Conf/lang.yaml`), often invented for the purpose: `.0815`,
`.phix`, `.arturo`, `.basic` for every BASIC. A tool that reads the name reads the label back through that
table where the extension is a real one (`.py`, `.rs`), and has nothing to go on where it is invented. The
names are kept (card: `names: label-derived`), but **the content-only runs are the fair reading** of this
benchmark. Tags: `invented-ext` — the extension is claimed by no Linguist language (1,135 cases);
`misleading-ext` — it is claimed by Linguist languages none of which is the label (114: ALGOL 68 as `.alg`,
J as `.j`, Component Pascal as `.pas`); `ambiguous-ext` — claimed by two or more (133).

**Two thirds of the cases are in languages Linguist does not know** (1,075 of 1,589; 584 of the 848
languages): a Linguist-family tool cannot name them, nor can most others. Read the `in-linguist` column
(514 cases: 264 Rosetta Code languages, 251 Linguist languages).

**Rosetta Code's categories are fine-grained.** Each dialect, implementation and machine has its own
heading — BBC BASIC, Applesoft BASIC, Free Pascal/Lazarus, X86 Assembly, 6502 Assembly, ooRexx — and they are
not mapped to Linguist's broader names (BASIC, Pascal, Assembly, REXX): `BASIC` for a BBC BASIC program
counts as wrong. These are disagreements of granularity as much as errors.

**Snippets of a wiki, not files of projects.** A solution is a code block of a wiki page: mostly a whole
program, sometimes a fragment or a session transcript. Files under 3 non-blank lines are left out; 202 cases
have 3 or 4 (tag `tiny`).

**Training data.** Rosetta Code is in the training data of some classifiers: the Hugging Face models
`philomath-1209/programming-language-identification` (CodeBERTa-small fine-tuned on `cakiki/rosetta-code`,
26 languages) and `FrameByFrame/programming-language-identification-100plus` (ModernBERT on
`cakiki/rosetta-code` and The Stack, 107 languages) say so on their model cards — `contamination.json` marks
the entries whose name starts with `philomath-1209` or `FrameByFrame`; `cakiki/rosetta-code` is a 2022 copy
of the site, and how many of these 1,589 solutions it holds is not checked. GitHub's OctoLingua (2019) was
trained on Rosetta Code too (not runnable here), and so, most likely, was every large language model. No
case is byte-identical to a sample of Linguist (76f88c6) or of Hyperpolyglot (a55a3b5).

## The crosswalk (`labels.csv`)

One row per Rosetta Code language: its Linguist name(s), how it was found, why, and its population in the
dump (`files`: solutions; `eligible`: of 3+ non-blank lines and at most 100 KB; `cases`: sampled). The rule is
the one of `tools/external/*/names.csv` — **synonyms only**: another name or spelling of the same language
(`AWK` → Awk, `C sharp` → C#), a Linguist alias (`Mathematica` → Wolfram Language, `Delphi` → Pascal,
`Octave` → MATLAB, `Clipper` → xBase), a version (`XSLT 2.0` → XSLT, `AutoHotKey V2` → AutoHotkey), or a shell
Linguist files under a name by its interpreter (`Ksh` → Shell, `C Shell` → Tcsh). Where Linguist splits one
language in two, the label maps to both (`Fortran` → Fortran; Fortran Free Form, `Lean` → Lean; Lean 4,
`Sass/SCSS`). Dialects, implementations and broader or narrower names are not mapped.

| how | languages | |
|---|---:|---|
| exact | 219 | same name, case or punctuation aside (`Batch File` → Batchfile, `PL/SQL` → PLSQL) |
| alias | 19 | a Linguist alias, checked |
| manual | 32 | checked by hand; 3 found through PL-ultimate-llm's crosswalk (`pl.csv`: C sharp, F Sharp, Q Sharp) |
| none | 613 | not in Linguist under a synonym — among them 6 false friends overridden by hand |

Hard calls, and false friends a name match would get wrong:

- `Visual Basic` → **Visual Basic 6.0**: Rosetta Code's Visual Basic is classic VB (VB.NET has its own
  category); Linguist's alias `visual basic` points to Visual Basic .NET, `visual basic classic` to 6.0.
- `Nu` → **Nushell**: the category is Nushell's language, not Linguist's Nu (a Lisp on Objective-C).
- In these two cases the label itself is left out of the accepted names, since `tools/score.py` accepts
  every Linguist name of an accepted one (`Nu` would accept Linguist's Nu).
- `V` is the concatenative V, not Linguist's V (Vlang, Rosetta Code's `V (Vlang)`); `Go!` is not Go; `Astro`
  and `Blade` are programming languages, not the web formats Linguist names so; `Bird` is not BIRD2; `S-lang`
  is not Linguist's Slang (a shading language). Their expected name is qualified (`V (Rosetta Code)`) so
  that the namesake's answer does not count.
- `TI-83 BASIC` → TI Program (Linguist's TI-83/84 BASIC, `.8xp`); `TI-89 BASIC`, another dialect, is not
  mapped.
- `68000 Assembly` → Motorola 68K Assembly; the other assemblers (X86, ARM, 6502, Z80, …) are narrower than
  Linguist's Assembly and not mapped.
- `Free Pascal/Lazarus`, `PascalABC.NET`, `Object Pascal`: Linguist lists `delphi` and `objectpascal` as
  aliases of Pascal, so `Delphi` and `Object Pascal` map; Free Pascal and PascalABC.NET, implementations with
  dialects of their own, do not.
- PL-ultimate-llm's `pl.csv` was used as a second source and read row by row; it gets 5 of these languages
  wrong — Astro, Blade, Go! (→ Go), Nu (→ Nu), V (→ V) — and files C++ under the Rosetta Code name `ΜC++`.

## Composition

By the number of solutions a language has in the dump (the tail is where most languages are):

| solutions in the dump | languages | solutions | cases | languages in Linguist | cases in Linguist |
|---|---:|---:|---:|---:|---:|
| 1 | 82 | 82 | 66 | 13 | 11 |
| 2–5 | 180 | 563 | 285 | 29 | 47 |
| 6–20 | 192 | 2,114 | 380 | 42 | 84 |
| 21–100 | 209 | 10,219 | 418 | 74 | 148 |
| 101–500 | 136 | 29,723 | 272 | 53 | 106 |
| more than 500 | 84 | 100,756 | 168 | 59 | 118 |
| **all** | **883** | **143,457** | **1,589** | **270** | **514** |

The 100 largest languages hold 75 % of the solutions (J 3,397, Python 3,054, Java 2,305, Haskell 2,304, jq
2,288, …); the median language has 18. Sampling the same number per language makes this a benchmark of the
tail, not of the solutions one would meet at random.

| tag | cases | |
|---|---:|---|
| `in-linguist` / `not-in-linguist` | 514 / 1,075 | the label maps to a Linguist language, or not |
| `invented-ext` | 1,135 | the extension is claimed by no Linguist language |
| `misleading-ext` | 114 | claimed by Linguist languages, none of them the label's |
| `ambiguous-ext` | 133 | claimed by two or more Linguist languages |
| `tiny` | 202 | 3 or 4 non-blank lines |

## Findings

Every figure below is from the runs in `baselines/` and `entries/` (2026-10-03). Each identifier is run with
the file name and, where it reads names, without (`--content-only`: the file run as `file`); a tool that reads
the bytes only has a content-only column alone. Accuracy over the 1,589 cases, then over the 514 `in-linguist`
cases.

| entry | names: right | names: all / in-linguist | content only: right | content only: all / in-linguist |
|---|---:|---:|---:|---:|
| GitHub Linguist 9.7.0 | 330 | 20.8 % / 64.2 % | 6 | 0.4 % / 1.2 % |
| go-enry 2.9.6 | 326 | 20.5 % / 63.4 % | 6 | 0.4 % / 1.2 % |
| GitHub Linguist 7.30.0 | 324 | 20.4 % / 63.0 % | 6 | 0.4 % / 1.2 % |
| GitHub Linguist 8.0.0 | 323 | 20.3 % / 62.8 % | 6 | 0.4 % / 1.2 % |
| go-enry 2.8.9 | 322 | 20.3 % / 62.6 % | 6 | 0.4 % / 1.2 % |
| Synid 48c3c45 | 315 | 19.8 % / 56.2 % | 21 | 1.3 % / 3.7 % |
| linguist-js 3.0.4 | 310 | 19.5 % / 60.3 % | 6 | 0.4 % / 1.2 % |
| Synid 9bc1c32 | 309 | 19.4 % / 55.1 % |  |  |
| Hyperpolyglot a55a3b5 | 292 | 18.4 % / 56.8 % | 4 | 0.3 % / 0.8 % |
| Pygments 2.21.0 | 249 | 15.7 % / 46.9 % | 35 | 2.2 % / 6.4 % |
| Pygments 2.19.2 | 249 | 15.7 % / 46.9 % | 35 | 2.2 % / 6.4 % |
| Neovim 0.12.5 filetype | 244 | 15.4 % / 41.6 % | 8 | 0.5 % / 1.6 % |
| Pygments 2.14.0 | 239 | 15.0 % / 44.9 % | 32 | 2.0 % / 5.8 % |
| scc 4.1.0 | 228 | 14.3 % / 42.8 % |  |  |
| tokei 15.0.0 | 220 | 13.8 % / 41.2 % |  |  |
| cloc 2.10 | 215 | 13.5 % / 41.1 % |  |  |
| Chroma 2.27.0 | 201 | 12.6 % / 37.5 % | 8 | 0.5 % / 1.6 % |
| Rouge 5.1.0 | 178 | 11.2 % / 34.4 % | 6 | 0.4 % / 1.2 % |
| gengo 0.15.0 | 151 | 9.5 % / 29.4 % |  |  |
| ohcount 4.0.0 (Debian 4.0.0-5) | 128 | 8.1 % / 24.9 % | 6 | 0.4 % / 1.2 % |
| Universal Ctags 6.2.1 | 122 | 7.7 % / 23.3 % | 3 | 0.2 % / 0.6 % |
| Magika 1.0.3 |  |  | 101 | 6.4 % / 19.6 % |
| Guesslang 2.2.1 |  |  | 76 | 4.8 % / 14.8 % |
| vscode-languagedetection 1.0.23 |  |  | 58 | 3.7 % / 11.3 % |
| highlight.js 11.12.0 |  |  | 51 | 3.2 % / 9.5 % |
| Magika 0.5.1 |  |  | 40 | 2.5 % / 7.8 % |
| flourite 1.3.0 |  |  | 36 | 2.3 % / 6.6 % |
| file 5.46 (libmagic) |  |  | 20 | 1.3 % / 3.9 % |

- **Without the name — the fair reading — no identifier recognises Rosetta Code solutions.** The best is
  Magika 1.0.3: 101 cases (19.6 % of `in-linguist`), then Guesslang 2.2.1 (76) and VS Code's detector (58);
  Pygments' `guess_lexer` gets 35, Synid 48c3c45 21 (3.7 %), and the Linguist family 6 — Linguist 9.7.0
  answers nothing on 1,577 of the 1,589 files without a name.
- **With the name, the Linguist family reads the label back.** Linguist 9.7.0 is right on 329 of the 353
  `in-linguist` cases whose extension is a real one (`.py`, `.rs`), on 1 of the 161 whose extension acmeism
  invented (`.basic`, `.genie`), and on none of the 1,075 cases in languages it does not know: 330 in all
  (20.8 %). Its score measures acmeism's extension table more than the tool.
- **Synid 48c3c45: 315 with the name (56.2 % of `in-linguist`: 276 of 353 with a real extension, 13 of 161
  with an invented one), 21 without.** It is right on 26 cases in languages Linguist lacks (8th, BCPL, Icon, K,
  Uiua, …: Synid has syntaxes of its own); the next best there are Pygments, scc and tokei, with 8. Its fallbacks dominate its answers: `Text` on 696 files with the name
  and 918 without, `Vim script` on 155 and 224. 9bc1c32 → 48c3c45: 309 → 315.
- The Hugging Face classifiers trained on Rosetta Code (`philomath-1209`, `FrameByFrame`; † in the
  leaderboard) and PLangRec are run in a separate batch: see [LEADERBOARD.md](LEADERBOARD.md).

[COVERAGE.md](COVERAGE.md) gives, for every entry, the languages it can name and its accuracy on those;
[HISTORY.md](HISTORY.md) the Synid versions side by side.

## Files

| file | |
|---|---|
| `cases.csv` | one row per solution: path in the dump, git blob id, SWHID, expected language (Linguist's name, else Rosetta Code's), accepted names, tags, the language's population |
| `labels.csv` | the crosswalk, with each language's population |
| `build_cases.py` | fetches the dump and Linguist's `languages.yml` at pinned revisions, samples, writes `cases.csv`, `labels.csv` and `files/` |
| `card.json`, `contamination.json` | the benchmark card; the entries trained on Rosetta Code |
| `reproduce.sh` | rebuilds the benchmark and every entry |
| `baselines/`, `entries/` | Synid versions; Synid without the file name, other identifiers |
