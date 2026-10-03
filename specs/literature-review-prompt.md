# Literature review prompt — benchmarks for programming-language identification

*Written 2026-10-03, to prepare [`bench-heldout`](bench-heldout.md): before building a new held-out
benchmark, map what academia and industry already use to evaluate programming-language identification.*

**How to use.** Paste the prompt below, as one message, into a deep-research tool (e.g. OpenAI Deep
Research). Run it in two passes: first as written, for the broad map; then follow up with *"deep-dive the
5 most relevant benchmarks: label procedure, leakage, and exact numbers"*. The seed works are named from
memory — the prompt asks the tool to verify their exact titles and venues; check them too. The extraction
table uses the dimensions of `bench-heldout.md` (independence, sampling, labels, taxonomy, name vs
content), so its rows can be compared with the spec directly. Store the results next to this file
(e.g. `literature-review-<date>.md` and `.csv`).

---

````markdown
# Research task: benchmarks and datasets for programming-language identification (PLI)

## Context (why I am asking)
I maintain *synid-bench*, a collection of benchmarks for programming-language identification of source
files: given a file (its bytes, and possibly its name), which programming language (or "not code") is it
written in? It assesses Synid, a syntax-identification tool developed in the CodeCommons project and run
over the Software Heritage archive, against other identifiers (GitHub Linguist, go-enry, Hyperpolyglot,
Pygments, cloc, Guesslang, Magika, small LLMs).

Our own experiments surfaced methodological problems I want to compare with the literature:
- **Training leakage.** GitHub Linguist's `samples/`, a common evaluation set, is the training data of
  Linguist and of tools derived from it. Their scores on it are near-perfect, then drop on newer files.
- **Label-set and taxonomy effects.** A tool cannot name a language outside its label set. Scores
  depend on naming and granularity (Octave vs MATLAB, INI vs systemd unit, JSX vs JavaScript), and on
  whether "not code" is a label.
- **Ambiguous file extensions** (`.m`, `.h`, `.pl`, `.v`, `.inc`…). This is where identifiers differ, and
  extension-based labels are least reliable.
- **File name vs content only.** Most rule-based tools collapse without the file name.
- **Representativeness.** Curated samples vs files drawn from a real population (e.g. an archive), with
  or without population weights.

I want to know what academic and industrial work already exists, so that a new held-out benchmark
builds on it rather than re-inventing it.

## Questions to answer
1. Which benchmarks or datasets have been used to evaluate programming-language identification, at the
   level of whole files, snippets (e.g. Stack Overflow), or fragments? Include sets built for one paper
   and never named.
2. For each: how were the labels obtained (file extension, repository language, human annotation,
   compiler or parser acceptance, LLM)? How reliable are they, and is that reliability measured?
3. Which tools or models were evaluated on them, with which results? Did the evaluation control for
   training/test overlap, label-set coverage, or name vs content?
4. Which works study ambiguous extensions, polyglot or embedded files, rare or legacy languages (COBOL,
   MUMPS, RPG, Fortran dialects…), or "not code" content?
5. Which works use large archives (Software Heritage, GitHub, The Stack, World of Code, Boa…) for
   language identification or for measuring language distributions, and how do they label languages?
6. Is there a survey or systematic mapping of PLI, or of the neighbouring file-type identification work
   (digital forensics: file fragments, magic numbers, content-type detection)? What evaluation lessons
   transfer?
7. Have LLMs (general or code models) been evaluated for PLI, and how was contamination handled?
8. Which methodological recommendations exist (held-out splits, deduplication, near-duplicate removal,
   temporal splits, inter-annotator agreement, stratified sampling, population weighting)?

## Scope
- Period: 2005 to today; weight 2015 onward, but include older seminal work.
- Sources: peer-reviewed venues (ICSE, FSE, ASE, MSR, SANER, ICSME, SCAM, EMSE, JSS, TSE, TOSEM, ESEM,
  ACL/EMNLP if relevant, DFRWS / Digital Investigation / Forensic Science International for file-type
  work), arXiv, theses, and technical reports. Also grey literature where it carries an evaluation: tool
  documentation, GitHub issues of Linguist, go-enry, Guesslang or Magika reporting accuracy, and
  industrial blog posts. Label grey literature as such.
