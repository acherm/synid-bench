# Spec — a portfolio of benchmarks, and what it says about building a better one

*Written 2026-10-03, after the [literature review](../literature-review/deepresearch-claude/Programming%20language%20identification%20benchmarks.md)
(pass 1; 83 benchmarks and datasets). Status: wave 1 built (see "Portfolio"); results in [LEADERBOARD.md](../LEADERBOARD.md).*

## Why more benchmarks

bench-m and bench-linguist were enough to compare Synid versions, not to say how good an identifier is.
Each is someone's **home turf**: bench-linguist is the training data of the Linguist family and of Synid's
classifier; bench-m comes from the `.m` study whose observations entered the cascade's candidates. One is
54 files of one extension. The literature review finds the same pattern everywhere: nearly every published
accuracy is agreement with a label that an extension table, a repository language or Linguist produced —
the signals the tools under test already use — and no benchmark is at once held out, human-labelled per
file, population-sampled, made of whole files and focused on ambiguous extensions.

A portfolio does three things a single benchmark cannot:

1. **Non-regression for any identifier, not only Synid.** Each benchmark is frozen and versioned; a tool's new
   release is run on all of them and compared with the last (`tools/score.py` for Synid,
   `tools/tool_history.py` for the other tools' versions).
2. **A leaderboard that knows what each benchmark measures.** Each benchmark has a card (`card.json`): the
   unit (whole file, snippet, tiny program), whether files keep a real name, who labelled them, how they were
   chosen, and whose training or development data they are (`contamination.json`, †). The overall ranking
   leaves each entry's home turf out.
3. **Evidence for the benchmark we actually need.** Running every identifier on every benchmark shows how far
   the order of the tools depends on the benchmark — and therefore what a held-out benchmark must control
   ([bench-heldout](bench-heldout.md)).

## The qualities a benchmark is described by

The card's fields, and the property of [bench-heldout](bench-heldout.md) each one approximates:

| field | values | why it matters | bench-heldout |
|---|---|---|---|
| unit | whole file / snippet / tiny program | content classifiers degrade on short inputs; rule-based tools need whole files (shebangs, headers) | whole files |
| file names | real / label-derived / none | rule-based tools live on the name; a name derived from the label leaks it; no name tests content only | real, plus content-only runs |
| labels | human / author-declared / maintainers / LLM judge / tool | a label produced by a tool under test is circular; an LLM judge favours LLM entries | P3: blind human, double-coded sample |
| sampling | curated / all / random per language / population-sampled with weights | curated sets over-represent what their curators test; only a population sample gives an error rate for the archive | P2: stratified by kind of name, weighted |
| home turf | entries built, trained or tuned on the files | the score is then partly recall of training data | P1: excluded by construction |
| languages | count, and how many are outside Linguist | coverage vs label set; the long tail | oversample rare languages |

## Portfolio

Built (wave 1) — each with a README (strengths, weaknesses, findings), a card, a build script pinned to a
commit that rebuilds identical cases, and every free entry run on it:

| benchmark | cases · languages | unit · names | labels | sampling | home turf (†) |
|---|---|---|---|---|---|
| [bench-m](../benchmarks/bench-m/README.md) | 54 · 8 | whole file · real | blind human | Software Heritage `.m` population, weighted | the `.m` rules; the cascade's `.m` candidates |
| [bench-linguist](../benchmarks/bench-linguist/README.md) | 3,404 · 768 | whole file · real | Linguist maintainers | curated (Linguist's samples) | Linguist family; Synid on 2,271 files |
| [bench-smola](../benchmarks/bench-smola/README.md) | 3,872 · 261 (ranked on the 1,107 gold) | whole file · real | a human (gold); Linguist's 2022 answer (silver) | one file per repository, chosen where Linguist named the language | — (the silver labels are Linguist's) |
| [bench-rosetta](../benchmarks/bench-rosetta/README.md) | 1,589 · 835 | snippet · derived from the label | the author | 2 per language, seeded | the two Rosetta-trained Hugging Face classifiers |
| [bench-hello](../benchmarks/bench-hello/README.md) | 1,009 · 965 | tiny program · extension only (`hello<ext>`) | contributors | all | — |
| [bench-pygments](../benchmarks/bench-pygments/README.md) | 637 · 428 | whole file · real | Pygments maintainers | curated | Pygments (a few files: Linguist family, Chroma) |
| [bench-hljs](../benchmarks/bench-hljs/README.md) | 191 · 185 | snippet · none | highlight.js maintainers | curated | highlight.js |
| [bench-rouge](../benchmarks/bench-rouge/README.md) | 455 · 229 | snippet · none | Rouge maintainers | curated | Rouge (1 file: Linguist family, Chroma) |
| [bench-rpgle](../benchmarks/bench-rpgle/README.md) | 760 · 4 | whole file · real | LLM judge + content rules (silver) | Software Heritage `.rpgle` population, weighted | the cascade's candidates |
| [bench-fsf](../benchmarks/bench-fsf/README.md) | 467 · 6 | whole file · real | LLM judge + content rule (silver) | Software Heritage `.fsf` population, weighted | the cascade; the study's rule |
| [bench-cobol](../benchmarks/bench-cobol/README.md) | 605 · 3 | whole file · real | LLM judge + content rules (silver) | Software Heritage `.cbl` population, weighted | the cascade; the study's rules |

Against the five properties the review checks (whole files, ambiguous extensions, human per-file labels,
population sampling, held out from the tools), none of the eleven has all five: bench-m comes closest (it
fails only on independence from the cascade, and on size); bench-smola's gold tier is human-labelled but
selected by Linguist; the population samples (rpgle, fsf, cobol) have LLM labels; the rest are curated.

Candidates not built yet, from the review (ids are the review's) and from local material:

| candidate | why | why not yet |
|---|---|---|
| **bench-heldout** ([spec](bench-heldout.md)) | the only one designed to have all five properties | needs a human review of 400–600 files (~5–6 h) |
| Stack Overflow snippets (C01/C02 SCC, SCC++) | the dominant snippet benchmark in papers; the only one an LLM was evaluated on | tag labels (noise never measured); dataset links untested; the July 2017 dump is in every LLM's training data |
| Project CodeNet (E08) | author-declared, judge-verified language; 55 languages | competitive-programming population (no config, data, generated or ambiguous files); 8 GB |
| PLangRec (A14) | the only extension labels with a measured error rate (parser check, 6.1 % rejected) | 113 GB corpus; GitHub only; 21 mainstream languages |
| The Stack v2 metadata (E03) | Software Heritage ids, paths, go-enry's language per file: a frame and a disagreement signal | go-enry labels are circular for the Linguist family; gated download — use it to *sample*, not to label |
| Del Bonifro et al. 2021 (A09) | Software Heritage, temporal second test set | the label is the extension, by design |
| PLDB `example` blocks (979 languages, local clone) | curated examples, long tail beyond Linguist | snippets; label = the concept; overlaps Rosetta/hello-world |
| Magika's `tests_data/` | Magika's home turf (like Pygments' example files) | a few files per content type |
| Telegram tglang 2023 (B14), AIcrowd (B13), OctoLingua (B04), Magika's test set (A13), Guesslang's (B05) | | not released |
| `Unknown` files of smola (171) | real files humans could not name: an open-set test | the scorer has no "abstaining is right" outcome yet |

## Identifiers

Run on every benchmark, each from a pinned Docker image (`tools/external/<tool>/`) or a pinned model: the
Linguist family (GitHub Linguist, go-enry, Hyperpolyglot, and re-implementations without a classifier),
highlighters (Pygments, Chroma, Rouge, highlight.js), line counters and taggers (cloc, tokei, scc, ohcount,
Universal Ctags), an editor (Neovim's filetype detection), magic numbers (libmagic), neural classifiers
(Magika, Guesslang, VS Code's language detection, Hugging Face models), lightweight LLMs (Jev, Kev-4B,
StarCoder2-3B), the candidates + Jev cascade, and Synid. Older releases of Linguist, go-enry, Pygments and
Magika are run too, to show regressions between a tool's versions.

## Leaderboard rules

- **Held-out mean.** An entry's rank is its mean accuracy over the benchmarks it ran on, *minus its home turf*.
  The raw mean and the pooled count are shown beside it.
- **Not applicable is not zero.** A tool that answers from the file name only is *n/a* on a benchmark without
  names (the review: "a content-only column is 'not applicable' for them, not zero").
- **Agreement between benchmarks.** Kendall's τ between the orders two benchmarks give to the same entries;
  and, per benchmark, the leaders and where its home-turf entries rank.
- **Coverage apart from skill.** `tools/coverage.py`: the languages each entry can name at all.

## What the portfolio shows

Figures from [LEADERBOARD.md](../LEADERBOARD.md), the benchmarks' leaderboards and READMEs, and
[TOOL-HISTORY.md](../TOOL-HISTORY.md) (2026-10-04).

**1. A benchmark crowns the tool that was tuned on it — for the task it was tuned for.** highlight.js 11.9.0
gets 187/191 (97.9 %) on its own auto-detection tests, which its test suite required it to pass until March
2024; the next tool, Magika, gets 33 %, and highlight.js' mean elsewhere is in single digits. Pygments is
first on its example files (93.7 %; 26 % held out); Linguist on its samples (99.5 %; 48 % held out). Rouge is
the exception that confirms the rule: 16th of 34 on its own samples, which its tests only *lex* — they
never ask it to guess. Home turf is a matter of what was tuned, not of who wrote the files. Within
bench-linguist, Synid is right on 76.6 % of all files but 56.1 % of those its classifier never saw.

**2. The benchmarks do not agree on the order of the tools, and the file name decides.** Kendall's τ between
benchmarks with file names (bench-m, linguist, smola, pygments, hello, rosetta, cobol) is 0.5–0.9; between
the three without names (hljs, rouge, fsf) 0.5–0.7; across the two groups −0.2 to +0.2. With names, the
Linguist family leads everywhere; without, a content classifier does (Magika: 92.5 % on fsf, 33 % on hljs,
27.5 % on rouge), and the Linguist family, Synid and the line counters fall to 0–6 %. A leaderboard over one kind of benchmark says
little about the other kind.

**3. Labels taken from a tool are a gift to that tool.** On bench-smola, Linguist 9.7.0 agrees with the silver
labels — Linguist's own 2022 answers — on 99.6 % of the files, and with the human on 87.4 % of the gold ones.
On the 167 files where the human corrected Linguist, Linguist 7.30.0 gives its 2022 answer again on 161, and
the content-only classifiers lead (Magika 44 %, Guesslang 33 %); Synid is right on 5 %.

**4. A name that carries the label inflates every name-based tool.** On bench-rosetta, whose file names come
from the language through acmeism's extension table, Linguist is right on 329 of the 353 files (of
languages it knows) with a real extension and on 1 of the 161 with an invented one. On bench-hello's 186
programs with a misleading extension (`Pebble.c`), no tool does better than 6.

**5. Samples of a real population contain failure classes that curated sets lack.** bench-cobol: synthetic
stubs and reading lists named `.cbl` — every name-based tool is wrong on all of them, which weighs
heavily once the sample is weighted back to the archive (56.5 % weighted for the best rule-based tools).
bench-fsf: a non-programming format — Synid answers ALGOL 68 on all 300 FEAT designs (3/467 right), Magika
92.5 %. bench-rpgle: every tool that reads the name is right (99.3 %); from the content alone, only Jev (an LLM)
recognises RPG.

**6. Tools regress between releases too.** highlight.js 11.9.0 → 11.12.0 is net −52 on its own test files (two
grammars, Dart and DNS Zone, now win on almost anything); Magika 0.5.1 → 1.0.3: +361 / −71 on
bench-linguist; Pygments 2.14 → 2.19 without names: +8 / −13 (a new Carbon lexer takes C files); Linguist's
switch to a centroid classifier (7.30.0 → 8.0.0) changed 37 answers on bench-linguist, +33 / −0.

**7. Coverage bounds everything.** Two thirds of bench-rosetta's cases are in languages Linguist does not know;
a tool's label set (6 to ~1,100 names) caps its score before its skill does — `COVERAGE.md` separates the two.

**8. Specific benchmarks find specific bugs.** In Synid: `Text` as the default answer (most of its misses
on every benchmark), the ALGOL 68 answer on `.fsf`, rule names that do not match candidate names
(`PLpgSQL`; 12 regressions on bench-smola), and one nondeterministic answer (HTML or ERB on hljs'
`xml/default.txt` across runs). In other tools: linguist-js' conversion of possessive regexes (its Adblock
heuristic can never match), Chroma's GDScript analyser that scores 0.2 on almost any text, ohcount's crashes.

## What it implies for the benchmark we need

The portfolio is a map of biases, each measured. A benchmark that is to rank identifiers on the files they
will actually meet — Software Heritage's — must control each one, and [bench-heldout](bench-heldout.md)'s
properties follow from the findings above:

| finding | what bench-heldout must do | spec |
|---|---|---|
| 1. home turf, 20–60 points | files no tool, mapping or rule set was built from, by construction and checked by blob id; rules and mappings frozen before labels are seen | P1 |
| 2. the name decides the order | stratify by kind of name (ambiguous / single claimant / unclaimed / none); score every entry with the name, without it, and with a misleading one | P2, P6 |
| 3. tool-derived labels inflate the tool | labels from a blind human review, never from a tool or an LLM; double coding of a sample, with agreement | P3 |
| 4. label-derived names leak | real archived names only | P4 |
| 5. failure classes only a population has | a probability sample of the archive, with weights; not-code and generated files kept | P2 |
| 6. tools regress | frozen, versioned cases; every tool pinned and rerun on new releases (`tools/run_all.py`) | P5 |
| 7. coverage bounds skill | taxonomy fixed up front (PL-ultimate-llm concepts with Linguist names and accept lists); report coverage apart | P3, P6 |

The existing benchmarks keep their use: as non-regression suites (each tool's release history), as
diagnostics (each one isolates a regime — content only, misleading names, a hard extension, the long tail),
and as the evidence for the design above. What none of them can give is the number Software Heritage needs:
how often an identifier is right on a file drawn from the archive.

## Next

1. **bench-heldout** — build it per its spec: ~500 files sampled from the Software Heritage export
   (`../PL-swh-contents`), strata by kind of name, blind review on PL-ultimate-llm's review page (~6 h).
2. **Human audit of the silver benchmarks** — a random 10 % of bench-rpgle, fsf and cobol through the same
   review page, to measure the LLM judge (the review recommends it before LLM labels are trusted).
3. **Jev and the cascade on the new benchmarks** (paid, small: see the README) — the strongest entries on
   bench-m and bench-linguist are not yet run on the nine others.
4. **Misleading-name runs** (OctoLingua's design): every file under another file's extension.
5. **An open-set outcome** in `tools/score.py` (abstaining is right on files in no known language), to score
   smola's 171 `Unknown` files and rosetta's languages no tool knows.
6. **Snippets from Stack Overflow** (SCC) and **Project CodeNet**, if a snippet-level or a
   judge-verified benchmark is wanted; both are listed above with their limits.
