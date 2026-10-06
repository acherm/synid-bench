# Diversifying synid-bench: findings

*2026-10-04. Eleven benchmarks, 24 other identifiers, Jev and Synid. Every figure comes from the stored runs:
[LEADERBOARD.md](LEADERBOARD.md) (every entry, intervals, failure triggers), [JEV.md](JEV.md) (Jev, failure by
failure), [TOOL-HISTORY.md](TOOL-HISTORY.md) (tools across their releases). Design and rationale:
[specs/benchmark-portfolio.md](specs/benchmark-portfolio.md); the literature review behind it:
[literature-review/](literature-review/deepresearch-claude/).*

## In short

Until now synid-bench had two benchmarks, each someone's home turf: Linguist's own samples, and 54 `.m` files
whose study fed the cascade's candidates. The literature has the same problem at large: nearly every
published accuracy for programming-language identification is agreement with a label that an extension table,
a repository language or Linguist itself produced. We added nine benchmarks that differ in what they measure
— human-checked files, author-declared Rosetta Code and hello-world programs, the example files of three
highlighters, population samples of three extensions from Software Heritage — gave each a card (unit, file
names, who labelled, sampling, home turf) and ran every identifier on every one of them.

The order of the tools depends on the benchmark: a tool wins where it was tuned; without an LLM, the file
name decides who wins; labels taken from a tool flatter it; a name derived from the label inflates every
name-based tool; and only samples of a real population show some failure classes. Held out of their home
turf, Jev choosing among PL-ultimate-llm's candidates, then among 2,140 languages, ranks first (75.7 %), Jev
over Linguist's 836 languages second (73.9 %), and Synid without its Pygments step is the best identifier
without an LLM (50.8 %), ahead of Linguist (48.3 %) and of Synid as shipped (45.8 %). None of the eleven benchmarks is held out, human-labelled, population-sampled, made of
whole files and focused on ambiguous extensions at once — which is what [bench-heldout](specs/bench-heldout.md)
is designed to be.

## The benchmarks

| benchmark | what | cases | unit · names | labels | home turf (†) |
|---|---|---:|---|---|---|
| [bench-m](benchmarks/bench-m/README.md) | `.m` files from Software Heritage | 54 | whole file · real | blind human review | the `.m` rules; the cascade |
| [bench-linguist](benchmarks/bench-linguist/README.md) | GitHub Linguist's samples | 3,404 | whole file · real | Linguist's maintainers | Linguist family; Synid on 2,271 files |
| [bench-smola](benchmarks/bench-smola/README.md) | one file per GitHub repository, 261 languages | 3,872 (1,107 gold) | whole file · real | a human (gold); Linguist (silver) | — |
| [bench-rosetta](benchmarks/bench-rosetta/README.md) | Rosetta Code solutions, 848 languages | 1,589 | snippet · derived from the label | the author | two Hugging Face classifiers |
| [bench-hello](benchmarks/bench-hello/README.md) | hello-world programs, ~1,000 languages | 1,009 | tiny program · extension only | contributors | — |
| [bench-pygments](benchmarks/bench-pygments/README.md) | Pygments' example files | 637 | whole file · real | Pygments' maintainers | Pygments |
| [bench-hljs](benchmarks/bench-hljs/README.md) | highlight.js' detection tests | 191 | snippet · none | highlight.js' maintainers | highlight.js |
| [bench-rouge](benchmarks/bench-rouge/README.md) | Rouge's samples and demos | 455 | snippet · none | Rouge's maintainers | Rouge |
| [bench-rpgle](benchmarks/bench-rpgle/README.md) | `.rpgle` files from Software Heritage | 760 | whole file · real | LLM judge + rules (silver) | the cascade |
| [bench-fsf](benchmarks/bench-fsf/README.md) | `.fsf` files from Software Heritage | 467 | whole file · real | LLM judge + rule (silver) | the cascade; the rule |
| [bench-cobol](benchmarks/bench-cobol/README.md) | `.cbl` files from Software Heritage | 605 | whole file · real | LLM judge + rules (silver) | the cascade; the rules |

## The leaderboard at a glance

Accuracy (%) on each benchmark, main configuration (with the file name), ranked by **held-out mean** — the mean
over the benchmarks an identifier ran on, leaving out its home turf. **Bold**: best on the benchmark, home turf
aside. † home turf. ‡ accuracy on the cases the tool was not built from. n/a: needs a file name, the benchmark
has none. The README carries the same table, regenerated with the leaderboard.

