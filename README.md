# synid-bench — benchmarks for Synid, a syntax-identification tool

A collection of benchmarks to assess **Synid**, a tool that identifies the
programming language (syntax) of source files, developed in the CodeCommons
project — here on real files archived by
[Software Heritage](https://www.softwareheritage.org), version after version:
*is this Synid version better or worse than the last one, on which files, and
on which known failure triggers?*

Each benchmark is a frozen set of real archived files, with the language each
file is written in and the provenance of that label. The repository holds the
benchmarks, their documentation and the tools to run them — not Synid itself
(its repository, `teams/codecommons/swh-syntax-identification` on the
CodeCommons team's GitLab space, is access-restricted).

## Leaderboard

**[LEADERBOARD.md](LEADERBOARD.md)** runs every identifier on every benchmark: Synid versions and
configurations (a strategy turned off, or without the file name); the other identifiers, each from a pinned
Docker image (`tools/external/`) — the Linguist family (GitHub Linguist, go-enry, Hyperpolyglot,
linguist-js, gengo), highlighters (Pygments, Chroma, Rouge, highlight.js), line counters and taggers (cloc,
tokei, scc, ohcount, Universal Ctags), an editor (Neovim's filetype detection), magic numbers (libmagic),
neural classifiers (Magika, Guesslang, VS Code's language detection, three Hugging Face models, PLangRec),
a snippet detector (flourite); lightweight models — Jev (OpenRouter), Kev-4B (local, llama.cpp), StarCoder2-3B
(local, Ollama); a two-stage identifier (PL-ultimate-llm's candidates for the extension, then Jev); and rules
written for one benchmark only. Older releases of Linguist, go-enry, Pygments, Magika and highlight.js are
run too: [TOOL-HISTORY.md](TOOL-HISTORY.md) shows what each release fixed and broke.

The benchmarks measure different things, and some are the training or development data of some entries —
their **home turf** (†). Each benchmark has a card (`card.json`: unit, file names, who labelled, sampling,
strengths, weaknesses), shown on the leaderboards. Entries are ranked by their **held-out mean**: the mean
accuracy over the benchmarks they ran on, leaving out their home turf. A tool that answers from the file name
only is *n/a* where a benchmark has no names. The leaderboard also says how far the benchmarks agree on the
order of the entries. Each benchmark has its own leaderboard (accuracy with intervals, precision of language
answers, tags), a coverage report (which of its languages each entry can name at all) and the entries not run
on it, with the reason. LLM judges whose agreement backs a benchmark's ground truth are shown apart, not
ranked. Why a portfolio, and what it shows: [specs/benchmark-portfolio.md](specs/benchmark-portfolio.md).

## Benchmarks

| benchmark | what | cases | unit · names | ground truth | home turf (†) |
|---|---|---:|---|---|---|
| [`bench-m`](benchmarks/bench-m/README.md) | `.m` files from Software Heritage: Objective-C, MATLAB/Octave, Wolfram, Mercury, MUMPS, Magma… ([failures](benchmarks/bench-m/FAILURES.md) · [assessment of Synid](benchmarks/bench-m/assessment/m-9bc1c32.md)) | 54 | whole file · real | blind human review; two LLM judges agree on all | the `.m` rules; the cascade's `.m` candidates |
| [`bench-linguist`](benchmarks/bench-linguist/README.md) | GitHub Linguist's sample files, 768 languages; tagged seen / unseen by Synid's classifier | 3,404 | whole file · real | Linguist's maintainers (the sample's directory) | Linguist, go-enry, Hyperpolyglot, Synid |
| [`bench-smola`](benchmarks/bench-smola/README.md) | one file per GitHub repository, 261 languages (smola/language-dataset); ranked on the 1,107 human-checked files, 167 of which correct Linguist | 3,872 | whole file · real | a human (gold); Linguist's own answer (silver) | — |
| [`bench-rosetta`](benchmarks/bench-rosetta/README.md) | Rosetta Code solutions, 848 languages, two thirds unknown to Linguist | 1,589 | snippet · derived from the label | the author (the solution's language heading) | Hugging Face classifiers trained on Rosetta Code |
| [`bench-hello`](benchmarks/bench-hello/README.md) | hello-world programs, ~1,000 languages, renamed `hello<ext>`; 186 with a misleading extension | 1,009 | tiny program · extension only | the contributors | — |
| [`bench-pygments`](benchmarks/bench-pygments/README.md) | Pygments' example files, 431 lexers | 637 | whole file · real | Pygments' maintainers | Pygments |
| [`bench-hljs`](benchmarks/bench-hljs/README.md) | highlight.js' auto-detection test files | 191 | snippet · none | highlight.js' maintainers | highlight.js |
| [`bench-rouge`](benchmarks/bench-rouge/README.md) | Rouge's visual samples and demos | 455 | snippet · none | Rouge's maintainers | Rouge |
| [`bench-rpgle`](benchmarks/bench-rpgle/README.md) | `.rpgle` files sampled from Software Heritage (PL-ultimate-llm's study) | 760 | whole file · real | LLM judge + content rules (silver), population weights | the cascade's candidates |
| [`bench-fsf`](benchmarks/bench-fsf/README.md) | `.fsf` files sampled from Software Heritage: FSL designs (Tcl), git-annex pointers, XML | 467 | whole file · real | LLM judge + content rule (silver), population weights | the cascade; the study's rule |
| [`bench-cobol`](benchmarks/bench-cobol/README.md) | `.cbl`/`.CBL` files sampled from Software Heritage: programs, copybooks, synthetic stubs | 605 | whole file · real | LLM judge + content rules (silver), population weights | the cascade; the study's rules |
| `bench-heldout` *(planned)* | files none of the identifiers, nor PL-ultimate-llm's mapping, was built from | 400–600 | whole file · real | blind human review | none, by construction ([spec](specs/bench-heldout.md)) |

What makes a good one here: **ground truth you can trust** (checked labels, with
their provenance), **diversity** (languages, repositories, failure triggers),
and **small enough** to run in seconds and to read every failure. Cases are
frozen within a version (`bench-m/1`) so that results stay comparable; a
benchmark grows by releasing a new version.

## Use

```bash
# build Synid (any version) — needs access to its repository
(cd path/to/swh-syntax-identification && cargo build --release --bin synid)

# run a benchmark, score it against its latest baseline
python3 tools/run.py benchmarks/bench-m --synid path/to/swh-syntax-identification/target/release/synid --label mytest
python3 tools/score.py benchmarks/bench-m/results/mytest.jsonl \
    --baseline benchmarks/bench-m/baselines/48c3c45-default.jsonl --report benchmarks/bench-m/results/mytest.md
```

Python 3.10+, no dependencies; runs locally.

| tool | what |
|---|---|
| `tools/run.py <bench> --synid … --label …` | runs a Synid binary over a benchmark → `<bench>/results/<label>.jsonl`. The configuration is generated by the binary itself (`synid info generate-config`), so it follows Synid's options across versions; the networked `linguist-api` strategy is off (benchmarks measure what Synid infers from a file's name and bytes); `--disable <strategy>` runs an ablation |
| `tools/score.py <run> [--baseline <run>] [--report <md>]` | accuracy overall, per expected language and per failure trigger; with a baseline, the cases fixed / regressed / changed; exit 1 when a case the baseline got right regresses |
| `tools/history.py <bench>` | every stored baseline side by side → `<bench>/HISTORY.md` |
| `tools/leaderboard.py` | every run of every benchmark (`baselines/` and `entries/`), ranked → `LEADERBOARD.md` and `<bench>/LEADERBOARD.md` |
| `tools/jev_linguist.py <bench>` | asks Jev (a lightweight decision model, OpenRouter) the language of each case among all of GitHub Linguist's languages → a leaderboard entry (needs an OpenRouter key; ~$0.06 for bench-m) |
| `tools/external.py <bench> --tool T` | runs another identifier in its pinned Docker image → a leaderboard entry (`--list`: the tools; `--content-only`: without the file name; `--labels`: the tool's label set). A tool is a directory `tools/external/<tool>/`: Dockerfile, `tool.json` (version, name, flags), identify script, `names.csv` (its labels → Linguist's names, synonyms only); an entry records the image's sources and the mapping it was made with |
| `tools/run_all.py [--synid …]` | every tool on every benchmark — the whole matrix, or what is missing or out of date (a new release, a changed script or mapping); `--skip 'hf-*'`, `--jobs N`, `--dry-run`. Non-regression for any tool, not only Synid |
| `tools/tool_history.py [--tool linguist …]` | each tool's releases side by side, per benchmark, with the cases fixed and regressed → `TOOL-HISTORY.md` |
| `tools/ollama_llm.py <bench> --model M` | asks a local language model (Ollama; e.g. StarCoder2-3B) the language from the first 2,000 characters → an entry |
| `tools/jev_cascade.py <bench>` | candidates + Jev: the languages PL-ultimate-llm associates with the file's extension (or name), among which Jev chooses; a broad fallback when none fits |
| `tools/export_pl_candidates.py` | snapshots PL-ultimate-llm's extension → language mapping into `tools/data/pl_candidates.json` |
| `tools/coverage.py <bench>` | which of the benchmark's languages each entry can name, and its accuracy on those → `COVERAGE.md` |
| `tools/failures.py <bench>` | every case the latest Synid gets wrong, with the program, the answers of every configuration, and the root cause (from the benchmark's `root_causes.py`) → `<bench>/FAILURES.md` |

A new Synid version that is accepted gets its run copied into
`<bench>/baselines/`, and `history.py` updates the record. Any other entry — a
Synid configuration (`run.py --disable …`), another identifier, a new tool —
goes into `<bench>/entries/` in the same format (first line `{"meta": {"label",
"name", "kind", "note", …}}`, then one `{"case_id", "answer"}` per case);
`leaderboard.py` ranks them all. The GitHub Actions
workflow in `.github/workflows/` (optional) does the run weekly when given a
GitLab token with `read_repository` as the secret `SYNID_GITLAB_TOKEN`.

## Format of a benchmark

```
benchmarks/<name>/
  README.md        what it covers, how it was built, its limits
  cases.csv        first line: "# <name>/<version> — …"; one row per file
  files/<sha1_git> the files' bytes
  baselines/       runs of known Synid versions (JSON lines: {"meta": …}, then {"case_id", "answer"})
  entries/         other leaderboard entries, same format
  card.json        the benchmark card; contamination.json: home-turf entries (†)
  HISTORY.md       generated by tools/history.py
  LEADERBOARD.md   generated by tools/leaderboard.py
  root_causes.py   (optional) known root causes of failures, and how to recognise them
  FAILURES.md      generated by tools/failures.py
  (build script, assessment, … as needed)
```

`cases.csv` columns — required: `case_id`, `sha1_git`, `filename` (Synid looks
at names), `ext`, `expected` (language), `accept` (the Synid answers that count
as right, `;`-separated); recommended: `qualified_swhid` (origin and path),
`expected_detail`, `reference` (who labelled it), `provenance`, `tier`,
`weight` (to re-weight a stratified draw), `tags` (failure triggers,
`;`-separated). A case is right when Synid gives exactly one syntax and it is
in `accept` (a name there also accepts its Linguist aliases); several syntaxes =
undecided.

Beside `cases.csv`: `card.json`, the benchmark card (unit, file names — real,
derived from the label, or none —, who labelled, sampling, strengths,
weaknesses; `headline_tier` when the leaderboard ranks on one tier, e.g. the
human-checked files); `contamination.json`, the entries built, trained or tuned
on these files (their home turf, †); `labels.csv`, the crosswalk from the
source's labels to Linguist's names; `build_cases.py`, which rebuilds the cases
from pinned sources; `reproduce.sh`, every run.

The files are copies of publicly archived source files, kept for
reproducibility; each keeps the licence of its origin repository (see its
qualified SWHID). They can also be fetched from Software Heritage:
`https://archive.softwareheritage.org/api/1/content/sha1_git:<sha1_git>/raw/`.
