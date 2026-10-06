#!/usr/bin/env python3
"""A two-stage identifier: candidates first, then Jev decides → a leaderboard entry.

    python3 tools/jev_cascade.py benchmarks/bench-m --limit 3            # a check
    python3 tools/jev_cascade.py benchmarks/bench-linguist --workers 8
    python3 tools/jev_cascade.py benchmarks/bench-linguist --content-only

1. Candidates. The file's name (when PL-ultimate-llm knows it whole) or its extensions — every
   suffix, `.antlers.html` as well as `.html` — give
   the languages PL-ultimate-llm associates with it (tools/data/pl_candidates.json:
   every source's claims, minus those the encyclopedia deprecated, plus the languages the
   extension studies observed in Software Heritage — Magma, MUMPS, C under .m).
2. Jev chooses among those candidates, plus `Text` (plain text or data, no programming
   language) and "none of these".
3. Fallback. When there is no candidate, or Jev answers "none of these", Jev chooses among
   the 1,289 languages PL-ultimate-llm knows an extension for or Linguist lists — a knockout
   (6 groups of ~215 with "none of these", then a final), as a question takes at most 255
   options.

The file name is shown to Jev unless --content-only (the candidates still come from it).
Same question wording and 16,000-character truncation as tools/jev_linguist.py; answers
are named by their Linguist name when they have one. Needs OPENROUTER_API_KEY (or
--endpoint for a local decision server). Resumable (<bench>/.work/jev/).
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
import sys  # noqa: E402

sys.path.insert(0, str(HERE))
from jev_linguist import INSTRUCTIONS, MAX_CHARS, MODEL, NONE, URL, api_key, decide  # noqa: E402

TEXT = "Text"
MAX_OPTIONS = 255
SEED = 20261003


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bench", type=Path)
    ap.add_argument("--content-only", action="store_true", help="do not show the file name to Jev")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--endpoint", default=URL)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--name", default="Jev 1.13")
    ap.add_argument("--label", default="jev-cascade")
    ap.add_argument("--candidates", type=Path, default=HERE / "data" / "pl_candidates.json",
                    help="the candidate mapping (tools/export_pl_candidates.py)")
    a = ap.parse_args()
    bench = a.bench.resolve()
    with (bench / "cases.csv").open(encoding="utf-8") as f:
        cases = list(csv.DictReader(line for line in f if not line.startswith("#")))
    version = (bench / "cases.csv").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").split(" —")[0]
    data = json.loads(a.candidates.read_text(encoding="utf-8"))
    langs = data["languages"]
    remote = a.endpoint.startswith("https://openrouter.ai")
    key = api_key() if remote else None

    def desc(pid: str) -> str:
        lg = langs[pid]
        parts = [f"{lg['name']} — {lg['type'] or 'programming language'}"]
        if lg["aliases"]:
            parts.append("also: " + ", ".join(lg["aliases"][:4]))
        if lg["extensions"]:
            parts.append("files: " + " ".join(lg["extensions"][:5]))
        return "; ".join(parts)

    def options(pids) -> dict[str, tuple[str, str]]:
        """label shown to Jev → (pl_id, description); labels unique."""
        out = {}
        for pid in pids:
            name = langs[pid]["name"]
            label = name if name not in out else f"{name} ({pid})"
            out[label] = (pid, desc(pid))
        return out

    def ask(state: str, opts: dict[str, tuple[str, str]], extra: dict[str, str]) -> tuple[str | None, dict, float]:
        crit = {lab: d for lab, (_, d) in opts.items()} | extra
        out = decide(state, {"language": {"type": "choice", "instructions": INSTRUCTIONS, "criteria": crit}},
                     key, a.endpoint, a.model)
        ans = (out.get("answers") or {}).get("language") or {}
        return ans.get("choice"), ans.get("probabilities") or {}, float((out.get("usage") or {}).get("cost") or 0)

    def candidates(c: dict) -> list[str]:
        """By whole file name, else by every extension suffix (`.antlers.html` and `.html`), longest first."""
        if c["filename"] in data["by_filename"]:
            return data["by_filename"][c["filename"]]
        parts = c["filename"].lower().split(".")[1:]
        out: list[str] = []
        for i in range(len(parts)):
            for pid in data["by_ext"].get("." + ".".join(parts[i:]), []):
                if pid not in out:
                    out.append(pid)
        return out

    fallback = data["fallback"]
    random.Random(SEED).shuffle(fallback)
    n_groups = -(-len(fallback) // (MAX_OPTIONS - 1))
    groups = [fallback[i::n_groups] for i in range(n_groups)]
    none_extra = {NONE: "none of the options above fits this file"}
    text_extra = {TEXT: "plain text, prose or data — not written in any of the languages above"}

    label = a.label + ("-content-only" if a.content_only else "")
    cache = bench / ".work" / "jev" / f"{label}.jsonl"
    cache.parent.mkdir(parents=True, exist_ok=True)
    done = {}
    if cache.exists() and not a.limit:
        for line in cache.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            done[r["case_id"]] = r
    lock = threading.Lock()

    def one(c: dict) -> dict:
        raw = (bench / "files" / c["sha1_git"]).read_bytes().decode("utf-8", "replace")
        trunc = len(raw) > MAX_CHARS
        body = (f"File content{' [truncated to the first %d characters]' % MAX_CHARS if trunc else ''}:\n"
                f"```\n{raw[:MAX_CHARS]}\n```")
        state = body if a.content_only else f"Filename: {c['filename']}\n\n" + body
        cand = candidates(c)
        cost, stage, answer, probs = 0.0, "", None, {}
        cand_probs, group_tops, final_probs = {}, [], {}
        if cand:
            opts = options(cand)
            ch, cand_probs, co = ask(state, opts, text_extra | none_extra)
            probs = cand_probs
            cost += co
            if ch == TEXT:
                stage, answer = "candidates", TEXT
            elif ch in opts:
                stage, answer = "candidates", langs[opts[ch][0]]["name"]
        if answer is None:  # no candidate, or none of them
            winners = []
            win_probs = []
            for g in groups:
                opts = options(g)
                ch, gp, co = ask(state, opts, none_extra)
                cost += co
                group_tops.append(sorted(gp.items(), key=lambda kv: -kv[1])[:5])
                if ch in opts:
                    winners.append(opts[ch][0])
                    win_probs.append(gp)
            stage = "fallback"
            if len(winners) > 1:
                opts = options(winners)
                ch, final_probs, co = ask(state, opts, text_extra)
                probs = final_probs
                cost += co
                answer = TEXT if ch == TEXT else langs[opts[ch][0]]["name"] if ch in opts else None
            elif winners:
                answer = langs[winners[0]]["name"]
                probs = win_probs[0]  # the deciding question was the winner's group
            else:
                probs = {}
        t5 = lambda pr: sorted(pr.items(), key=lambda kv: -kv[1])[:5]  # noqa: E731
        # top5: the question that decided the answer (runs before 2026-10-04: the candidates' question even when
        # the fallback decided); then every question's own
        r = {"case_id": c["case_id"], "n_candidates": len(cand), "stage": stage, "answer": answer,
             "top5": t5(probs), "candidates_top5": t5(cand_probs), "groups_top5": group_tops,
             "final_top5": t5(final_probs), "cost": cost, "truncated": trunc}
        if not a.limit:
            with lock, cache.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        return r

    todo = cases[: a.limit] if a.limit else cases
    pending = [c for c in todo if c["case_id"] not in done]
    print(f"{len(todo)} cases, {len(done)} cached, {len(pending)} to ask", flush=True)
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=max(1, a.workers)) as ex:
        for n, r in enumerate(ex.map(one, pending), 1):
            done[r["case_id"]] = r
            if n % 200 == 0 or a.limit:
                print(f"{n}/{len(pending)} {time.time() - t0:.0f}s ${sum(x['cost'] for x in done.values()):.3f} "
                      f"{r['stage']}: {r['answer']}", flush=True)
    rows = [done[c["case_id"]] for c in todo]
    cost = sum(r["cost"] for r in rows)
    stages = {s: sum(1 for r in rows if r["stage"] == s) for s in ("candidates", "fallback")}
    print(f"total ${cost:.4f}; decided among candidates: {stages['candidates']}, fallback: {stages['fallback']}")
    if a.limit:
        return 0
    meta = {"label": label, "kind": "cascade", "benchmark": version,
            "name": f"{a.name}, PL-ultimate-llm candidates then fallback"
                    + (f" over {len(fallback):,} languages" if data.get("fallback_name") else "")
                    + (", content only" if a.content_only else ", with file name"),
            "version": f"{a.model}, " + ("OpenRouter Decisions API" if remote else f"local ({a.endpoint})")
                       + f"; candidates: {data['source']}",
            "about": ("two stages: the languages PL-ultimate-llm associates with the file's extension (claims by "
                      "Linguist, Pygments, Wikidata, Wikipedia, plus the languages the extension studies observed), "
                      "among which Jev chooses — or `Text`, or none; then, if none, a knockout over the "
                      + (data.get("fallback_name") or f"{len(fallback):,} languages with a known extension")
                      + " (tools/jev_cascade.py)"
                      + (". The file name is not shown to Jev" if a.content_only else "")
                      + f". {len(rows)} files: {stages['candidates']} decided among candidates, {stages['fallback']} "
                        f"by the fallback; ${cost:.4f}"),
            "date": time.strftime("%Y-%m-%d")}
    (bench / "entries" / "raw").mkdir(parents=True, exist_ok=True)
    with (bench / "entries" / "raw" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (bench / "entries" / f"{label}.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"meta": meta}) + "\n")
        for r in rows:
            f.write(json.dumps({"case_id": r["case_id"], "answer": [r["answer"]] if r["answer"] else None}) + "\n")
    print(f"→ {bench / 'entries' / (label + '.jsonl')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
