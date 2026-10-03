# Partial runs

Answers of runs still in progress, saved so they are not lost (the leaderboard only reads complete entries).

- `kev-linguist.jsonl` — Kev-4B Q8_0, run locally with llama.cpp (`/v1/systemone`, commit a4cb4c6), choosing among
  Linguist's 804 languages from the content only (same protocol as Jev), files asked in a fixed random order: 1907 of
  3,404 files at 2026-10-03 07:37. On those files: Kev-4B 61.9 % [59.5, 64.1], Jev 82.1 % (content only),
  Jev 88.7 % (with file name), Synid 48c3c45 76.4 % (with file name). Resume with the command in
  `../reproduce.sh`; answers already given are kept.