| # | identifier | held-out mean | m | smola | linguist | pygments | rpgle | cobol | fsf | hello | rosetta | hljs | rouge |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Jev 1.13, cascade, fallback over 2,140 languages | 75.7 | 100 † | 89 | **96** | 82 | 99 † | 91 † | 90 † | **36** | 55 † | 76 | 75 |
| 2 | Jev 1.13, Linguist's 836 languages | 73.9 | **93** | **92** | 93 | 70 | **99** | **93** | 68 | 26 | 31 | 74 | 74 |
| 3 | Jev 1.13, PL-ultimate-llm candidates (cascade) | 69.2 | 100 † | 89 | 96 | 82 | 99 † | 91 † | 88 † | 31 | **35** | **77** | **75** |
| 4 | Synid 48c3c45, Pygments step off | 50.8 | 76 | 79 | 61 ‡ | **87 ‡** | **99** | 91 | 0 | 28 | 22 | 8 | 7 |
| 5 | GitHub Linguist 9.7.0 | 48.3 | 87 | 87 | 100 † | 67 ‡ | **99** | 91 | 0 | 27 | 21 | 2 | 3 ‡ |
| 6 | go-enry 2.9.6 | 48.0 | 87 | 86 | 96 † | 66 ‡ | **99** | 91 | 0 | 26 | 21 | 2 | 3 ‡ |
| 7 | Synid 48c3c45 | 45.8 | 61 | 61 | 56 ‡ | 82 ‡ | **99** | 91 | 1 | 23 | 20 | 6 | 4 |
| 8 | linguist-js 3.0.4 | 45.5 | 70 | 79 | 95 † | 66 | **99** | 91 | 0 | 25 | 20 | 2 | 2 |
| 9 | cloc 2.10 | 37.0 | 87 | 48 | 34 | 43 | 0 | 91 | 0 | 17 | 14 | n/a | n/a |
| 10 | scc 4.1.0 | 34.1 | 74 | 41 | 28 | 42 | 0 | 91 | 0 | 17 | 14 | n/a | n/a |
| 11 | FrameByFrame (Hugging Face) | 34.1 | 48 | 31 | 21 | 22 | 0 | 88 | 64 | 9 | 13 † | 32 | 25 |
| 12 | Neovim 0.12.5 filetype | 33.7 | 59 | 44 | 35 | 47 | **99** | 45 | 0 | 17 | 16 | 3 | 4 |
| 13 | Hyperpolyglot a55a3b5 | 33.5 | 83 | 80 | 10 ‡ | 60 ‡ | 0 | 91 | 0 | 23 | 18 | 2 | 2 |
| 14 | Magika 1.0.3 | 33.0 | 70 | 28 | 25 | 19 | 0 | 56 | **93** | 5 | 6 | 33 | 27 |
| 15 | Rouge 5.1.0 | 31.8 | 57 | 44 | 27 | 38 | 0 | 91 | 35 | 12 | 11 | 2 | 6 † |
| 16 | Pygments 2.21.0 | 26.3 | 35 | 52 | 32 | 94 † | 0 | 91 | 0 | 20 | 16 | 9 | 7 |
| 17 | tokei 15.0.0 | 26.0 | 15 | 35 | 24 | 40 | 0 | 91 | 0 | 16 | 14 | n/a | n/a |
| 18 | Guesslang 2.2.1 | 25.2 | 67 | 22 | 22 | 16 | 0 | 86 | 9 | 4 | 5 | 27 | 20 |
| 19 | Universal Ctags 6.2.1 | 22.6 | 74 | 27 | 15 | 22 | 0 | 91 | 0 | 9 | 8 | 1 | 2 |
| 20 | Chroma 2.27.0 | 22.2 | 7 | 36 | 23 | 48 ‡ | **99** | 0 | 0 | 15 | 13 | 2 | 1 ‡ |
| 21 | vscode-languagedetection 1.0.23 | 21.3 | 63 | 22 | 19 | 13 | 0 | 63 | 9 | 2 | 4 | 25 | 15 |
| 22 | ohcount 4.0.0 (Debian 4.0.0-5) | 16.8 | 80 | 34 | 19 | 27 | 0 | 2 | 0 | 10 | 8 | 3 | 2 |
| 23 | philomath-1209 (Hugging Face) | 13.2 | 9 | 9 | 10 | 10 | 0 | 66 | 0 | 3 | 3 † | 14 | 10 |
| 24 | PLangRec 3fb01dd | 10.9 | 59 | — | 13 | 10 | 0 | 0 | 0 | 3 | 2 | 13 | 8 |
| 25 | gengo 0.15.0 | 10.3 | 7 | 25 | 17 † | 30 | 0 | 0 | 0 | 11 | 10 | n/a | n/a |
| 26 | file 5.46 (libmagic) | 9.4 | 15 | 12 | 16 | 7 | 0 | 9 | 27 | 3 | 1 | 7 | 7 |
| 27 | highlight.js 11.12.0 | 7.0 | 9 | 13 | 9 | 14 | 0 | 0 | 0 | 3 | 3 | 73 † | 19 |
| 28 | flourite 1.3.0 | 5.0 | 2 | 9 | 8 | 8 | 0 | 0 | 0 | 3 | 2 | 15 | 8 |
| 29 | CodeBERTa-language-id (Hugging Face) | 1.6 | 0 | 2 | 4 | 3 | 0 | 0 | 0 | 0 | 1 | 5 | 2 |

