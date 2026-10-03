# Spec — `bench-heldout`: a benchmark none of the identifiers was built from

*Status: specification, not built. Written 2026-10-03 to be picked up later. Before building it, map
the existing benchmarks: [literature review prompt](literature-review-prompt.md).*

## Why

The two benchmarks so far favour some identifiers by construction:

- **bench-linguist** is GitHub Linguist's own sample set. Linguist, go-enry, Hyperpolyglot and Synid's
  classifier were trained on most of it, and its labels are Linguist's — so is part of the candidate
  mapping the cascade (`tools/jev_cascade.py`) relies on.
- **bench-m** comes from the `.m` extension study, whose observations (Magma, MUMPS and C under `.m`)
  entered PL-ultimate-llm's mapping: the cascade's 54/54 is partly a reflection of that.

`bench-heldout` should measure what each identifier does on files that **neither the tools, nor the
mapping, nor the rules were derived from** — the honest test of the cascade, and of any future Synid.

## Properties

Each property is checkable; *must* properties are checked by the build script, which refuses to emit
`cases.csv` when one fails.

### P1 — Independence (no leakage)

- **Must:** no file whose `sha1_git` is in any known training or tuning set: Linguist's `samples/` (all
  revisions), Hyperpolyglot's `samples/`, Pygments' test files, Magika's `tests_data/`, the files sampled,
  reviewed or judged by the PL-ultimate-llm extension studies (`.m`, `.cbl`, `.rpgle`, `.fsf`), the files
  of bench-m and bench-linguist.
- **Must:** no file from an origin in an exclusion list: `github-linguist/linguist` and its forks,
  `monkslc/hyperpolyglot`, `pygments/pygments`, `google/magika`, `yoeo/guesslang`, PL-ultimate-llm itself.
- **Must:** the candidate mapping and every rule set evaluated on it are frozen *before* the labels are
  revealed to whoever maintains them — PL-ultimate-llm's `ext_evidence` must not be fed from this
  benchmark's labels. A *dev* split (~20 %, public) may be used for tuning; scores are reported on the
  *test* split, and an entry tuned on the dev split says so in its metadata.
- **Should:** LLM training data cannot be excluded for public code; record each file's first archival date
  in Software Heritage and report results split at a cutoff (e.g. first seen after 2026-06-01), so that a
  gap between old and new files shows memorisation.

### P2 — Population and sampling

- **Must:** a defined frame — Software Heritage contents reachable under a file name (directory entries),
  at a recorded graph export — and a recorded random seed.
- **Must:** stratification by the kind of name, because that is where identifiers differ:
  1. *ambiguous extensions* (two or more languages claim it in PL-ultimate-llm),
  2. *single-claimant extensions*,
  3. *extensions no source claims*,
  4. *no extension* (whole-name files such as `Dockerfile`, and extension-less scripts).
  Within each stratum, extensions are drawn by frequency, then files at random.
- **Must:** inclusion probabilities recorded per file, so that accuracy can be weighted back to the
  population (as bench-m does), next to the unweighted figure.
- **Must:** diversity caps — at most 2 files per origin, at most ~5 % of the cases per expected language.
- **Should:** oversample rare languages (a stratum of languages under N files in the archive) so that
  coverage, not only the head of the distribution, is measured.
- **Size:** 400–600 files — large enough for ±4-point intervals overall and per stratum, small enough for
  a full human review.

### P3 — Labels

- **Must:** a blind human review of every file (the online review tool of PL-ultimate-llm, which shows
  the bytes and the file name, never a tool's answer); a second reviewer on a random 20 % to report
  agreement (Cohen's κ); disagreements adjudicated and recorded.
- **Should:** LLM judges only to triage (order the queue, flag likely non-code), never as labels; their
  agreement with the humans is reported, as in bench-m.
- **Must:** a taxonomy fixed up front: labels are PL-ultimate-llm concepts, each with its Linguist name
  when it has one and an `accept` list (aliases, and the members of a family the label stands for, e.g.
  MATLAB/Octave). Explicit labels for *not code* (text, data, binary), *other language* and *unsure*.
- **Must:** a written granularity policy — when is a dialect a different answer (Systemd vs INI, JSX vs
  JavaScript, ZSH vs Shell)? One rule, applied to every tool, stated in the README.
- **Should:** *unsure* files go to a silver tier, excluded from the headline figure.

### P4 — Provenance and licensing

- **Must:** every case has a qualified SWHID (content, origin, path) resolvable in the archive.
- **Must:** files are fetched from Software Heritage at build time and checked against their `sha1_git`;
  they are stored in the repository only when their licence allows it.
- **Must:** the build is reproducible from pinned inputs (graph export, seed, exclusion sets, mapping
  snapshot).

### P5 — Versioning

- **Must:** `bench-heldout/<n>` in `cases.csv`'s first line; any change to cases, labels or accept lists
  makes a new version, with a changelog; entries record the version they were run on.
- **Must:** an entry built or tuned with access to a version's labels says so (`tuned_on`), and the
  leaderboard marks it.

### P6 — What it must be able to show

- the candidate recall of PL-ultimate-llm's mapping (is the expected language among the extension's
  candidates?) on files it was not built from, per stratum;
- the cascade against Synid, Linguist, go-enry and the others on equal footing — no † anywhere;
- the label-set effect (Jev with the study's 63 labels, Linguist's 804, the encyclopedia's candidates);
- with vs without the file name, per stratum.

## Building it (later)

1. **Exclusion sets** — collect the `sha1_git` of every set in P1 (Linguist samples over all revisions:
   `git log --all` of the repository; the studies' sample tables in PL-ultimate-llm).
2. **Frame and draw** — from a Software Heritage graph export (the CodeCommons infrastructure Synid runs
   on), list file names with their extension, assign strata from PL-ultimate-llm's `ext_claim`, draw per
   P2, fetch contents, drop excluded or empty files, record first-seen dates.
3. **Review** — publish the review page; LLM triage orders the queue; 1 human on all, 2 on 20 %;
   adjudicate.
4. **Freeze** — `cases.csv`, the dev/test split, the README (taxonomy, granularity policy, strata and
   weights), checks of P1–P5 in `build_cases.py`.
5. **Run** every entry of the collection (`reproduce.sh`).

**Cost.** Review is the bulk: ~30 s per file → 4–5 hours for 500 files, plus ~1 hour for the double
review and adjudication; LLM triage < $5; tool runs as for bench-linguist (Jev ≈ $0.1, the cascade ≈ $0.1).

## Open questions

- Should a misnamed file (C code in a `.m`) count against an identifier that trusts the extension? bench-m
  says yes (`c-or-cpp`); keep it, and report the stratum.
- Generated and minified files: include as they come (they are part of the population), tag them.
- Whether the dev/test split of the labels can stay public: a public test split invites tuning; a
  private one needs a maintainer to run entries. A public split with `tuned_on` discipline is the
  simplest start.
