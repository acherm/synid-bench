# bench-smola — files from GitHub repositories, labelled by a human or by Linguist

A benchmark of **real files in the wild**: the samples of
[smola/language-dataset](https://github.com/smola/language-dataset) (Santiago M. Mola, 2019–2022) —
**3,872 whole files from 3,872 GitHub repositories, in 261 languages**, each under its real file name.
**1,107 were labelled by a human** (`gold`); the other 2,765 carry the dataset's vote, which is
Linguist's own answer (`silver`). Where [bench-linguist](../bench-linguist/README.md) is Linguist's curated
sample set, this one is ordinary repository content; and its gold tier has **167 files where the human
corrected Linguist** (tag `human-overrode-linguist`) — the cases this benchmark exists for.

| | |
|---|---|
| cases | 3,872 files (all the samples with a language label; 175 `Unknown` or contested samples left out, see below), 261 languages, 500 B – 100 KB each |
| labels | `gold` (1,107): the human annotation (`human-<user>` in the dataset); `silver` (2,765): the dataset's `vote` — Linguist's answer of 2019–2022 for all but 2 (from Pygments' file-name lexer) |
| names | Linguist's names at [`76f88c6`](https://github.com/github-linguist/linguist/tree/76f88c6d3c22f8560d22d29854f24d9607f9edde) (as bench-linguist); the dataset's own labels are Linguist's names of v7.22.0 (2022), mapped in [`labels.csv`](labels.csv) |
| source | language-dataset at [`4d1827d`](https://github.com/smola/language-dataset/tree/4d1827d1018b922e03a48a5de5cb921a6762dda3) (2022-07-15, MIT; each sample keeps the licence of its repository) |
| files | **not stored here**: `build_cases.py` fetches the dataset at the pinned revision (it holds the bytes under `data/github.com/<owner>/<repo>/<commit>/<path>`) and checks each file against its git blob id |
| provenance | `qualified_swhid` = content + origin `https://github.com/<owner>/<repo>` + path; the column `commit` is the repository's commit (also its SWH revision id, `swh:1:rev:<commit>`). 8 cases drawn at random: 8 / 8 contents and 8 / 8 revisions are archived by Software Heritage (checked 2026-10-03; the others were not checked) |

```bash
python3 benchmarks/bench-smola/build_cases.py          # fetch the files (and rebuild cases.csv, identical); --cache DIR
python3 tools/run.py benchmarks/bench-smola --synid path/to/synid --label mytest
python3 tools/score.py benchmarks/bench-smola/results/mytest.jsonl \
    --baseline benchmarks/bench-smola/baselines/48c3c45-default.jsonl
```

`score.py` reports the gold and silver tiers apart. **Read the gold tier**; the leaderboard ranks over
both.

## Read it with care: labels from Linguist, samples chosen by Linguist

**The silver labels are Linguist's own answers.** Without a human annotation, the dataset's `vote` is
the answer of Linguist (2019–2022) on 2,763 of the 2,765 files. On the silver tier, the Linguist family
(Linguist, go-enry, Hyperpolyglot — and Synid, whose heuristics and classifier come from Hyperpolyglot)
is graded against itself: a high score there is agreement with Linguist, not accuracy.
The leaderboard therefore ranks on the **gold tier** (`headline_tier` in `card.json`) and shows all tiers
beside it. Only 3 files are byte-identical to Linguist samples (tag `in-linguist-samples`: `App.rbbas` ×2,
its `samples/Xojo/App.xojo_code`, and `Util.cls`); all three are silver, outside the headline, so no entry
is marked † (home turf) here.

**Every sample was chosen by Linguist.** The dataset's harvester searched GitHub for `language:"<X>"`
(GitHub's language detection is Linguist), scanned each repository with Linguist, and kept a file
Linguist assigned to X (one per repository, 500 B – 100 KB, about 20 per language). A human then checked
part of them. Files Linguist does not recognise at all are therefore absent, even from the gold tier: the
gold labels correct Linguist's *answers*, not its *selection*. The column `dataset_linguist` keeps
Linguist's 2022 answer for every case.

**The gold tier is not a random subset.** One annotator labelled nearly all of it (`smola`: 1,089 files;
`ajnavarro`: 26, 8 of them also checked by `smola`), language by language: 255 of the 402 files whose
label starts with an A are gold, and 24 languages have 15 gold files or more. 51 % of the gold files have an
ambiguous extension, against 20 % of the silver ones. So gold vs silver mixes two effects — who labelled,
and which languages; the column *gold, human = Linguist* (the 940 gold files where the human confirmed
Linguist's answer) separates them.

**Not scored in this version (175 samples, [`excluded.csv`](excluded.csv)):** 171 samples the human
labelled `Unknown` (not one of the dataset's languages: i3 configuration files under `.i3`, NEURON or
OPL models under `.mod`, data files…; Linguist had named 22 of them Modula-3, 15 AMPL), 2 whose `vote` is
`Unknown`, and 2 on which the two annotators disagree (`sicp.lisp`: NewLisp / Scheme; `iex.fish`: fish /
Shell). They are the seed of an open-set tier — where *no language* is the right answer — once the scorer
has that outcome. The list is at the end of this file.

**Taxonomy.** Labels are mapped to Linguist's names at 76f88c6, synonyms only
([`labels.csv`](labels.csv)): `Coq` → Rocq Prover, `Vim Script` → Vim script and `Wolfram Language`
(Linguist's `Mathematica` in 2022) were renamed since (tag `label-renamed`, 51 files; the old names stay
accepted, as Linguist aliases or the dataset's own name); `PL/SQL`, `PL/pgSQL`, `CUDA` are spelling
variants (PLSQL, PLpgSQL, Cuda); `KoLMafia ASH`, the dataset's own language in 2022, has been a Linguist
language since (KoLmafia ASH). The dataset's `Fortran` groups Linguist's Fortran and Fortran Free Form:
both accepted. Five cases have no Linguist name: `Literate Idris` (2; Linguist dropped it, `.lidr` is now
Idris's — Synid, cloc and Pygments still name it), `Gosu Template` (Pygments names it), `BCPL`,
`Visual Basic` (no tool here). As on bench-linguist, a dialect or a neighbouring format counts as wrong
(Synid's `ANTLR 4` for ANTLR's `.g4` files, for example).

**Duplicates.** 8 cases have the same bytes as another case (a file copied between repositories, e.g.
Mono's `DefaultWsdlHelpGenerator.aspx` three times); each is a separate case with its own origin.

**The human chose among the dataset's labels** (Linguist's languages of 2022, a few Rosetta Code and
Pygments names) or `Unknown`, so a few gold labels are the nearest one offered: 4 EasyCrypt files (`.ec`)
are labelled Coq (Rocq Prover here).

## Tags

| tag | gold | silver | meaning |
|---|---:|---:|---|
| `human-overrode-linguist` | 167 | — | the human label differs from Linguist's 2022 answer (`dataset_linguist`) |
| `ambiguous-ext` | 569 | 553 | the extension is claimed by two or more Linguist languages at 76f88c6 |
| `label-renamed` | 15 | 36 | the label's Linguist name changed since 2022 |
| `in-linguist-samples` | 0 | 3 | byte-identical to a Linguist sample (at 76f88c6, v9.7.0, v9.5.0, v8.0.0, v7.30.0, and Hyperpolyglot's 2023 copy): `App.rbbas` ×2 (Linguist files these bytes as `samples/Xojo/App.xojo_code`; the dataset says REALbasic) and `Util.cls` (OpenEdge ABL) |

The 167 corrections, by Linguist's answer → the human's: AGS Script → KoLmafia ASH (21, `.ash`), Harbour
→ Handlebars (13, `.hb`), SQL → PLSQL (11), Augeas → XML (6, Hero Lab files), eC → C (6), eC → Rocq
Prover (4, EasyCrypt files), Frege → HTML (4), then 102 files in 81 other pairs (Prolog → IDL, GLSL →
ShaderLab, Hack → HTML, Clean → XML, …).

## Composition

| | cases | languages | `ambiguous-ext` | no extension | Linguist type: programming / markup / data / prose / none |
|---|---:|---:|---:|---:|---|
| gold | 1,107 | 207 | 569 | 8 | 993 / 30 / 67 / 12 / 5 |
| silver | 2,765 | 201 | 553 | 35 | 2,639 / 86 / 27 / 13 / 0 |
| all | 3,872 | 261 | 1,122 | 43 | 3,632 / 116 / 94 / 25 / 5 |

About 20 files per language (15 to 24 for 172 of the 261), at most 32 (XML); 43 languages have fewer than 5.

## Findings — Synid 48c3c45

- **61.3 % on the gold tier** (679 / 1,107), 90.9 % on the silver one (2,513 / 2,765); 82.4 % overall.
  When it names a language, it is right 86.2 % of the time on gold, 97.2 % on silver.
- **Gold is harder for two reasons.** Where the human confirmed Linguist's answer (940 files), Synid is
  right on 71.3 %: the gold languages are harder ones (ambiguous extensions: Arc, Apex, Smalltalk,
  AMPL, Scheme…). Where the human corrected Linguist (167 files), it is right on **5.4 %** (9): it gives
  Linguist's 2022 answer on 60 of them and `Text` on 82.
- **`Text` is the main failure, as on bench-linguist:** 304 of the 428 gold files it misses (Arc 20,
  Apex 20, Smalltalk 17, AMPL 15, Scheme 15, RouterOS Script 13, Cycript 11, XML 11…): the Pygments step
  ends the chain with `Text` when no heuristic decides.
- **Taxonomy:** `ANTLR 4` for all 18 ANTLR `.g4` files (Linguist's name is ANTLR) — counted wrong.
- **Without its name, a file is almost never identified: 5.3 %** (`--content-only`).
- **9bc1c32 → 48c3c45: 74 files fixed, 12 regressed.** The 12 are PL/pgSQL `.sql` files, now TSQL,
  SQLPL, SQL or `Text`: the rule-name mismatch already seen on bench-linguist (Synid's `.sql` rule is
  named `PLpgSQL`, the candidate `PL/pgSQL`).

## Where a human corrected Linguist

The key result. On the 167 files of `human-overrode-linguist`, every tool that decides from the file
name first repeats Linguist's mistake:

- **The Linguist family is near-perfect where the human agreed with Linguist and fails where they did
  not.** Linguist 7.30.0 (2024) is right on 99.7 % of the 940 confirmed files and on 5 of the 167
  corrected ones; on 161 of them it gives Linguist's 2022 answer again. Newer releases do better —
  8.0.0: 17, 9.7.0: 38 (20 of them the KoLmafia ASH files, a language Linguist has added since; the
  other 18 are heuristics that changed: IDL, ShaderLab, Befunge, MATLAB…) — but still repeat the 2022
  answer on 113. go-enry, Hyperpolyglot and linguist-js do the same (122 – 142 repeats).
- **The corrections are mostly files whose extension misleads:** XML in `.aug` (Hero Lab), Handlebars in
  `.hb` (Harbour's extension), PLSQL in `.sql`, C in `.ec` (eC's), HTML in `.php` and `.fr`, JSON and
  YAML under other names. A tool that trusts the extension cannot get them.
- **So the content-only detectors, weak overall, are the best here:** Magika 1.0.3 is right on 44.3 %
  (74), vscode-languagedetection and Magika 0.5.1 on 35.3 %, Guesslang on 32.9 % — against 25.3 %,
  21.4 %, 11.6 % and 21.5 % over the whole benchmark. They read the bytes, and most corrected files are
  in languages or formats they can name (XML 17, HTML 7, C 8, JSON, YAML, Text, SQL, Shell…).
- **Synid sits with the name-first tools** (5.4 %): its content strategies narrow an extension's
  candidates but do not override them. Letting the content contradict the extension when it disagrees
  strongly is what this tag would measure.

Caveat: these 167 are the files where *Linguist of 2019–2022* was wrong and a human noticed. The
same tools' failures on files Linguist never assigned to a language are not measured here.

## Other identifiers

Every tool runs from its pinned Docker image (`tools/external/`); names mapped to Linguist's only for
synonyms. Sorted by gold accuracy. The last column counts the corrected files on which the entry gives
Linguist's 2022 answer — the error the human fixed.

**With the file name**

| entry | all | gold | silver | gold, human = Linguist | `human-overrode-linguist` | of these, Linguist's 2022 answer |
|---|---:|---:|---:|---:|---:|---:|
| GitHub Linguist 9.7.0 | 96.1 % | 87.4 % | 99.6 % | 98.8 % | 38 (22.8 %) | 113 |
| go-enry 2.9.6 | 95.6 % | 86.0 % | 99.4 % | 97.9 % | 32 (19.2 %) | 122 |
| GitHub Linguist 8.0.0 | 95.7 % | 85.6 % | 99.7 % | 99.0 % | 17 (10.2 %) | 137 |
| GitHub Linguist 7.30.0 | 95.7 % | 85.1 % | 99.9 % | 99.7 % | 5 (3.0 %) | 161 |
| go-enry 2.8.9 | 94.8 % | 84.1 % | 99.0 % | 97.8 % | 12 (7.2 %) | 142 |
| Hyperpolyglot a55a3b5 | 92.3 % | 79.9 % | 97.3 % | 92.6 % | 14 (8.4 %) | 126 |
| linguist-js 3.0.4 | 93.4 % | 79.3 % | 99.1 % | 91.9 % | 14 (8.4 %) | 129 |
| Synid 48c3c45 | 82.4 % | 61.3 % | 90.9 % | 71.3 % | 9 (5.4 %) | 60 |
| Synid 9bc1c32 | 80.8 % | 59.4 % | 89.4 % | 69.0 % | 9 (5.4 %) | 61 |
| Pygments 2.21.0 | 60.8 % | 51.7 % | 64.4 % | 59.7 % | 11 (6.6 %) | 42 |
| Pygments 2.19.2 | 60.2 % | 51.4 % | 63.7 % | 59.5 % | 10 (6.0 %) | 42 |
| Pygments 2.14.0 | 59.4 % | 50.7 % | 62.9 % | 58.5 % | 11 (6.6 %) | 43 |
| cloc 2.10 | 50.1 % | 47.9 % | 51.0 % | 52.7 % | 35 (21.0 %) | 44 |
| Neovim 0.12.5 filetype | 49.8 % | 44.3 % | 52.0 % | 48.8 % | 31 (18.6 %) | 30 |
| Rouge 5.1.0 | 45.3 % | 43.8 % | 45.9 % | 49.1 % | 23 (13.8 %) | 44 |
| scc 4.1.0 | 47.0 % | 40.7 % | 49.5 % | 46.0 % | 19 (11.4 %) | 30 |
| Chroma 2.27.0 | 42.5 % | 35.7 % | 45.2 % | 40.7 % | 12 (7.2 %) | 22 |
| tokei 15.0.0 | 46.1 % | 34.6 % | 50.7 % | 38.9 % | 17 (10.2 %) | 30 |
| ohcount 4.0.0 (Debian 4.0.0-5) | 35.4 % | 34.2 % | 35.8 % | 37.7 % | 25 (15.0 %) | 43 |
| Universal Ctags 6.2.1 | 27.5 % | 27.4 % | 27.6 % | 30.4 % | 17 (10.2 %) | 16 |
| gengo 0.15.0 | 35.0 % | 24.8 % | 39.1 % | 28.1 % | 11 (6.6 %) | 24 |

**Without it** (the file run as `file`; Magika, Guesslang, vscode-languagedetection, flourite and
file/libmagic read only the bytes by nature)

| entry | all | gold | silver | gold, human = Linguist | `human-overrode-linguist` | of these, Linguist's 2022 answer |
|---|---:|---:|---:|---:|---:|---:|
| Magika 1.0.3 | 25.3 % | 27.8 % | 24.2 % | 24.9 % | 74 (44.3 %) | 14 |
| Guesslang 2.2.1 | 21.5 % | 21.7 % | 21.4 % | 19.7 % | 55 (32.9 %) | 8 |
| vscode-languagedetection 1.0.23 | 21.4 % | 21.6 % | 21.3 % | 19.1 % | 59 (35.3 %) | 9 |
| Magika 0.5.1 | 11.6 % | 14.5 % | 10.5 % | 10.7 % | 59 (35.3 %) | 13 |
| Pygments 2.14.0, content only | 6.9 % | 11.8 % | 5.0 % | 11.0 % | 28 (16.8 %) | 0 |
| Pygments 2.19.2, content only | 7.3 % | 11.7 % | 5.5 % | 10.9 % | 27 (16.2 %) | 0 |
| Pygments 2.21.0, content only | 7.3 % | 11.7 % | 5.5 % | 10.9 % | 27 (16.2 %) | 0 |
| file 5.46 (libmagic) | 7.9 % | 11.6 % | 6.4 % | 9.5 % | 39 (23.4 %) | 0 |
| flourite 1.3.0 | 9.0 % | 8.7 % | 9.1 % | 7.2 % | 28 (16.8 %) | 3 |
| GitHub Linguist 7.30.0, content only | 3.8 % | 6.6 % | 2.7 % | 6.1 % | 16 (9.6 %) | 2 |
| GitHub Linguist 8.0.0, content only | 3.8 % | 6.6 % | 2.7 % | 6.1 % | 16 (9.6 %) | 2 |
| GitHub Linguist 9.7.0, content only | 3.8 % | 6.6 % | 2.7 % | 6.1 % | 16 (9.6 %) | 2 |
| go-enry 2.8.9, content only | 3.8 % | 6.4 % | 2.7 % | 5.9 % | 16 (9.6 %) | 1 |
| go-enry 2.9.6, content only | 3.8 % | 6.4 % | 2.7 % | 5.9 % | 16 (9.6 %) | 1 |
| Rouge 5.1.0, content only | 3.8 % | 6.3 % | 2.9 % | 4.5 % | 28 (16.8 %) | 1 |
| Neovim 0.12.5 filetype, content only | 2.6 % | 5.5 % | 1.5 % | 4.6 % | 18 (10.8 %) | 0 |
| Synid 48c3c45, content only | 5.3 % | 5.2 % | 5.4 % | 5.6 % | 5 (3.0 %) | 2 |
| linguist-js 3.0.4, content only | 2.9 % | 3.5 % | 2.6 % | 4.0 % | 1 (0.6 %) | 1 |
| Universal Ctags 6.2.1, content only | 2.0 % | 3.1 % | 1.6 % | 3.5 % | 1 (0.6 %) | 1 |
| Hyperpolyglot a55a3b5, content only | 2.0 % | 3.0 % | 1.6 % | 3.4 % | 1 (0.6 %) | 0 |
| Chroma 2.27.0, content only | 0.7 % | 1.4 % | 0.5 % | 0.9 % | 7 (4.2 %) | 0 |

Not run on this benchmark: highlight.js, PLangRec and the three Hugging Face models (`hf-*`), added to
`tools/external/` while these runs were made. On the machine's load at the time (other runs in parallel)
highlight.js had answered 1,724 of the 3,872 files after 74 minutes and PLangRec had printed nothing after
71; both were stopped. `python3 tools/run_all.py --bench bench-smola` runs the missing entries.

Reading across: on the whole benchmark the Linguist family wins (92 – 96 %), but on the silver tier it
is graded against itself (97 – 99.9 %). The gold tier shrinks its lead — 79 – 87 % — and the 167
corrected files reverse the order: there the content-only neural detectors lead and the Linguist family
is at 3 – 23 %. Without the file name every name-reading tool collapses (0.7 – 7.3 %), as on
bench-linguist. Language models (Jev, Kev-4B) were not run on this benchmark.

## Files

| file | |
|---|---|
| `cases.csv` | one row per sample: git blob id, file name, SWHID (origin, path), commit, expected Linguist name and accepted names, the dataset's label (`source_label`) and Linguist's 2022 answer (`dataset_linguist`), tier, tags |
| `labels.csv` | the dataset's labels → Linguist's names at 76f88c6 (`how`: exact / alias / none), with renames |
| `excluded.csv` | the 175 samples not scored, with their annotations |
| `build_cases.py` | fetches language-dataset, Linguist and Hyperpolyglot at pinned revisions; writes the three CSVs and `files/` |
| `card.json` | the benchmark card (`headline_tier`: gold) |
| `baselines/` | Synid versions, default configuration |
| `entries/` | other configurations (content only) and other identifiers |
| `reproduce.sh` | rebuilds the benchmark and every entry |
| `HISTORY.md`, `COVERAGE.md`, `LEADERBOARD.md` | generated by `tools/history.py`, `tools/coverage.py`, `tools/leaderboard.py` |

## Samples not scored (175)

<details><summary>The list (Linguist's 2022 answer, and the dataset's note when there is one)</summary>

| sample | why | Linguist (2022) | note |
|---|---|---|---|
| [`Adams123/OrgArquivos`: `dragon.rl`](https://github.com/Adams123/OrgArquivos/blob/44e237ded68ac94b146e0224c8d0b4b237db12b8/T2/T2/dragon.rl) | human: Unknown | Ragel |  |
| [`Astro-SMG/calc_mags`: `A0V_KURUCZ_92.SED`](https://github.com/Astro-SMG/calc_mags/blob/f08426a0831601f1c240e0b99d72d80c758b0400/vega_sed/A0V_KURUCZ_92.SED) | human: Unknown | sed |  |
| [`Azure/ccodashboard`: `AKS.m`](https://github.com/Azure/ccodashboard/blob/9740e2fc9f26ac4490d7a5fd7523abe0ac2a67d6/queries/AKS.m) | human: Unknown | Wolfram Language |  |
| [`BhallaLab/FindSim`: `b-arrestin2_20Feb2018_renamed.g`](https://github.com/BhallaLab/FindSim/blob/c1dad5c53d08b0933a3902da531be13572c13ddc/models/submodels/b-arrestin2_20Feb2018_renamed.g) | human: Unknown | GAP |  |
| [`BillFarber/ml-unit-test-example`: `xml.dcl`](https://github.com/BillFarber/ml-unit-test-example/blob/cc38ad2ef6b58a2e69866d87183144b617897ec5/src/main/ml-data/shaks200/xml.dcl) | human: Unknown | Clean |  |
| [`C-Bouthoorn/i3config`: `10-core.i3`](https://github.com/C-Bouthoorn/i3config/blob/de58cdbb9a1f2299182e25139b67cccd02b8a6f3/20-keys.i3/10-core.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`CCBR/Pipeliner`: `wgs.somatic.germline.calls.rl`](https://github.com/CCBR/Pipeliner/blob/477aecebac322aae9ed8fabee361baa2961a183f/Rules/wgs.somatic.germline.calls.rl) | human: Unknown | Ragel |  |
| [`CCTV-404/Zigbee`: `zmac_cb.pbi`](https://github.com/CCTV-404/Zigbee/blob/af227896803ef7891952487be42cbff8487d3001/Projects/zstack/Samples/GenericApp/CC2530DB/CoordinatorEB/Obj/zmac_cb.pbi) | human: Unknown | PureBasic |  |
| [`CandySunPlus/CY_erbi`: `g2b.cy`](https://github.com/CandySunPlus/CY_erbi/blob/089beb34602ce4be814e4ca109fb7135348e95b5/plugin/g2b.cy) | human: Unknown | Cycript |  |
| [`CarlosGS/open-radiation-detector`: `open_rad_detector-drl_map.plt`](https://github.com/CarlosGS/open-radiation-detector/blob/a887e9dcfe0f1568f1ef2a03ba7313825fc00f3b/Detector_PCB_1.0/Gerber/open_rad_detector-drl_map.plt) | human: Unknown | Gnuplot |  |
| [`Chadderz121/wii-ct-code`: `mod0.mod`](https://github.com/Chadderz121/wii-ct-code/blob/8aaf1a879d276b55c4eb2abdf916e2727e4dfa81/bad0/bad0Data/mod/mod0.mod) | human: Unknown | AMPL |  |
| [`Chaferfu/tal`: `formal_small.lima.ne`](https://github.com/Chaferfu/tal/blob/45ba9284d3b30f67d4b4a025abc171405fdef906/outputs/formal_small.lima.ne) | human: Unknown | Nearley | Tabular data |
| [`Cherifabk/ArabTAG-XMG`: `Verbal.mg`](https://github.com/Cherifabk/ArabTAG-XMG/blob/1f83391a59ca936a9002d95521014b374cf2161b/Verbal.mg) | human: Unknown | Modula-3 |  |
| [`DavidSkrundz/B`: `TypeResolve.b`](https://github.com/DavidSkrundz/B/blob/dfc2de8a88d34195007c38697ebc134e94964252/src/resolver/type/TypeResolve.b) | human: Unknown | Limbo |  |
| [`Eddie-CooRo/computer-architecture`: `SimpleAdd.hack`](https://github.com/Eddie-CooRo/computer-architecture/blob/bdc4df3abf39d94251dfea665d3fb1b294d068e5/07/StackArithmetic/SimpleAdd/SimpleAdd.hack) | human: Unknown | Hack |  |
| [`Endurance-Robotics/ChatBots`: `Orders.self`](https://github.com/Endurance-Robotics/ChatBots/blob/9e957067c84fe36d517220255947a88a3bf4d910/botabout/botlibre/scripts/Orders.self) | human: Unknown | Self |  |
| [`EricZimmerman/RECmd`: `BatchExample.reb`](https://github.com/EricZimmerman/RECmd/blob/41efec6fe08e17ee37287e4af781838a2391b4fe/BatchExamples/BatchExample.reb) | human: Unknown | Rebol |  |
| [`ErrkO/Manjaro-Desktop-Settings`: `config.i3`](https://github.com/ErrkO/Manjaro-Desktop-Settings/blob/3b246cfb71d467ca8131296d8518ba61e6e0a58e/config.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`GillesArcas/sapid-lisp`: `print.l`](https://github.com/GillesArcas/sapid-lisp/blob/2775bcf84a0ccf99a4d2aa327d2a3d254b3b9d5f/print.l) | human: Unknown | PicoLisp | Lisp (sapid-lisp) |
| [`HGldJ1966/guru-lang`: `checkh.g`](https://github.com/HGldJ1966/guru-lang/blob/a6b85e707d46ea7314ae5eb5e88c4b04deefccf6/tests/golfsock/checkh.g) | human: Unknown | GAP |  |
| [`HarshTrivedi/paraphrase-generation-web-demo`: `tt.g`](https://github.com/HarshTrivedi/paraphrase-generation-web-demo/blob/b2e1bbc946323b47b17e77ed1a08b0220591d463/bllip/models/WSJ/parser/tt.g) | human: Unknown | GAP |  |
| [`HartmutBorth/PLASIM`: `N032_surf_1731.sra`](https://github.com/HartmutBorth/PLASIM/blob/ea4d2d8d11d8b4c8de2ed947f3362f3932e620c3/plasim/dat/T21/N032_surf_1731.sra) | human: Unknown | PowerBuilder |  |
| [`HauyuChen/Parking-System`: `hal_assert.pbi`](https://github.com/HauyuChen/Parking-System/blob/171034f27df89d7c3e60a78b8dd163389c21bb85/Parking-ZigBee/ParkingSystem/CC2530DB/CoordinatorEB/Obj/hal_assert.pbi) | human: Unknown | PureBasic |  |
| [`Heracles-Brigade/rotbd`: `multrc02.LGT`](https://github.com/Heracles-Brigade/rotbd/blob/690b67d7b9f01460c5d7f588a608b2748c990ded/src/mp/race/multrc02/multrc02.LGT) | human: Unknown | Logtalk |  |
| [`HrafnkellNK/dotfiles`: `config.i3`](https://github.com/HrafnkellNK/dotfiles/blob/258c458bd82d07a7dbb697dd316069a3d0b4eff8/config.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`IJTAG-Ecosystem/Public`: `ScanCell.icl`](https://github.com/IJTAG-Ecosystem/Public/blob/c09f43976b4941104e35f7ca227931afc6406037/ScanCell.icl) | human: Unknown | Clean |  |
| [`JeeJay23/dotfiles`: `config.i3`](https://github.com/JeeJay23/dotfiles/blob/9ef75d37851dff19f535d75daf998859fb390159/config.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`JohannesPfeifer/DSGE_mod`: `Gali_2008_chapter_5_commitment.mod`](https://github.com/JohannesPfeifer/DSGE_mod/blob/736e0a66d6908ea3acda5c34cf2f7e04448293a7/Gali_2008/Gali_2008_chapter_5_commitment.mod) | human: Unknown | AMPL |  |
| [`LubomirBednar/PhD`: `E7_RT-qPCR_template.asy`](https://github.com/LubomirBednar/PhD/blob/d5e04c89361b06905b0e00e1a79be89bd69849e9/E7/E7_RT-qPCR_template.asy) | human: Unknown | Asymptote | epRealPlex Assay File V4 |
| [`MagerValp/ArcadeGameSelector`: `AGS2Menu.e`](https://github.com/MagerValp/ArcadeGameSelector/blob/e21f22ff84ca3d6014e95e2c3c45214bbeaa6c3f/AGS2Menu.e) | human: Unknown | Eiffel |  |
| [`MagicLu550/MyIdealLang`: `program.nl`](https://github.com/MagicLu550/MyIdealLang/blob/9768acdc36cc6209a38497bd81b9f41c5c1a9d06/program.nl) | human: Unknown | NewLisp |  |
| [`Manitary/advent-of-code`: `18_11.mg`](https://github.com/Manitary/advent-of-code/blob/803f38a11d2e7980d46b42bb80bc5e0cc2c31830/2018/18_11.mg) | human: Unknown | Modula-3 |  |
| [`MartynEcc0/Custom-Light-Bars`: `expressions_primary_verbose_front_rear.ec`](https://github.com/MartynEcc0/Custom-Light-Bars/blob/20ce516e8ad07015087b640d3e740b34634a6286/Pakistan%20v1.2%20-%20Copy/Pakistan%20Master/Previous/v1_08/Include/expressions_primary_verbose_front_rear.ec) | human: Unknown | eC |  |
| [`MatthieuAnsart/loadForecast`: `patset.mod`](https://github.com/MatthieuAnsart/loadForecast/blob/6fa3c1f93f6e79e8056d4260f300ead26e3f258e/IBM/ILOG/CPLEX_Studio1262_x64/opl/examples/opl/BasketballScheduling/patset.mod) | human: Unknown | AMPL | IBM ILOG Script / IBM OPL (AMPL-like) |
| [`MetaCell/NEURON-UI`: `hsyn.mod`](https://github.com/MetaCell/NEURON-UI/blob/2a642c78a127a500ba139b83bb8d263035b52be7/neuron_ui/models/PTCell/mod/hsyn.mod) | human: Unknown | AMPL | NEURON MODL |
| [`NIDCD/lsnm_in_python`: `lgnsev1h.w`](https://github.com/NIDCD/lsnm_in_python/blob/c244ba39627840485919ca395c08287eded3cf2c/visual_model/subject_19/lgnsev1h.w) | human: Unknown | CWeb |  |
| [`OneIdentity/Polypkg`: `pp.back.kit`](https://github.com/OneIdentity/Polypkg/blob/20ea9e5170a83daec883dd7fa69914dfb00eaa32/pp.back.kit) | human: Unknown | Kit |  |
| [`PSEmulator/Client`: `ugd03.zpl`](https://github.com/PSEmulator/Client/blob/6f644a754736b7a44f4fd660562dbe1bf1ade87f/expansion1/expansion1/ugd03.zpl) | human: Unknown | Zimpl |  |
| [`Passw4r/dotfiles`: `config.i3`](https://github.com/Passw4r/dotfiles/blob/a068dd0db007aa84d1e8c5539de129e41390305f/config.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`PavlezT/Tiva-MCU-TM4C123G-LaunchPad`: `bme280_old.rl`](https://github.com/PavlezT/Tiva-MCU-TM4C123G-LaunchPad/blob/88256c7ba6b5ac657f10a13b3e6cee4afd6b26b0/blinkyAlien/Debug/bme280_old.rl) | human: Unknown | Ragel |  |
| [`RayPragma/jmrccz`: `call_jmrcc.zpl`](https://github.com/RayPragma/jmrccz/blob/1de90644cca0fac0894a585e302d84fc76057b17/call_jmrcc.zpl) | human: Unknown | Zimpl |  |
| [`Roniius/hoimi`: `hoimi.mod`](https://github.com/Roniius/hoimi/blob/ac85a9c815483b9b309f332cb94ea2a330ffeb59/hoimi.mod) | human: Unknown | AMPL | Hearts of Iron 4 mod |
| [`Ruixel/YACY`: `Castle.cy`](https://github.com/Ruixel/YACY/blob/49835f35a0d114d60c20e91f9c5f7707db77a2ec/res/levels/Castle.cy) | human: Unknown | Cycript |  |
| [`S25214/.dot`: `.i3`](https://github.com/S25214/.dot/blob/4a05cd1a5f830a4aa25f0b3e2bb402f7929353b2/.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`SarahChabane/correct-by-construction-SR-systems`: `abstioa.ec`](https://github.com/SarahChabane/correct-by-construction-SR-systems/blob/c6de239cb1b85ebfedbdb6f19ecf41d73d5b8010/abstioa.ec) | human: Unknown | eC |  |
| [`Shanjaq/peanut`: `inferno.hc`](https://github.com/Shanjaq/peanut/blob/1f590eaac0c24cfc79a3c38b3a9d8be9f7e45455/phcc/inferno.hc) | human: Unknown | HolyC | HexenC (QuakeC-based) |
| [`Shanjaq/uhexen2-progs`: `entity.hc`](https://github.com/Shanjaq/uhexen2-progs/blob/f9eb2b52316d9cdeae1acb06774ccf3b18e07786/h2/entity.hc) | human: Unknown | HolyC | HexenC (QuakeC-based) |
| [`SopaXorzTaker/fxesplus`: `M610415.DCL`](https://github.com/SopaXorzTaker/fxesplus/blob/0d7f01b22e60db41688184491be1d8b25a60fdf1/tools/u8-sdk/M610415.DCL) | human: Unknown | Clean |  |
| [`Spirent/cloudstress`: `config.zpl`](https://github.com/Spirent/cloudstress/blob/602783b84dbcb4363195dd359ef7f60d710d5f48/config.zpl) | human: Unknown | Zimpl |  |
| [`SquidDev/urn`: `function.lisp`](https://github.com/SquidDev/urn/blob/6e6717cf1376b0950e569e3771cb7e287aed291d/lib/data/function.lisp) | human: Unknown | Common Lisp |  |
| [`ThatsNotAUsername/MEMo`: `matrix.eq`](https://github.com/ThatsNotAUsername/MEMo/blob/9d97bd0b2e4eed22e2f9265e87dd3e50d9aefde6/MMB_github/matrix.eq) | human: Unknown | EQ |  |
| [`TrumpyGoad/Project_EUROPA`: `Project_EUROPA.mod`](https://github.com/TrumpyGoad/Project_EUROPA/blob/99965591f8a2a701771ef602a95133f650becd68/Project_EUROPA.mod) | human: Unknown | AMPL | Hearts of Iron 4 mod |
| [`Ttreintaysiete/chaves`: `chaves.pro`](https://github.com/Ttreintaysiete/chaves/blob/9972f5b735048064f86628ce642d3d94d7502cea/v2/hardware/chaves.pro) | human: Unknown | INI | EAGLE AutoRouter Statistics |
| [`WebGLSamples/WebGLSamples.github.io`: `GlobeInner.ma`](https://github.com/WebGLSamples/WebGLSamples.github.io/blob/79a3ef4783f8d97b3d0332b7cbd16ffe5dfbc2f9/aquarium/source_assets/Scenes/GlobeInner.ma) | human: Unknown | Wolfram Language |  |
| [`adam-cowley/journeyplanning`: `all.cy`](https://github.com/adam-cowley/journeyplanning/blob/ffc7b29766b2d9f030a070b4aedbbb67aa55e0a3/all.cy) | human: Unknown | Cycript |  |
| [`adobe-fonts/source-han-sans`: `cidfontinfo.OTC.HW.SC`](https://github.com/adobe-fonts/source-han-sans/blob/e251b7a4fecc7c5bc57d25cb2c2e92a3e8980a39/Regular/OTC/cidfontinfo.OTC.HW.SC) | human: Unknown | Scala |  |
| [`albandescottes/EIT`: `formal-tst.NE.key.04oct95_small.txt.ref.ne`](https://github.com/albandescottes/EIT/blob/999139b2e56f2ff7e74bf29865648688d8d0bdef/files/v/formal-tst.NE.key.04oct95_small.txt.ref.ne) | human: Unknown | Nearley | Text annotated with name entity tags |
| [`alecmuffett/eotk`: `nginx.conf.txt`](https://github.com/alecmuffett/eotk/blob/d6021400df94479fe28d928aecacff98d1bc7822/templates.d/nginx.conf.txt) | human: Unknown | Awk | Nginx config with custom templating and bogus Awk modeline |
| [`amunch/Language-to-Latex`: `test.eq`](https://github.com/amunch/Language-to-Latex/blob/42ff1648fe9035ff9753df0f08092490bdf3ed91/data/data/final_data/test.eq) | human: Unknown | EQ |  |
| [`andrealani/COOLFluiD`: `restartRDS.surf.plt`](https://github.com/andrealani/COOLFluiD/blob/cd73fc5e70209808b75c6440df68cd2b01225613/plugins/NavierStokes/testcases/DoubleEllipse/restartRDS.surf.plt) | human: Unknown | Gnuplot |  |
| [`anotherkeebler/DiceGen`: `diceware.wordlist.asc`](https://github.com/anotherkeebler/DiceGen/blob/fc63e355eb881b894984420151d0db3169205508/diceware.wordlist.asc) | human: Unknown | AGS Script |  |
| [`archipaorg/k8s-icl`: `policyrule.icl`](https://github.com/archipaorg/k8s-icl/blob/f1269b8dd3264822af46433c220d608488592cf6/v1.6.6/v1beta1/policyrule.icl) | human: Unknown | Clean |  |
| [`areiman/PFO-ADC-DER-Testbed`: `fncs.zpl`](https://github.com/areiman/PFO-ADC-DER-Testbed/blob/2ecc3ef94a995a594e05cafacd58e68d4ea487c3/ADC-DER-Testbed/PythonTest/Python/fncs.zpl) | human: Unknown | Zimpl |  |
| [`arinabondarenko/DL_homework_2`: `task_2.txl`](https://github.com/arinabondarenko/DL_homework_2/blob/dbfde3172fc647e1d00d73a31aa0a26e59558c2a/task_2.txl) | human: Unknown | TXL |  |
| [`arne-cl/codra-rst-parser`: `tt.g`](https://github.com/arne-cl/codra-rst-parser/blob/9f39d7f1679ec82f587cb99efa956ed830924d86/Tools/CharniakParserRerank/first-stage/DATA/EN/tt.g) | human: Unknown | GAP |  |
| [`assaflavi/peptalk`: `1DKX.mat.hb`](https://github.com/assaflavi/peptalk/blob/daf63f1768449854e814ddce656a1d302c8fbe07/data/peptiDB/unbound/MotifAnalysis/data/1DKX/1DKX.mat.hb) | human: Unknown | Harbour |  |
| [`avais25/Lustre-examples`: `ROADS.ec`](https://github.com/avais25/Lustre-examples/blob/2dd06a0bed855bba1a1aa0e5685d9fbc8cfae4a9/Question2/ROADS.ec) | human: Unknown | eC |  |
| [`ayuryshev/config`: `A-main.i3`](https://github.com/ayuryshev/config/blob/c00693a20028eb72c7541e12159576a0b1ffc3fb/i3/src/A-main.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`b-cakir/hecke-operator`: `optimized.mg`](https://github.com/b-cakir/hecke-operator/blob/6d6b57400ed54ef637c2b49550448000e999eab2/optimized.mg) | human: Unknown | Modula-3 |  |
| [`badocksbi/BADock`: `2B4J_l_b.pdb.HB`](https://github.com/badocksbi/BADock/blob/c79e1be5e23f254d64414ddfe342c1b75336536a/db/AffinityBenchmark/2B4J_l_b.pdb.HB) | human: Unknown | Harbour |  |
| [`bambenek/block-doh`: `db.doh`](https://github.com/bambenek/block-doh/blob/57e3698b959b8eda5df6b8698a0187b4ad1df074/db.doh) | human: Unknown | Stata |  |
| [`banneker-aztlan/intro-to-python`: `Sc_A_0.sed`](https://github.com/banneker-aztlan/intro-to-python/blob/a2633812d2591c036d629265579b4b7b88ed001a/data/seds/Sc_A_0.sed) | human: Unknown | sed |  |
| [`bbvbb/ChineseFan`: `ChineseFan-0.0.1-zh_CN.mse`](https://github.com/bbvbb/ChineseFan/blob/d79f1a7e2ea3565d918cab12752a01e81d67423e/ChineseFan-0.0.1-zh_CN.mse) | human: Unknown | — |  |
| [`begoon/acm`: `text05.tst`](https://github.com/begoon/acm/blob/05472eaa0fff7abb6679826085da5e0c990df4cb/ch24.org/2011/Pre-round,%202011.02.12/R/text05.tst) | human: Unknown | Scilab |  |
| [`bernerdschaefer/sgheme`: `sicp.lisp`](https://github.com/bernerdschaefer/sgheme/blob/5007b2763c8280668d3bb72b9e50c17a057bc8ee/sicp.lisp) | humans disagree (human-ajnavarro: NewLisp, human-smola: Scheme) | NewLisp |  |
| [`blackcata/1D-RANS`: `CHANNEL_0180_mean_prof.plt`](https://github.com/blackcata/1D-RANS/blob/cdf7efa59778749b0f492cfa1cabda342327ec6f/DATA/CHANNEL_0180_mean_prof.plt) | human: Unknown | Gnuplot |  |
| [`breuleux/quaint`: `index.q`](https://github.com/breuleux/quaint/blob/8c538dfde32183f1116f6c661835f35f6c249d21/scaffold/index.q) | human: Unknown | q |  |
| [`byackee/jarvis-rivescript`: `cerveaudebase.rs`](https://github.com/byackee/jarvis-rivescript/blob/f89853fb359083cf6c8b4ddcd7b363986fadb6ce/eg/brain/fr/cerveaudebase.rs) | human: Unknown | XML |  |
| [`carloop/hardware`: `CarloopXL-v3.1.pro`](https://github.com/carloop/hardware/blob/7fe80cc13adf8100ad54f4a6c7fb054c739a4806/CarloopXL.v3/CarloopXL-v3.1.pro) | human: Unknown | Prolog | EAGLE AutoRouter Statistics |
| [`chatopera/conversation-sampleapp`: `zh_CN.weather.ms`](https://github.com/chatopera/conversation-sampleapp/blob/0e7928b2cf846cfd7c82987450f9ace5c522d4fa/app/zh_CN.weather.ms) | human: Unknown | MAXScript |  |
| [`chrishwiggins/orly`: `screendump.asc`](https://github.com/chrishwiggins/orly/blob/990dc81d1b7cb228f57929a0b62c76de5b354cb2/screendump.asc) | human: Unknown | AsciiDoc |  |
| [`ckgyarmathy/debian_config`: `config_.i3`](https://github.com/ckgyarmathy/debian_config/blob/ca5f883bfe5e57218f6c62aa8528a53e011ffbcc/config_.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`codeneomatrix/multics-history`: `generate_cmf.ec`](https://github.com/codeneomatrix/multics-history/blob/09daeb08947c07f2be770e2da3db0a72a3541c70/source/Multics/ldd/system_library_tools/object/generate_cmf.ec) | human: Unknown | eC |  |
| [`compomics/colims`: `allSpectra.CID.ITMS.iso_2.apl`](https://github.com/compomics/colims/blob/4936195068337ba0c5236830f7f5f84e05d73ae5/colims-distributed/src/test/resources/data/maxquant/maxquant_SILAC_integration/combined/andromeda/allSpectra.CID.ITMS.iso_2.apl) | human: Unknown | APL |  |
| [`corywalker/expreduce`: `time.m`](https://github.com/corywalker/expreduce/blob/0a346d0d4ef1800bf7762f4cba0fb7e9cee0101a/expreduce/resources/time.m) | human: Unknown | Wolfram Language |  |
| [`cswaroop/opl`: `timetabling.mod`](https://github.com/cswaroop/opl/blob/7098061d01ac85d1a84f1580019ebb2b8597db3b/timetabling/timetabling.mod) | human: Unknown | AMPL | IBM ILOG Script / IBM OPL (AMPL-like) |
| [`cycyustc/isotracks`: `ptcri_ovh0.20.ovhe0.50.z0.00555.y0.25409.HB`](https://github.com/cycyustc/isotracks/blob/3d1f71b58af375db67f5cb8a77c879b50c702911/isotrack/mesa/MESA_KS_DB/ptcri_ovh0.20.ovhe0.50.z0.00555.y0.25409.HB) | human: Unknown | Harbour |  |
| [`danvratil/kde-sdk-images`: `html.dcl`](https://github.com/danvratil/kde-sdk-images/blob/ae9e971354debf8ddc58496f42ea130b5737e65d/packages/SOURCES/html.dcl) | human: Unknown | Clean |  |
| [`darrenjw/smfsb`: `autoreg-3-1.mod`](https://github.com/darrenjw/smfsb/blob/3bc38adcea5097812322599dd41d1d9511c62270/models/autoreg-3-1.mod) | human: Unknown | AMPL |  |
| [`derele/Eimeria_Lab`: `E7_112018_Eim_RT-qPCR_template.asy`](https://github.com/derele/Eimeria_Lab/blob/f98fbfd96a65bfd1c25cca068d36d2452b73c70c/data/3_recordingTables/E7_112018_Eim_RT-qPCRs/E7_112018_Eim_RT-qPCR_template.asy) | human: Unknown | Asymptote | epRealPlex Assay File V4 |
| [`derele/Mouse_Eimeria_Databasing`: `template0509plate2.asy`](https://github.com/derele/Mouse_Eimeria_Databasing/blob/1ce069d2b596e7ab037d44e07b070948df4fee65/data/Eimeria_detection/raw_qPCR/bavariaqPCR2015/raw/template0509plate2.asy) | human: Unknown | Asymptote | epRealPlex Assay File V4 |
| [`doublec/shen-wasp`: `toplevel.kl.ms`](https://github.com/doublec/shen-wasp/blob/0792d0e019554b2788f883ac667454ff5ab83088/compiled/toplevel.kl.ms) | human: Unknown | MAXScript |  |
| [`ebladrocher/scriptinstall`: `ihotkeys.i3`](https://github.com/ebladrocher/scriptinstall/blob/c11dce8abf84246ad9c12975bd65f654ad392948/i3/ihotkeys.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`elpopisencio/.dotfiles`: `.i3`](https://github.com/elpopisencio/.dotfiles/blob/bdc87cc9b769e877b33712d3cdf1df642aced340/.i3) | human: Unknown | Modula-3 |  |
| [`ernell/ABB-RAPID-UTILITY-LIBRARY`: `LEERULZ.mod`](https://github.com/ernell/ABB-RAPID-UTILITY-LIBRARY/blob/8577ae71073b8547c7fc0cec620c92a1e5e37621/Contributions/LeeJustice/LEERULZ.mod) | human: Unknown | AMPL |  |
| [`evilmartians/foundry-lib`: `integer.fy`](https://github.com/evilmartians/foundry-lib/blob/9ab4ad8a5625c8c852e04adf8ce463b4c9320212/rtl/integer.fy) | human: Unknown | Fancy |  |
| [`fish-shell/fish-shell`: `iex.fish`](https://github.com/fish-shell/fish-shell/blob/ac2eed2ffa71aa6db08dad2ea6f6b0dd89f815d6/share/completions/iex.fish) | humans disagree (human-ajnavarro: Shell, human-smola: fish) | fish |  |
| [`frznlogic/ipsysctl-tutorial`: `xml.dcl`](https://github.com/frznlogic/ipsysctl-tutorial/blob/0dda94cf007a68cd70d6c886de3e1acb6449d91d/styles/dsssl-stylesheets/dtds/decls/xml.dcl) | human: Unknown | Clean |  |
| [`gazingatnavel/ucf-spring2017-cda3103-spim-project-tests`: `test-spim-rtype.asc`](https://github.com/gazingatnavel/ucf-spring2017-cda3103-spim-project-tests/blob/e132e36f07a3621751cd8981b5bfa717e6e8571c/test-spim-rtype.asc) | human: Unknown | AGS Script |  |
| [`google/digitalassetlinks`: `4300-check-relation.pb`](https://github.com/google/digitalassetlinks/blob/d893749ee3c84b31f72b552a7ed333789c3235d3/compatibility-tests/v1/4000-query-matching/4300-check-relation.pb) | human: Unknown | PureBasic |  |
| [`haggi/OpenMaya`: `simpleShadingNetwork.ma`](https://github.com/haggi/OpenMaya/blob/746e0740f480d9ef8d2173f31b3c99b9b0ea0d24/src/mayaToCorona/mayaToCoronaExamples/scenes/simpleShadingNetwork.ma) | human: Unknown | Wolfram Language |  |
| [`hpd/DigitalEmily`: `Emily_2_1_Lightstage_Cameras_Animated.ma`](https://github.com/hpd/DigitalEmily/blob/8bb2583fb41e40c58ee2da8bb7988732e2031624/maya/scenes/Emily_2_1_Lightstage_Cameras_Animated.ma) | human: Unknown | Wolfram Language |  |
| [`hustlingchen/ALFM`: `5.item.factor`](https://github.com/hustlingchen/ALFM/blob/ca32c2724d4df21d5abe4b9602f2351936a76561/model/alfm/Musical_Instruments/5.item.factor) | human: Unknown | Factor |  |
| [`igorwfaoro/keyboard-autocomplete`: `keys.ik`](https://github.com/igorwfaoro/keyboard-autocomplete/blob/4117bb813d46ad85f8aa4c1f16ba7f5695731822/data%20-%20Copia/keys.ik) | human: Unknown | Ioke |  |
| [`isabelangelo/mcfost`: `SSTTAUJ042021.4+281349_reduced.sed`](https://github.com/isabelangelo/mcfost/blob/a5fa2d134db90e5c999ef91ece10b503b0817473/seds/reduced_seds/SSTTAUJ042021.4+281349_reduced.sed) | human: Unknown | sed |  |
| [`james101c/kafka-blend`: `pdb.LOL`](https://github.com/james101c/kafka-blend/blob/a4045436cb16740a4825828a3c28d5ec8a230965/data/datatourney/development/tourney/200110/pdb/pdb.LOL) | human: Unknown | LOLCODE |  |
| [`jgallowa07/SLiMSimulations`: `MyRecipe9_0_1.E`](https://github.com/jgallowa07/SLiMSimulations/blob/fda6455968359235cf4dcb443b3be4984708e3e3/MyRecipes1/MyRecipe9_0_1.E) | human: Unknown | Eiffel |  |
| [`jhmaloney/GP-Mods`: `Menu.gp`](https://github.com/jhmaloney/GP-Mods/blob/36044f3cca7770c0b7f983c176b56926a8b72bcd/runtime/lib/Menu.gp) | human: Unknown | Gnuplot |  |
| [`jjlee/w3c-markup-validator-commandline`: `xhtml1.dcl`](https://github.com/jjlee/w3c-markup-validator-commandline/blob/730033b1be7636b211d6163c229bbb138baa1a4a/etc/sgml-lib/REC-xhtml1-20000126/xhtml1.dcl) | human: Unknown | Clean |  |
| [`jldbc/gunsandcrime`: `Moody Replication and Improvements.do`](https://github.com/jldbc/gunsandcrime/blob/547aee98349ae2f9b9a2116cfe60ccfebc5c80e7/Moody%20Replication%20and%20Improvements.do) | human: Unknown | Stata |  |
| [`khagag/tiva_c_dynamic_drivers`: `tm4c123gh6pm_startup_ccs.rl`](https://github.com/khagag/tiva_c_dynamic_drivers/blob/97fccef2e18580c690883f1257c75eee2add9ea1/Release/tm4c123gh6pm_startup_ccs.rl) | human: Unknown | Ragel |  |
| [`khanhvu207/competitiveprogramming`: `room.i3`](https://github.com/khanhvu207/competitiveprogramming/blob/5cc7b020c0fd64b6d84e4c0cba1256225803814b/CST%202019/Thầy%20Vinh/T13/CHAMTUAN13/debai/room/room.i3) | human: Unknown | Modula-3 |  |
| [`klayoutmatthias/si4all`: `process.xs`](https://github.com/klayoutmatthias/si4all/blob/51bff19ee59377e46fc373b6c3b74fd153c6e53a/process.xs) | human: Unknown | XS |  |
| [`kragen/stoneknifeforth`: `onescreen.tbf1`](https://github.com/kragen/stoneknifeforth/blob/67ae4f422d4b5740cf335c0894e80a007744f0d2/onescreen.tbf1) | human: Unknown | — | Forth-inspired toy language |
| [`lang-flags/de`: `a.shen`](https://github.com/lang-flags/de/blob/10a6d633dd70807d9355cb59e619c5408e0c5c42/a.shen) | human: Unknown | Shen |  |
| [`lang-flags/fr`: `a.hb`](https://github.com/lang-flags/fr/blob/352067103548b749c7823914ced25865ce38b9b5/a.hb) | human: Unknown | Harbour |  |
| [`larzm42/dom4inspector`: `GuardiansOfTheDeep.dm`](https://github.com/larzm42/dom4inspector/blob/1f39fbc7fe94c2c81a7c82ce75a59b776b8a0c9b/mods/ExpandedMods/Globals/GuardiansOfTheDeep.dm) | human: Unknown | DM |  |
| [`linboqiao/EEA`: `ru.g`](https://github.com/linboqiao/EEA/blob/5b6ffa08d1972946d6941ac6b7ae57f9fe805dcc/limo-re/parser/bllip-parser/first-stage/DATA/EN/ru.g) | human: Unknown | GAP |  |
| [`lisawray/fiftyshades`: `50shades.pb`](https://github.com/lisawray/fiftyshades/blob/a316281545f88b212b6afdfa51e05e0cf3de74fe/50shades.pb) | human: Unknown | PureBasic |  |
| [`llinaresvicent/dotfiles`: `.i3`](https://github.com/llinaresvicent/dotfiles/blob/535d7cb7512ed6c14a39bc0c78c44074a6476285/.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`luxe/unilang`: `str_to_bdf_segments.hcp`](https://github.com/luxe/unilang/blob/749e8285ff61aed471f3b37ba2e4a05aa75cd7f7/source/code/utilities/graphics/imgui/ui/draw/text/str_to_bdf_segments.hcp) | human: Unknown | — |  |
| [`ma-ath/Amplificador-de-Potencia`: `Trabalho.ALS`](https://github.com/ma-ath/Amplificador-de-Potencia/blob/eb5828dd4ff27abb62e4369cfa17e55c920f02dd/eletronica-iv-trabalho-PSpiceFiles/Trabalho/Trabalho.ALS) | human: Unknown | Alloy |  |
| [`madison-traynham/OrcadParts`: `x7r_0603.caps.dcl`](https://github.com/madison-traynham/OrcadParts/blob/538540ffc5a82af6ddb72910f4ea016fe017e2a0/pcb_lib/x7r_0603.caps.dcl) | human: Unknown | Clean |  |
| [`magnesium-lang/scratch`: `scratch.mg`](https://github.com/magnesium-lang/scratch/blob/126aac1e82f033f387cc4b0ed74ffc1e23a7797e/scratch.mg) | human: Unknown | Modula-3 |  |
| [`mandosrex/AoE3ImpMod_Base`: `sonoraLarge.xs`](https://github.com/mandosrex/AoE3ImpMod_Base/blob/69b6d477f39f45f54689d0b6104d544756248924/RMM/sonoraLarge.xs) | human: Unknown | XS |  |
| [`matej-macak/Neuron_Vagrant`: `h.mod`](https://github.com/matej-macak/Neuron_Vagrant/blob/1d40cea1b931629bac4fd53d064d753b21e7ceea/Python3.4/Mods/h.mod) | human: Unknown | AMPL | NEURON MODL |
| [`materialsvirtuallab/snap`: `displace.mod`](https://github.com/materialsvirtuallab/snap/blob/d2b9c3c618cc3a808ca2f8cc3267211b98105226/Mo/usage/elastic_example/displace.mod) | human: Unknown | AMPL | LAMMPS |
| [`mcimini/GradualizerDynamicSemantics`: `fpl.mod`](https://github.com/mcimini/GradualizerDynamicSemantics/blob/c013ae31547a81e5214e0fa39c1999b86c9a0ca4/GradualFpl_mechanized_proofs/fpl.mod) | human: Unknown | AMPL |  |
| [`mcimini/TypeSoundnessCertifier`: `stlc_par_letrecWithType.mod`](https://github.com/mcimini/TypeSoundnessCertifier/blob/321d1367339421b650557eb3b1745995fde4a369/repo/stlc_par_letrecWithType.mod) | human: Unknown | AMPL |  |
| [`mehmetharas/banner`: `BANNER.FY`](https://github.com/mehmetharas/banner/blob/8256889bbdfc82ea8af84ff4386bb7eaf2f9d348/BANNER.FY) | human: Unknown | Fancy |  |
| [`menski/dotfiles-old`: `.Xresources.color.self`](https://github.com/menski/dotfiles-old/blob/2bf5eea12ad781f78a063e1f0941e0673c9c7a93/xorg/.Xresources.color.self) | human: Unknown | Self |  |
| [`mmariani/tamc.pas`: `gnuchess.boo`](https://github.com/mmariani/tamc.pas/blob/e54b3d7427422d6b6daf5a88c08bdb752f720bff/gnuchess.boo) | human: Unknown | Boo |  |
| [`mne-tools/mne-testing-data`: `testdata_ctf_mc.hc`](https://github.com/mne-tools/mne-testing-data/blob/cc40c2964c81c83b9af317fc3cf9a9634a05f095/CTF/testdata_ctf_mc.ds/testdata_ctf_mc.hc) | human: Unknown | HolyC |  |
| [`mozilla-services/screenshots`: `server.ftl`](https://github.com/mozilla-services/screenshots/blob/33eeff19d361e2a12f5474cf9a0d5ef409082c99/locales/zh-TW/server.ftl) | human: Unknown | Fluent |  |
| [`mozilla/blurts-server`: `bento.ftl`](https://github.com/mozilla/blurts-server/blob/39de9a07442a3c0e4240c22066fcc3cf817f2104/locales/zh-TW/bento.ftl) | human: Unknown | Fluent |  |
| [`nilp0inter/dotfiles`: `.i3`](https://github.com/nilp0inter/dotfiles/blob/2af9e96e19cd23e5d22d316704ba1bd8adfd9254/.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`onnx/onnx`: `output_0.pb`](https://github.com/onnx/onnx/blob/e108da9a9a9916880ca7d1a0cfff96637921212c/onnx/backend/test/data/node/test_slice/test_data_set_0/output_0.pb) | human: Unknown | PureBasic |  |
| [`oscfdezdz/Dotfiles-WIP`: `config.i3`](https://github.com/oscfdezdz/Dotfiles-WIP/blob/fbcb800a377c3c7ae85bec90f038e54cc500a44b/config.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`pengdev/home-networking`: `traffic_long.xpl`](https://github.com/pengdev/home-networking/blob/9dd139aed3ee3bd5caa0c3dec1218d88e104bf88/data/build/tmp/oneMoreTime_dlna_android_bw_700k/traffic_long.xpl) | human: Unknown | XProc |  |
| [`plotnick/clweb`: `test.clw`](https://github.com/plotnick/clweb/blob/4c736b4c8b4c0afbdd939eefbcb986c16c24c1e3/test.clw) | human: Unknown | Clarion |  |
| [`potassco/asprilo-encodings`: `quantities.clp`](https://github.com/potassco/asprilo-encodings/blob/0bd438fe8b25df11bd33926490729b817f1550d2/abc/quantities.clp) | human: Unknown | CLIPS |  |
| [`potatoHVAC/dotfiles`: `.i3`](https://github.com/potatoHVAC/dotfiles/blob/4c0b80418453bbcd9679762d088b371ee1c4723b/.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`probe-scope/Probe-Scope-PCB`: `Probe-Scope v1.0.G4`](https://github.com/probe-scope/Probe-Scope-PCB/blob/f5a3add610575115ad71bc815e6f6577f5d11894/Project%20Outputs%20for%20Probe-Scope%20v1.0/Probe-Scope%20v1.0.G4) | human: Unknown | ANTLR |  |
| [`procaconsul/sociologic`: `narrow-passage-one-person.las`](https://github.com/procaconsul/sociologic/blob/dcec734783f92ad04d118376131f162fddf55670/experiments/narrow-passage-one-person.las) | human: Unknown | Lasso |  |
| [`proofcert/fpccheck`: `pair.mod`](https://github.com/proofcert/fpccheck/blob/6de59990bfb7762f869e0d3a4c5d0fad453a86c2/fpc/lprolog/pair.mod) | human: Unknown | AMPL |  |
| [`quillford/config`: `.i3`](https://github.com/quillford/config/blob/9e482da34d4dc835d34305db773e82752cc26925/.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`ramonsaraiva/cfg`: `.i3`](https://github.com/ramonsaraiva/cfg/blob/41a14360bb7bda3f1689a90ea2c109059796116f/.i3) | human: Unknown | Modula-3 | i3 configuration |
| [`rehnd/MoS2-band-structure`: `MoS2-2H.bands.dat.gnu`](https://github.com/rehnd/MoS2-band-structure/blob/56a90b1384cccb63bc4cfe6747077c38cc3526cc/espresso/electron/4-plotbands/MoS2-2H.bands.dat.gnu) | human: Unknown | Gnuplot |  |
| [`robinhouston/wdg-html-validator`: `xml1n.dcl`](https://github.com/robinhouston/wdg-html-validator/blob/9694889302d12e6bb1a78f65e145af4d2ccd3ec8/root/usr/local/share/sgml/declaration/xml1n.dcl) | human: Unknown | Clean |  |
| [`rolledback/regionadjacency`: `test.boo`](https://github.com/rolledback/regionadjacency/blob/42e3bbdb38ea3f194ad11b0e2d89b5fde3b63336/test.boo) | human: Unknown | Boo |  |
| [`rricharz/Tek4010`: `msdusa.plt`](https://github.com/rricharz/Tek4010/blob/0efbc2e783efe4f88375f07af6172c3cb437045b/pltfiles/More_pltfiles/msdusa.plt) | human: Unknown | Gnuplot |  |
| [`sbsdev/sbs-braille-tables`: `sbs-de-g2-name.mod`](https://github.com/sbsdev/sbs-braille-tables/blob/ad8b4d3b898d228cce81d72ac2e8038d931db747/tables/sbs-de-g2-name.mod) | human: Unknown | AMPL | SBS modules |
| [`sciguy14/Eagle-Tutorial-Series`: `blinky.pro`](https://github.com/sciguy14/Eagle-Tutorial-Series/blob/2683c0f2b7aaacc525c2180436f6940eb952dfe4/02%20Layout/blinky.pro) | human: Unknown | Prolog | EAGLE AutoRouter Statistics |
| [`sctb/lumen`: `main.l`](https://github.com/sctb/lumen/blob/2d272b2cc78b23b0b23a69a08fc625240e545ebc/main.l) | human: Unknown | Common Lisp |  |
| [`sebschub/FontPro`: `MnSymbolF5.pl`](https://github.com/sebschub/FontPro/blob/165b4a7d11ad34b64d7457ee6d51af4875e0bf14/fontinst/MyriadPro/MnSymbolF5.pl) | human: Unknown | Prolog | TeX Font Metrics (pl - Property List format) |
| [`shanhuio/smlos`: `join.g`](https://github.com/shanhuio/smlos/blob/9f7de31d7ba9a97dad1ecb54583c8d3702663165/sync/join.g) | human: Unknown | GAP | Toy language (G / Small VM), subset of Go. |
| [`shihyu/MyTool`: `ctviews.e`](https://github.com/shihyu/MyTool/blob/541771d9bc10d32a54baa48eb62992b4bcb9353f/mybin/se/macros/ctviews.e) | human: Unknown | Eiffel |  |
| [`shsdev/arc2warc-hadoop`: `2-metadata-1.arc`](https://github.com/shsdev/arc2warc-hadoop/blob/96e624592deaa1cf355a27772032bd0206dc6ce5/src/test/resources/arc-dedup/2-metadata-1.arc) | human: Unknown | Arc |  |
| [`sredmond/stanford-karel`: `StoneMasonSmall.w`](https://github.com/sredmond/stanford-karel/blob/0cd5e64cbc9cd5930bddaacaf8bc0b175fd3e26c/worlds/StoneMasonSmall.w) | human: Unknown | OpenEdge ABL |  |
| [`sriniiyer/nl2sql`: `geo_train.nl`](https://github.com/sriniiyer/nl2sql/blob/652edf4814dce2cddf1661e05a18602161c65e8f/data/geo/geo_train.nl) | human: Unknown | NewLisp |  |
| [`stipub/stixfonts`: `stix2-mathrm.pl`](https://github.com/stipub/stixfonts/blob/73d7c426993abacea44288aded4e81b568d57ed1/archive/STIXv2.0.0/Type1/fonts/source/public/stix2/stix2-mathrm.pl) | human: Unknown | Prolog | TeX Font Metrics (pl - Property List format) |
| [`superpomme/DoomZ`: `TEXTURES.aug`](https://github.com/superpomme/DoomZ/blob/b9308844cdc80351e6ed6b30dfa4d002fdb17e18/TEXTURES.aug) | human: Unknown | Augeas |  |
| [`takano32/selfevaluck`: `hello.ms`](https://github.com/takano32/selfevaluck/blob/db001a1dfc5ac041c85d13d8467b0ff02cbd9d41/hello.ms) | human: Unknown | MAXScript |  |
| [`texmacs/texmacs`: `man-structure.zh.tm`](https://github.com/texmacs/texmacs/blob/106de6e055fd0b3054e7a1246fef42535680ec51/TeXmacs/doc/main/text/man-structure.zh.tm) | human: Unknown | Tcl |  |
| [`ti-cortex-m4/devices`: `CONTRO2.TU`](https://github.com/ti-cortex-m4/devices/blob/01001b79425c7d6e4d99d4429d674ac5b5a60f61/nzif/программы/WTune/repiter/CONTRO2.TU) | human: Unknown | Turing |  |
| [`tommybennett/slickc`: `make_func.e`](https://github.com/tommybennett/slickc/blob/e53694b21f15d0695b2b6e1e37dd2a0931936bb8/cpp/make_func.e) | human: Unknown | Eiffel |  |
| [`trajanrx/dotfiles`: `.i3`](https://github.com/trajanrx/dotfiles/blob/c22ad938f2243dfd8eff26a93fcde03d51fa1789/.i3) | human: Unknown | Modula-3 |  |
| [`tushar-97/Convex-Hull`: `hull_5.ch`](https://github.com/tushar-97/Convex-Hull/blob/2cbb53ed5b687793b593d7c0a959ece86896a15b/Test%20Cases/Test%20Case%205/hull_5.ch) | human: Unknown | xBase |  |
| [`unforswearing/applescript`: `AppWatcher.applescript`](https://github.com/unforswearing/applescript/blob/7ecc04d1b2fc1192259e1f1f65abc9c59b02cb4a/Application%20Services/AppWatcher.applescript) | human: Unknown | AppleScript |  |
| [`utoh/pygmy-forth`: `ed.scr`](https://github.com/utoh/pygmy-forth/blob/21d555e1592ed266f3156d2a62e75a553cdbf9bf/ed.scr) | vote: Unknown | — |  |
| [`wasplang/std`: `strings.w`](https://github.com/wasplang/std/blob/44a681aaca4c1f30287c9a41ecda48ccfff47ac2/strings.w) | human: Unknown | CWeb |  |
| [`wensir365/pkugcm`: `N032_surf_0134.sra`](https://github.com/wensir365/pkugcm/blob/aee29d92cbba29d1f2f222ecdb8e5cbde0789651/ppp/N032_surf_0134.sra) | human: Unknown | PowerBuilder |  |
| [`wolfgangj/okami`: `log.ok`](https://github.com/wolfgangj/okami/blob/7b44509d36d1e61be05935f1e02e22286e79d929/lib/log.ok) | vote: Unknown | — |  |
| [`yanghaoqin/1-16_RF_PWR_DIV`: `bestsave.w`](https://github.com/yanghaoqin/1-16_RF_PWR_DIV/blob/5316812a7f701bc9aec36a8e75d7528a98e09efb/bestsave.w) | human: Unknown | CWeb |  |
| [`yuechenglei/VastChallenge2006`: `1101163520244.txt.p.NE`](https://github.com/yuechenglei/VastChallenge2006/blob/2e0c9c175e18133f470fc5ae4943f68a1ce933bf/static/news-processed/1101163520244.txt.p.NE) | human: Unknown | Nearley | Text annotated with name entity tags |

</details>
