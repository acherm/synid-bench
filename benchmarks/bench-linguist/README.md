# bench-linguist — GitHub Linguist's sample files

A broad benchmark: the **3,404 sample files of [GitHub Linguist](https://github.com/github-linguist/linguist/tree/main/samples)**
in **768 languages**, each labelled by the directory Linguist's maintainers filed it under. Where
[bench-m](../bench-m/README.md) is small, blind-reviewed and deep on one ambiguous extension, this one
is wide: it measures how far Synid's coverage goes, and catches regressions on languages bench-m never
sees.

| | |
|---|---|
| cases | 3,404 files (`samples/<language>/…`, symbolic links left out), 768 languages |
| labels | the sample's directory = its Linguist language; a case is right when the answer is that language or one of its Linguist aliases |
| source | Linguist at [`76f88c6`](https://github.com/github-linguist/linguist/tree/76f88c6d3c22f8560d22d29854f24d9607f9edde/samples) (2026-09-25), the revision Software Heritage archived that day — every case has a SWHID with that origin |
| files | **not stored here** (each sample keeps its own licence): `build_cases.py` fetches them at the pinned revision and checks each against its git blob id |

```bash
python3 benchmarks/bench-linguist/build_cases.py          # fetch the files (and rebuild cases.csv, identical)
python3 tools/run.py benchmarks/bench-linguist --synid path/to/synid --label mytest
python3 tools/score.py benchmarks/bench-linguist/results/mytest.jsonl \
    --baseline benchmarks/bench-linguist/baselines/48c3c45-default.jsonl
```

## Read it with care: training data, unknown languages, taxonomy

**Most of these files are training data.** Synid's Bayesian classifier (`hyplyclassifier`) comes from
[Hyperpolyglot](https://github.com/monkslc/hyperpolyglot), trained on a 2023 copy of these very samples;
**2,271 of the 3,404 files are byte-identical to a training file** (tag `seen-in-training`), 1,133 are not
(`unseen`). Linguist trains its own classifier on them too. A score over the whole set therefore
overstates what either tool does on new files — read the `unseen` column.

**Some languages are unknown to Synid.** 39 languages (112 files, nearly all `unseen`: languages added
to Linguist after 2023) are not among the syntaxes Synid can output under an accepted name: no strategy
can name them. [COVERAGE.md](COVERAGE.md) gives, for every entry, the languages it can name and its
accuracy on those — a tool with a small label set (Magika, cloc) is mostly limited by it.

**Labels follow Linguist's taxonomy.** Synid sometimes names a dialect or a neighbouring format where
Linguist files the sample under a broader language — `Systemd` for an `INI` unit file, `MSBuild` for
`XML`, `ASP` for `ASP.NET`, `CBM BASIC V2` for `BASIC`. These count as wrong here; they are
disagreements of granularity as much as errors.

Tags: `seen-in-training` / `unseen`; `ambiguous-ext` — the extension is claimed by two or more Linguist
languages (1,200 files: the cases where content must decide); `by-filename` — a sample identified by its
whole file name (`samples/<language>/filenames/`, 321 files).

## Findings — Synid 48c3c45

- **76.6 %** right overall (2,606 / 3,404); when it names a language, it is right 92.2 % of the time.
- **Seen vs unseen: 86.7 % vs 62.2 %** (unseen files in languages Synid can name; precision 98.7 % vs
  83.2 %). The gap is the effect of training on the test files.
- **Ambiguous extensions on new files are the weak spot: 17.6 %** (56 / 318 unseen files in languages
  Synid can name); 209 of them end as `Text`.
- **Without its name, a file is almost never identified: 5.4 %** (`--content-only`, the file run as
  `file`). Synid's content strategies narrow the candidates an extension gives; on their own they
  rarely conclude.
- **The Pygments step trades recall for precision.** With `pygmentsheuristics` off: 85.7 % right
  (+310), but language answers are right 85.8 % of the time instead of 92.2 % — on unseen files in
  languages it can name, +59 right for +191 wrong. On bench-m the same change was a pure gain (no wrong answers):
  the two benchmarks disagree, which is the point of having both.
- **9bc1c32 → 48c3c45: 38 files fixed, 6 regressed.** The six are PL/pgSQL `.sql` files, now answered
  SQLPL or TSQL: Synid's `.sql` rule is named `PLpgSQL` (Linguist's name) while the candidate is
  `PL/pgSQL`, so the rule is filtered out — the same name mismatch as Wolfram's on bench-m — and the
  new strategy order lets the SQLPL/TSQL rules decide before the classifier.

## Other identifiers

Every other tool runs from a pinned, reproducible setup (`reproduce.sh` rebuilds everything): a Docker
image per tool in `tools/external/` (versions and transitive dependencies pinned; rebuilt images give
identical answers), Jev through OpenRouter, a local model through Ollama or llama.cpp. Their names are
mapped to Linguist's only for synonyms (`tools/external/<tool>/names.csv`); see [COVERAGE.md](COVERAGE.md)
for what each can name at all.

| entry | right | note |
|---|---:|---|
| **Jev 1.13 among PL-ultimate-llm's candidates**, with file name | **93.2 %** | the extension's candidates from PL-ultimate-llm, Jev decides; 87.7 % on `unseen`, 90.6 % on `ambiguous-ext`; $0.62 |
| the same, file name not shown to Jev | 91.1 % | the candidates still come from the extension |
| GitHub Linguist 9.7.0 † | 99.5 % | trained on every file but 16 (languages it does not know: 0 / 16); 6.1 % without the file name |
| go-enry 2.9.6 † | 95.7 % | generated from Linguist v9.5.0; on the 62 files added since, in languages it knows: **22.6 %** (Jev: 79.0 %) |
| Jev 1.13 (OpenRouter), with file name | 89.3 % | $3.29 for the 3,404 files |
| Jev 1.13 (OpenRouter), content only | 82.3 % | 76.1 % on `unseen`, 84.5 % on `ambiguous-ext` — without the file name |
| Synid 48c3c45 † | 76.6 % | 5.4 % without the file name |
| Hyperpolyglot a55a3b5 † | 69.7 % | 2.8 % without the file name; no answer on 807 files (languages added since 2023) |
| cloc 2.10 | 33.8 % | names 250 of the 768 languages; right on 68.8 % of those |
| Pygments 2.21.0 | 32.3 % | 10.2 % from the content only (`guess_lexer`) |
| StarCoder2-3B (local, completion prompt) | 30.1 % | answers C, Python, C++ or JavaScript on 1,322 files; trained on The Stack v2 (from Software Heritage) — whether these files were in it is not checked |
| Magika 1.0.3 | 25.3 % | content types, not languages: names 96 of the 768; right on 78.7 % of those |
| Guesslang 2.2.1 | 21.8 % | 54 languages; reads the text only (on TensorFlow 2.10: 2.5 has no ARM build) |
| Jev 1.13, the `.m` study's 63 labels | 14.2 % | 54/54 on bench-m; here right on 94.9 % of the 509 files whose language has a label of its own — the label set, not the model, limits it |
| Kev-4B (local, llama.cpp), Linguist's languages | in progress | 47/54 on bench-m; on the first 132 files of its random-order run, 60.6 % (Jev on the same files: 84.8 %) |

Reading across: with the file name, the Linguist family wins on the files it was built from; without
it, every other tool collapses (2.8 – 10.2 %) while a decision model keeps 82 %. On files a tool was not
trained on, the decision model does better: 76.1 % vs 54.8 % for Synid on `unseen`; 79.0 % vs 22.6 %
for go-enry on the files added to Linguist after its snapshot (Jev's own training data is not known).
And the label set matters as much as the model: the same Jev, asked with the 63 labels of the `.m`
study, is perfect on bench-m and right on 14.2 % here. Giving it, for each file, the languages
PL-ultimate-llm associates with the file's extension — every source's claims plus what the extension
studies observed in Software Heritage — gets the best of both: 54/54 on bench-m and 93.2 % here (one
call per file for 94 % of them; a broad fallback for the rest). Caveat: the candidates include
Linguist's claims, and this benchmark's labels are Linguist's; and the `.m` observations come from the
study bench-m's files were drawn from — both benchmarks favour the mapping, which a benchmark of files
outside both would test.

See the [leaderboard](LEADERBOARD.md) and the [history of Synid versions](HISTORY.md).

## Files

| file | |
|---|---|
| `cases.csv` | one row per sample: path, git blob id, SWHID, expected language, accepted names (language + Linguist aliases), Linguist type, tags |
| `build_cases.py` | fetches Linguist and Hyperpolyglot at pinned revisions, writes `cases.csv` and `files/` |
| `baselines/` | Synid versions, default configuration |
| `entries/` | other configurations (content only, a strategy off) |
