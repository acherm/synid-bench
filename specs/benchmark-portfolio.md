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
| labels | human / author-declared / maintainers / LLM judge / tool | a label produced by a tool under test is circular; an LLM judge favours LLM entries | blind human, double-coded sample |
| sampling | curated / all / random per language / population-sampled with weights | curated sets over-represent what their curators test; only a population sample gives an error rate for the archive | stratified by kind of name, weighted |
| home turf | entries built, trained or tuned on the files | the score is then partly recall of training data | excluded by construction |
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

Twenty-four other identifiers, each from a pinned Docker image (`tools/external/<tool>/`: Dockerfile, `tool.json`,
identify script, `names.csv` mapping its labels to Linguist's names, synonyms only), language models and Synid:

| family | tools | reads |
|---|---|---|
| Linguist and its ports | GitHub Linguist 9.7.0, go-enry 2.9.6, Hyperpolyglot; linguist-js, gengo (Linguist's rules, no classifier) | name, then content |
| highlighters | Pygments, Chroma, Rouge (name, then content); highlight.js (content) | |
| line counters, taggers | cloc, tokei, scc (name only); ohcount, Universal Ctags (name, shebang, modelines) | name |
| editor | Neovim's filetype detection | name, then content |
| magic numbers | libmagic (`file`) | content |
| neural classifiers | Magika, Guesslang, VS Code's language detection, three Hugging Face models (CodeBERTa-language-id, philomath-1209, FrameByFrame), PLangRec | content |
| snippet detector | flourite | content |
| language models | Jev 1.13 (OpenRouter), Kev-4B (llama.cpp), StarCoder2-3B (Ollama); the candidates + Jev cascade | content (± name) |
| Synid | 48c3c45, 9bc1c32, and 48c3c45 with one strategy off or without the name | name, then content |

Older releases are run for non-regression ([TOOL-HISTORY.md](../TOOL-HISTORY.md)): Linguist 7.30.0 (naive
Bayes) and 8.0.0 (centroid), go-enry 2.8.9, Pygments 2.14.0 and 2.19.2, Magika 0.5.1, highlight.js 11.9.0.
Jev runs on every benchmark in two forms: over Linguist's 836 languages at 76f88c6 (with and without the
file name), and as the candidates + Jev cascade ($35 in all for the nine new benchmarks plus the 836-language
rerun on bench-m and bench-linguist). Not run everywhere, for cost: Kev-4B (~21 s per file), StarCoder2-3B
(~2.5 s per file; bench-hljs only among the new benchmarks), PLangRec on bench-smola (~600,000 distinct lines),
and Jev with the 804-language snapshot or the extension studies' 63 labels (kept where they were run) — each
benchmark's leaderboard says which entries are missing and why.

## Leaderboard rules

- **Held-out mean.** An entry's rank is its mean accuracy over the benchmarks it ran on, *minus its home turf*.
  The raw mean and the pooled count are shown beside it.
- **Not applicable is not zero.** A tool that answers from the file name only is *n/a* on a benchmark without
  names (the review: "a content-only column is 'not applicable' for them, not zero").
- **Agreement between benchmarks.** Kendall's τ between the orders two benchmarks give to the same entries;
  and, per benchmark, the leaders and where its home-turf entries rank.
- **Coverage apart from skill.** `tools/coverage.py`: the languages each entry can name at all.

## What the portfolio shows

The findings, numbered 0–8 as referred to below, are in [FINDINGS.md](../FINDINGS.md).

## What it implies for the benchmark we need

The portfolio is a map of biases, each measured. A benchmark that is to rank identifiers on the files they
will actually meet — Software Heritage's — must control each one, and [bench-heldout](bench-heldout.md)'s
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

## Next

1. **bench-heldout** — build it per its spec: ~500 files sampled from the Software Heritage export
   (`../PL-swh-contents`), strata by kind of name, blind review on PL-ultimate-llm's review page (~6 h).
2. **Human audit of the silver benchmarks** — a random 10 % of bench-rpgle, fsf and cobol through the same
   review page, to measure the LLM judge (the review recommends it before LLM labels are trusted).
3. **Misleading-name runs** (OctoLingua's design): every file under another file's extension.
4. **An open-set outcome** in `tools/score.py` (abstaining is right on files in no known language), to score
   smola's 171 `Unknown` files and rosetta's languages no tool knows.
5. **Snippets from Stack Overflow** (SCC) and **Project CodeNet**, if a snippet-level or a
   judge-verified benchmark is wanted; both are listed above with their limits.
6. **For Synid**, from findings 0 and 8: without the Pygments step it is the best identifier that does not
   call an LLM (50.8 % held out, against 45.8 %) — return the candidates rather than `Text` when no rule
   decides; fix the `comment` strategy's ALGOL 68 answer on `.fsf`, the rule names that do not match
   candidate names, and the nondeterministic answer on `xml/default.txt`.