## Findings

**0. Overall.** Held out, the candidates + Jev cascade with its fallback widened to 2,140 languages ranks first
(75.7 %, over the 6 benchmarks that are not its home turf; 80.5 % of all cases pooled), then Jev over
Linguist's 836 languages (73.9 % with the file name, 71.8 % without, held out on all 11; on the 6 benchmarks
held out for both, 71.5 % against the wide cascade's 75.7 %), then the cascade with its original fallback
(69.2 %), then Synid without its Pygments step (50.8 %), Linguist
(48.3 %), go-enry (48.0 %) and Synid as shipped (45.8 %); then linguist-js (45.5 %), cloc (37 %), Magika (33 %). The Jev entries are the only ones ahead on both kinds of
benchmark, with names and without.

**1. A benchmark crowns the tool that was tuned on it — for the task it was tuned for.** highlight.js 11.9.0
gets 187/191 (97.9 %) on its own auto-detection tests, which its test suite required it to pass until March
2024; the Jev cascade gets 77.5 %, the best other tool without an LLM (Magika) 33 %, and highlight.js'
mean elsewhere is 7 %. Pygments is first on its example files (93.7 %; 26 % held out); Linguist on its
samples (99.5 %; 48 % held out). Rouge is the exception that confirms the rule: 24th of 44 on its own
samples, which its tests only *lex* — they never ask it to guess. Home turf is a matter of what was tuned,
not of who wrote the files. Within bench-linguist, Synid is right on 76.6 % of all files but 56.1 % of
those its classifier never saw.

**2. Without the LLM entries, the file name decides who wins.** Kendall's τ between the orders the benchmarks
give to the entries: 0.6–0.9 between benchmarks with file names (bench-m, linguist, smola, pygments, hello,
rosetta, cobol; 0.3–0.5 with rpgle, where every name-based tool ties), 0.5–0.9 between the three without
(hljs, rouge, fsf), −0.1 to +0.4 across the two groups. Among the tools that do not call an LLM, the
Linguist family and Synid lead every benchmark with names; a content classifier leads every benchmark
without (Magika: 92.5 % on fsf, 33 % on hljs, 27.5 % on rouge), where the Linguist family and Synid fall
to 0–6 % and the name-only tools cannot answer. A leaderboard over one kind of benchmark says little about the other kind.

**3. Labels taken from a tool are a gift to that tool.** On bench-smola, Linguist 9.7.0 agrees with the silver
labels — Linguist's own 2022 answers — on 99.6 % of the files, and with the human on 87.4 % of the gold ones.
On the 167 files where the human corrected Linguist, Linguist 7.30.0 gives its 2022 answer again on 161 and
9.7.0 is right on 38; Jev over Linguist's languages is right on 135 (130 without the name), Magika on 74,
the cascade on 75–85 (its candidates come from the misleading extension), Synid on 9.

**4. A name that carries the label inflates every name-based tool — and an LLM.** On bench-rosetta, whose
file names come from the language through acmeism's extension table, Linguist is right on 329 of the 353
files (of languages it knows) with a real extension and on 1 of the 161 with an invented one; Jev gains 125
of the 514 such files when shown the name (490 vs 365). On bench-hello's 186 programs with a misleading
extension (`Pebble.c`), no entry does better than 11 (the cascade).

