# bench-hello — a hello-world program in every language

The long tail in its smallest form: **the 1,009 programs of
[leachim6/hello-world](https://github.com/leachim6/hello-world)**, one per language (1,002 labels, from
`!` to `Zsq`), each labelled by the language its contributor named the file after. A tiny program shows
little more than a language's surface — how it prints a string — which is what an identifier must know to
tell 965 languages apart.

| | |
|---|---|
| cases | 1,009 programs (every file of `<initial>/`, the README, licence and the images of `t/` left out); 1,002 labels, 965 expected languages once mapped |
| labels | the file's stem, chosen by the contributor (author-declared), with the repository's own substitutions (`∗` for `*`, `˸` for `:`); mapped to Linguist's name for synonyms only ([`labels.csv`](labels.csv)); a case is right when the answer is that name, one of its Linguist aliases, or the label |
| source | [leachim6/hello-world](https://github.com/leachim6/hello-world) at [`a152253b102999bf31988fef077101022e2ad1a5`](https://github.com/leachim6/hello-world/tree/a152253b102999bf31988fef077101022e2ad1a5) (2026-01-20); Linguist's `languages.yml` at `76f88c6` for the crosswalk |
| file names | the stem *is* the label, so each file is run as `hello<ext>` with the contributor's extension (`Pebble.c` → `hello.c`); without extension, as `hello`; the original path is in `path` |
| files | **not stored here** (MIT-licensed, but kept out like every benchmark's files): `build_cases.py` fetches the repository at the pinned commit and checks each file against its git blob id |

```bash
python3 benchmarks/bench-hello/build_cases.py          # fetch the files (and rebuild cases.csv, identical)
python3 tools/run.py benchmarks/bench-hello --synid path/to/synid --label mytest
python3 tools/score.py benchmarks/bench-hello/results/mytest.jsonl \
    --baseline benchmarks/bench-hello/baselines/48c3c45-default.jsonl
```

`build_cases.py --cache DIR` (or `$BENCH_CACHE`) sets where the repository is fetched (default `.work/`).
Every case has a SWHID with the repository as origin; the contents are archived by Software Heritage (4 of
4 checked through its API, including the last program added, `Koka.kk`).

## Read it with care

**Tiny.** Half the programs have one or two non-blank lines (median: 2). Many are the same bytes under
several labels — `print("Hello World")` is a program in 15 of them, `"Hello World"` in 13: **109 cases share
their bytes with a program of another language** (tag `shared-bytes`); no reading of the content can get
all of them right.

**Most labels are not Linguist languages** (704 of 1,009 cases): esoteric languages, dialects, one-person
projects, jokes (`Your Mom`, `Mostawesomeprograminglanguage`). Read the `in-linguist` column (305 cases, 261
Linguist languages).

**The extension is the contributor's choice, and sometimes another language's.** `Pebble.c`, `BIRL.c`,
`Panther.py`, `Assembler 6502.asm`: 186 cases have an extension claimed by Linguist languages none of which is
the label (`misleading-ext`). Two kinds are mixed there: a language borrowing a host's extension (`Pebble.c`,
`Panther.py`), and a label that names no language at all — `Flask.py`, `React.js`, `Android.java`,
`Node.js.js` — where the file is written in the language the extension names (tag `not-a-language`: 52
labels naming a framework, library, platform, runtime, implementation or protocol). On the latter, the
"wrong" answer (Python for `Flask.py`) is the right language. 123 programs have no extension (`no-ext`).

**Not all are text.** 13 files have a NUL byte in their first 8 KB (`binary`): Piet, Brainloller and MOONBlock
programs are images; Scratch, App Inventor and Catrobat projects are archives or binary files;
`Executable.exe` is a Windows executable; `ThotPatrol.txt` is UTF-16 text.

**Training data.** No case is byte-identical to a sample of Linguist (76f88c6) or of Hyperpolyglot
(a55a3b5). The repository has been public since 2008 (about 12,000 stars and 2,100 forks on GitHub in October
2026): large language models have most likely seen it; no identifier run here says it was trained on it.

## The crosswalk (`labels.csv`)

One row per label: its Linguist name(s), how it was found, why, and how many programs carry it. The rule is
the one of `tools/external/*/names.csv` — **synonyms only**: another name or spelling of the same language
(`CSharp` → C#, `Modula 2` → Modula-2, `4th Dimension` → 4D), a Linguist alias (`Perl6` → Raku, `Bash` →
Shell, `Mumps` → M), a former name (`Jade` → Pug, `daScript` → Daslang, `Coq` → Rocq Prover), a version
(`Python 2`, `Python 3` → Python, `Fortran77` → Fortran, `ActionScript 2` → ActionScript), or a shell
Linguist files under a name by its interpreter (`KSH` → Shell, `C Shell` → Tcsh). Where Linguist splits one
language in two, the label maps to both (`Fortran` → Fortran; Fortran Free Form, `Lean` → Lean; Lean 4).
Dialects, implementations, frameworks and broader or narrower names (`Assembler MASM DOS` vs Assembly,
`MySQL` vs SQL, `CLISP` vs Common Lisp, `Node.js` vs JavaScript) are not mapped.

| how | labels | |
|---|---:|---|
| exact | 222 | same name, case or punctuation aside (`Objective C` → Objective-C, `SmallTalk` → Smalltalk) |
| alias | 34 | a Linguist alias, checked |
| manual | 43 | checked by hand, file in hand |
| none | 703 | not in Linguist under a synonym — among them 10 false friends overridden by hand |

Hard calls, and false friends a name match would get wrong (their expected name is qualified, `Monkey
(hello-world)`, so that the namesake's answer does not count):

- `Monkey` (`puts("Hello World")`) is the language of *Writing an Interpreter in Go*, not Linguist's Monkey
  (Monkey X); `Tea` (`echo`) is not Linguist's Tea (a template language); `OX.oz` is Oz code, not Linguist's
  Ox; `IRC` is an mIRC command, not an IRC log; `HTTP` and `Django` are Python files, not Linguist's HTTP or
  Jinja (alias `django`); `C--`, `D♭♭`, `Cω` and `@text` are not C, D or Text.
- `V` labels two files: `V.v` is Vlang (Linguist's V), `V` (`iHello World`) another V, not mapped.
- `Cil` and `Il` (`.il`, `.assembly …`) → IL Assembly: .NET's Common Intermediate Language; Linguist's `CIL`
  is SELinux's — so `Cil` is left out of the accepted names (`tools/score.py` accepts every Linguist name of an
  accepted one).
- `Assembler NASM …` (6 programs) → Assembly, since `nasm` is a Linguist alias; MASM, TASM, FASM and the
  other machines are narrower than Linguist's Assembly and not mapped; `Assembler m68000 amigaos` →
  Motorola 68K Assembly.
- `Visual Basic` (`.vb`, `Module … End Module`) → Visual Basic .NET, as Linguist's alias says (on
  bench-rosetta the same name is classic VB).
- `Inform` (the file is Inform 7) → Inform 7; `dBase`, `XBase++`, `VisualFoxPro` → xBase, the family Linguist
  names after dBase (aliases clipper, foxpro); `dos` → Batchfile.
- PL-ultimate-llm's crosswalk adds nothing right here; it maps `F` (a subset of Fortran 95) to F*.

## Composition

| tag | cases | |
|---|---:|---|
| `in-linguist` / `not-in-linguist` | 305 / 704 | the label maps to a Linguist language (270 programming, 19 markup, 11 data, 5 prose), or not |
| `misleading-ext` | 186 | the extension is claimed by Linguist languages, none of them the label's |
| `ambiguous-ext` | 181 | claimed by two or more Linguist languages |
| `no-ext` | 123 | no extension |
| `not-a-language` | 52 | the label names a framework, library, platform, runtime, implementation or protocol |
| `shared-bytes` | 109 | the same bytes are filed under another language |
| `binary` | 13 | not text |

## Findings

Every figure below is from the runs in `baselines/` and `entries/` (2026-10-03). Each identifier is run with
the file name (`hello<ext>`) and, where it reads names, without (`--content-only`: the file run as `file`); a
tool that reads the bytes only has a content-only column alone. Accuracy over the 1,009 cases, then over the
305 `in-linguist` cases and the 186 `misleading-ext` ones.

| entry | names: right | names: all / in-linguist / misleading-ext | content only: right | content only: all / in-linguist / misleading-ext |
|---|---:|---:|---:|---:|
| GitHub Linguist 9.7.0 | 270 | 26.8 % / 88.5 % / 0.0 % | 19 | 1.9 % / 6.2 % / 0.0 % |
| go-enry 2.9.6 | 263 | 26.1 % / 86.2 % / 0.0 % | 19 | 1.9 % / 6.2 % / 0.0 % |
| GitHub Linguist 8.0.0 | 260 | 25.8 % / 85.2 % / 0.0 % | 19 | 1.9 % / 6.2 % / 0.0 % |
| GitHub Linguist 7.30.0 | 258 | 25.6 % / 84.6 % / 0.0 % | 19 | 1.9 % / 6.2 % / 0.0 % |
| linguist-js 3.0.4 | 256 | 25.4 % / 83.9 % / 0.0 % | 18 | 1.8 % / 5.9 % / 0.0 % |
| go-enry 2.8.9 | 255 | 25.3 % / 83.6 % / 0.0 % | 19 | 1.9 % / 6.2 % / 0.0 % |
| Synid 48c3c45 | 231 | 22.9 % / 68.9 % / 0.5 % | 20 | 2.0 % / 6.6 % / 0.0 % |
| Synid 9bc1c32 | 229 | 22.7 % / 68.2 % / 0.5 % |  |  |
| Hyperpolyglot a55a3b5 | 228 | 22.6 % / 74.8 % / 0.0 % | 17 | 1.7 % / 5.6 % / 0.0 % |
| Pygments 2.21.0 | 206 | 20.4 % / 61.6 % / 3.2 % | 25 | 2.5 % / 7.9 % / 0.0 % |
| Pygments 2.19.2 | 204 | 20.2 % / 61.0 % / 3.2 % | 24 | 2.4 % / 7.5 % / 0.0 % |
| Pygments 2.14.0 | 193 | 19.1 % / 58.0 % / 2.7 % | 23 | 2.3 % / 7.2 % / 0.0 % |
| scc 4.1.0 | 176 | 17.4 % / 54.4 % / 0.5 % |  |  |
| Neovim 0.12.5 filetype | 175 | 17.3 % / 52.1 % / 1.1 % | 16 | 1.6 % / 5.2 % / 0.0 % |
| cloc 2.10 | 172 | 17.0 % / 55.1 % / 1.1 % |  |  |
| tokei 15.0.0 | 165 | 16.4 % / 51.1 % / 0.5 % |  |  |
| Chroma 2.27.0 | 147 | 14.6 % / 47.2 % / 1.1 % | 8 | 0.8 % / 2.6 % / 0.0 % |
| Rouge 5.1.0 | 126 | 12.5 % / 40.3 % / 0.5 % | 19 | 1.9 % / 6.2 % / 0.0 % |
| gengo 0.15.0 | 110 | 10.9 % / 35.4 % / 0.5 % |  |  |
| Universal Ctags 6.2.1 | 95 | 9.4 % / 29.5 % / 0.5 % | 12 | 1.2 % / 3.6 % / 0.0 % |
| ohcount 4.0.0 (Debian 4.0.0-5) | 94 | 9.3 % / 30.5 % / 0.5 % | 9 | 0.9 % / 3.0 % / 0.0 % |
| FrameByFrame/programming-language-identification-100plus da6a18b |  |  | 91 | 9.0 % / 29.8 % / 1.1 % |
| Magika 1.0.3 |  |  | 55 | 5.5 % / 18.0 % / 0.5 % |
| Magika 0.5.1 |  |  | 40 | 4.0 % / 13.1 % / 0.0 % |
| Guesslang 2.2.1 |  |  | 39 | 3.9 % / 12.8 % / 0.0 % |
| flourite 1.3.0 |  |  | 33 | 3.3 % / 9.8 % / 1.6 % |
| highlight.js 11.12.0 |  |  | 33 | 3.3 % / 10.5 % / 0.5 % |
| philomath-1209/programming-language-identification 9090d38 |  |  | 31 | 3.1 % / 10.2 % / 0.5 % |
| file 5.46 (libmagic) |  |  | 27 | 2.7 % / 8.9 % / 0.0 % |
| vscode-languagedetection 1.0.23 |  |  | 17 | 1.7 % / 5.6 % / 0.0 % |
| huggingface/CodeBERTa-language-id 67e92a9 |  |  | 4 | 0.4 % / 1.3 % / 0.0 % |

- **With the name, the Linguist family leads** — Linguist 9.7.0 is right on 270 programs (88.5 % of
  `in-linguist`), go-enry 2.9.6 on 263, Linguist 8.0.0 and 7.30.0 on 260 and 258, linguist-js on 256 — ahead
  of Synid 48c3c45 (231; 68.9 % of `in-linguist`), Hyperpolyglot (228) and Pygments 2.21.0 (206). Synid is
  right on 21 programs in languages Linguist lacks (Aheui, Arturo, BBC BASIC, K, Rockstar, …).
- **An extension that belongs to another language defeats every tool**: on the 186 `misleading-ext` cases the
  best is Pygments with 6; Linguist gets none. On 47 of them the label is not a language (`not-a-language`):
  Linguist names the language the file is in instead (Python for `Flask.py` 19 times, JavaScript for
  `React.js` 9 times) — wrong by the label, right by the bytes.
- **Without the name, a hello-world program is almost never identified.** The best content-only entry is
  FrameByFrame's ModernBERT classifier (91 programs; 29.8 % of `in-linguist`), then Magika 1.0.3 (55),
  Guesslang (39), highlight.js and flourite (33); Pygments' `guess_lexer` gets 25, Synid 48c3c45 20, the
  Linguist family 19 (it answers rarely: when it does, it is right 68 % of the time). A program of one or two
  lines carries little more than a print call.
- **Synid's fallbacks**: `Text` on 414 programs with the name and 510 without, `Vim script` on 166 and 345 —
  with the name, 9 of the 13 programs that are just `"Hello World"` (a double quote opens a Vim script
  comment). 9bc1c32 → 48c3c45: 229 → 231.
- On the 109 `shared-bytes` cases, Linguist is right on 35 (the extension decides), every content-only run
  on 5 or fewer.
- PLangRec is run in a separate batch: see [LEADERBOARD.md](LEADERBOARD.md).

[COVERAGE.md](COVERAGE.md) gives, for every entry, the languages it can name and its accuracy on those;
[HISTORY.md](HISTORY.md) the Synid versions side by side.

## Files

| file | |
|---|---|
| `cases.csv` | one row per program: original path, git blob id, SWHID, expected language (Linguist's name, else the label), accepted names, tags |
| `labels.csv` | the crosswalk, with the number of programs per label |
| `build_cases.py` | fetches the repository and Linguist's `languages.yml` at pinned revisions, writes `cases.csv`, `labels.csv` and `files/` |
| `card.json` | the benchmark card |
| `reproduce.sh` | rebuilds the benchmark and every entry |
| `baselines/`, `entries/` | Synid versions; Synid without the file name, other identifiers |