- Out of scope: natural-language identification, and code *generation* benchmarks. Exception: a
  generation dataset whose language labels are reused as identification ground truth (e.g. The Stack's
  per-file language).

## Search strategy (follow it, and report what you did)
- Keywords, combined: "programming language identification", "source code language detection",
  "language identification source code", "code snippet classification programming language",
  "file type identification", "content type detection", "Linguist accuracy", "GitHub language detection",
  "Stack Overflow snippet language prediction", "polyglot files", "file extension ambiguity",
  "software language identification", "language classification of source files", "LLM programming
  language detection".
- Snowball from seed works, backward (references) and forward (citations): Kennedy van Dam & Zaytsev,
  "Software Language Identification with Natural Language Classifiers" (SANER 2016); Alrashedy et al.,
  "SCC: Automatic Classification of Code Snippets" (SCAM 2018) and its Stack Overflow follow-up;
  Fratantonio et al., "Magika: AI-Powered Content-Type Detection" (arXiv 2409.13768); the papers
  describing The Stack and The Stack v2 (how they assign languages); and the Guesslang project.
  Verify each seed's exact title and venue rather than trusting mine.
- Check Google Scholar, Semantic Scholar, the ACM DL, IEEE Xplore, DBLP and arXiv. For each tool
  (Linguist, enry, Guesslang, Magika, Pygments, cloc, ohcount, tokei, scc), look for papers that
  evaluate it.

## What to extract — one row per benchmark or dataset
| field | content |
|---|---|
| name / short id | as in the source; invent a descriptive id if unnamed, and say so |
| reference | full citation with DOI or arXiv id, and the URL of the dataset |
| year | |
| granularity | file / snippet / fragment / repository |
| size | number of items and of languages (label-set size) |
| file source | e.g. GitHub, Stack Overflow, Rosetta Code, Software Heritage, Linguist samples, synthetic |
| file names available? | yes / no; evaluated with and without? |
| label source and quality | extension, repo metadata, human (how many annotators, agreement), compiler, LLM |
| "not code" / "other" labels? | |
| taxonomy | which naming (Linguist, Pygments, own); handling of dialects and families |
| splits and leakage control | train/test, dedup, temporal split, overlap with known training sets |
| sampling | curated / random / stratified; population weights? |
| tools evaluated and headline results | accuracy, F1, per-language results if reported |
| availability and licence | downloadable? still online? licence of the files |
| known issues | as reported by the authors or by later work |
| relevance to us | high / medium / low, with one sentence why |

## Deliverables
1. **Table:** the extraction table above, as Markdown and as CSV. Aim for exhaustiveness; I prefer 40
   rows with some low-relevance ones over 10 rows.
2. **Synthesis, about 2 pages:** what the field measures and how; recurring pitfalls (leakage, label
   noise, label-set mismatch, extension-derived labels); what is missing. In particular: is there any
   held-out, human-labelled, population-sampled benchmark of whole files with ambiguous extensions?
3. **Recommendations for a new held-out benchmark:** independence from training sets, sampling,
   labelling, taxonomy, metrics. Cite which work each recommendation comes from.
4. **Tools list:** every identifier that appears, with its approach (rules / Bayesian / neural / LLM),
   its label-set size if stated, and its training data if stated.
5. **Search log:** queries and databases used, number of hits screened, inclusion/exclusion decisions
   for borderline items.

## Rules
- Never invent a paper, author, venue, DOI, dataset or number. If you cannot verify a claim from the
  source itself, say "unverified" and give where you saw it.
- Prefer primary sources. When a number comes from a secondary source, say so.
- Distinguish what a paper *reports* from your *interpretation*.
- When two works use the same dataset under different names, merge them and note the aliases.
- Give direct links for everything, and flag dead links.
````