**5. Samples of a real population contain failure classes that curated sets lack.** bench-cobol: synthetic
stubs and reading lists named `.cbl` — every name-based tool is wrong on all of them, which weighs
heavily once the sample is weighted back to the archive (56.5 % weighted for the best rule-based tools).
bench-fsf: a non-programming format — Synid answers ALGOL 68 on all 300 FEAT designs (3/467 right), Magika
92.5 %. bench-rpgle: every tool that reads the name is right (99.3 %); from the content alone, only Jev (an LLM)
recognises RPG.

**6. Tools regress between releases too.** highlight.js 11.9.0 (the last release whose test suite checked
detection) → 11.12.0 regresses on every benchmark: −49 / +1 on its own test files, −164 / +6 on
bench-linguist, −317 / +19 on bench-smola (two grammars, Dart and DNS Zone, now win on almost anything); Magika 0.5.1 → 1.0.3: +361 / −71 on
bench-linguist; Pygments 2.14 → 2.19 without names: +8 / −13 (a new Carbon lexer takes C files); Linguist's
switch to a centroid classifier (7.30.0 → 8.0.0) changed 37 answers on bench-linguist, +33 / −0.

**7. Coverage bounds everything.** Two thirds of bench-rosetta's cases are in languages Linguist does not know;
a tool's label set (6 to ~1,100 names) caps its score before its skill does — `COVERAGE.md` separates the two.

**8. Specific benchmarks find specific bugs.** In Synid: `Text` as the default answer (most of its misses
on every benchmark), the ALGOL 68 answer on `.fsf`, rule names that do not match candidate names
(`PLpgSQL`; 12 regressions on bench-smola), and one nondeterministic answer (HTML or ERB on hljs'
`xml/default.txt` across runs). In other tools: linguist-js' conversion of possessive regexes (its Adblock
heuristic can never match), Chroma's GDScript analyser that scores 0.2 on almost any text, ohcount's crashes.

## Jev: where it shines, where it fails

Jev is TypeSafe's lightweight decision model, asked which of Linguist's 836 languages a file is written in (a
knockout over four groups of ~209 names, then a final). Details, failure by failure: [JEV.md](JEV.md).

- **Overall**: Jev is right on 73.3% of the cases, Synid on 55.7%, Linguist on 65.7%; all the identifiers without an LLM taken together (right when any one is) on 79.9%.
- **Where it shines**: files a human corrected Linguist on (`human-overrode-linguist`: 80.8%, Synid 5.4%); files Synid's classifier was not trained on (bench-linguist's `unseen`: 92.9%, Synid 56.1%); tiny files (`tiny`: 53.1%, Synid 18.0%); files without a name (bench-hljs 73.8%, bench-rouge 74.1%; Synid 5.8% and 4.0%).
- **Where it fails**: the label set first — 2084 of its 2744 misses are languages outside Linguist's 836 (`not-in-linguist`: 0.0%, Synid 8.8%); then the knockout (555 lost in a group or in the final, 105 with no answer); and a name can mislead it — on bench-fsf it is right on 67.9% with the file name and 84.2% without.
- **Against Synid**: 2206 cases Jev right and Synid wrong, 396 the reverse; where Synid answers `Text` on code, Jev is right on 51.8%.

Combining it with Synid, pooled over the 10,278 headline cases:

| policy | right | Jev asked on |
|---|---:|---:|
| Synid alone | 5724/10278 (55.7%) | 0% |
| Synid first, then Jev | 6983/10278 (67.9%) | 24.2% |
| Jev alone | 7534/10278 (73.3%) | 100% |
| Jev, then Synid where Jev gives no answer | 7657/10278 (74.5%) | 100% |

Synid adds about a point as a fallback where Jev gives no answer; asking Synid first saves three quarters of
the paid calls but keeps Synid's wrong answers.

**Does Jev know when it is wrong? Largely.** With every probability kept (the wide-fallback cascade, 10,051
answers), confidence separates right from wrong answers well (AUROC 0.88): abstaining below 0.9 keeps 76 % of
the answers at 94.1 % accuracy and avoids 74 % of the wrong ones. The confident failures remain: 11.5 % of the
wrong answers come with ≥ 0.99, mostly files whose language was not among the options, where Jev picks the
nearest one with conviction (OoRexx → REXX). A probability ranks the options given; it cannot tell that the
right one was missing. (Runs before 2026-10-04 kept only part of the probabilities: AUROC 0.83 on the first
cascade's decisions among candidates, 0.76 on the knockout's finals.)

