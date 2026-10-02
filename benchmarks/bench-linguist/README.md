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

**Some languages are unknown to Synid.** 35 languages (100 files, all `unseen`: languages added to
Linguist after 2023) are not among Synid's syntaxes under any name: no strategy can name them.

**Labels follow Linguist's taxonomy.** Synid sometimes names a dialect or a neighbouring format where
Linguist files the sample under a broader language — `Systemd` for an `INI` unit file, `MSBuild` for
`XML`, `ASP` for `ASP.NET`, `CBM BASIC V2` for `BASIC`. These count as wrong here; they are
disagreements of granularity as much as errors.

Tags: `seen-in-training` / `unseen`; `ambiguous-ext` — the extension is claimed by two or more Linguist
languages (1,200 files: the cases where content must decide); `by-filename` — a sample identified by its
whole file name (`samples/<language>/filenames/`, 321 files).

## Findings — Synid 48c3c45

- **76.6 %** right overall (2,606 / 3,404); when it names a language, it is right 92.2 % of the time.
- **Seen vs unseen: 86.7 % vs 61.6 %** (unseen files in languages Synid knows; precision 98.7 % vs 82.5 %).
  The gap is the effect of training on the test files.
- **Ambiguous extensions on new files are the weak spot: 17.3 %** (56 / 323 unseen files in known
  languages); 212 of them end as `Text`.
- **Without its name, a file is almost never identified: 5.4 %** (`--content-only`, the file run as
  `file`). Synid's content strategies narrow the candidates an extension gives; on their own they
  rarely conclude.
- **The Pygments step trades recall for precision.** With `pygmentsheuristics` off: 85.7 % right
  (+310), but language answers are right 85.8 % of the time instead of 92.2 % — on unseen files in known
  languages, +59 right for +195 wrong. On bench-m the same change was a pure gain (no wrong answers):
  the two benchmarks disagree, which is the point of having both.
- **9bc1c32 → 48c3c45: 38 files fixed, 6 regressed.** The six are PL/pgSQL `.sql` files, now answered
  SQLPL or TSQL: Synid's `.sql` rule is named `PLpgSQL` (Linguist's name) while the candidate is
  `PL/pgSQL`, so the rule is filtered out — the same name mismatch as Wolfram's on bench-m — and the
  new strategy order lets the SQLPL/TSQL rules decide before the classifier.

See the [leaderboard](LEADERBOARD.md) and the [history of Synid versions](HISTORY.md).

## Files

| file | |
|---|---|
| `cases.csv` | one row per sample: path, git blob id, SWHID, expected language, accepted names (language + Linguist aliases), Linguist type, tags |
| `build_cases.py` | fetches Linguist and Hyperpolyglot at pinned revisions, writes `cases.csv` and `files/` |
| `baselines/` | Synid versions, default configuration |
| `entries/` | other configurations (content only, a strategy off) |