**A richer list? Yes.** 54 % of the 2,084 files Jev loses for want of the language in Linguist's list are in
PL-ultimate-llm's taxonomy (12,628 languages, mostly through the Esolang wiki and PLDB). Widening the cascade's
fallback from 1,238 to 2,140 languages — Linguist, Pygments, Rosetta Code, Wikipedia, Wikidata and
Hyperpolyglot's, plus every language with an extension; the Esolang wiki and PLDB left out — recovers 580 of
them (195 before), and lifts the cascade from 76.8 % to 80.5 % of all cases: bench-rosetta 34.7 → 54.9 % (a
label-set home turf: Rosetta Code's names are in the list, so it is marked †), bench-hello 30.6 → 35.9 %,
the rest within a point (slightly down where every file goes to the fallback: more rivals). It costs 10
calls per fallback file instead of 7 ($15 for the whole portfolio). Jev costs about $1 per 1,000 files (5 calls each); these runs
cost $50 (the cascade $9, its wide fallback $15, Jev over the 836 languages $26).

## For Synid

- **Turn the Pygments step's default off** — or return the candidates instead of `Text` when no rule decides:
  +5 points held out (45.8 → 50.8 %), +17 on bench-smola's human-checked files (61.3 → 78.5 %). The cost:
  more wrong languages where it used to say `Text` (on bench-linguist, its language answers are right
  85.8 % of the time instead of 92.2 %).
- **Fix the `.fsf` answer** (ALGOL 68 on all 300 FEAT designs, from the `comment` strategy), the **rule names
  that do not match candidate names** (`PLpgSQL`, the Wolfram rule), and the **nondeterministic answer** on
  highlight.js' `xml/default.txt` (HTML or ERB from one run to the next).
- **Where it loses most to Jev**: files a human corrected Linguist on (5 % vs 81 %), files its classifier
  never saw (56 % vs 93 % on bench-linguist's `unseen`), tiny files (18 % vs 53 %), files without a name.
- **Where it beats Jev**: languages outside Linguist's list — Synid's catalogue (~1,100 syntaxes) names some
  that Jev cannot (184 of the 396 cases where Synid is right and Jev wrong).

## What it implies for the benchmark we need

The portfolio is a map of biases, each measured. A benchmark that is to rank identifiers on the files they
will actually meet — Software Heritage's — must control each one, and [bench-heldout](specs/bench-heldout.md)'s
design follows from the findings above:

| finding | what bench-heldout must do |
|---|---|
| 1. home turf: 20 points (Synid, seen vs unseen files) to 90 (highlight.js, its tests vs elsewhere) | files no tool, mapping or rule set was built from, by construction and checked by blob id; rules and mappings frozen before labels are seen |
| 2. the name decides the order | stratify by kind of name (ambiguous / single claimant / unclaimed / none); score every entry with the name, without it, and with a misleading one |
| 3. tool-derived labels inflate the tool | labels from a blind human review, never from a tool or an LLM; double coding of a sample, with agreement |
| 4. label-derived names leak | real archived names only |
| 5. failure classes only a population has | a probability sample of the archive, with weights; not-code and generated files kept |
| 6. tools regress | frozen, versioned cases; every tool pinned and rerun on new releases (`tools/run_all.py`) |
| 7. coverage bounds skill | taxonomy fixed up front (PL-ultimate-llm concepts with Linguist names and accept lists); report coverage apart |

The existing benchmarks keep their use: as non-regression suites (each tool's release history), as
diagnostics (each one isolates a regime — content only, misleading names, a hard extension, the long tail),
and as the evidence for the design above. What none of them can give is the number Software Heritage needs:
how often an identifier is right on a file drawn from the archive.

## Limits

- Three benchmarks (rpgle, fsf, cobol) have labels from an LLM judge, not yet audited by a human: they favour
  the LLM entries. bench-smola's gold tier is one annotator, on files chosen where Linguist named a language.
- Held-out means average benchmarks of different sizes and natures, and over different subsets for different
  entries (an entry's home turf is left out); read them with the per-benchmark columns.
- Not run everywhere, for cost: Kev-4B and StarCoder2-3B (local, slow), PLangRec on bench-smola.
- The pass-1 literature review hit its search budget; its figures are to be re-checked before citing.

## Reproduce

```bash
python3 benchmarks/<bench>/build_cases.py          # each benchmark, from pinned sources
python3 tools/run_all.py --synid path/to/synid     # every identifier on every benchmark (Docker), what is missing
python3 tools/jev_cascade.py benchmarks/<bench>    # and tools/jev_linguist.py: Jev (OpenRouter key)
python3 tools/leaderboard.py && python3 tools/jev_report.py && python3 tools/tool_history.py
```
