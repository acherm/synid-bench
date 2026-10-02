"""Root causes of Synid's failures on bench-m (used by tools/failures.py).

Each cause names the mechanism inside Synid, the evidence that pins it down,
how it was verified, and the fix it suggests. `diagnose()` assigns a failing
case to one cause from the case's features and the answers of the stored runs
(Synid with one strategy off, the port of Linguist's `.m` rules).

Established on Synid 9bc1c32 and 48c3c45 (`assessment/m-9bc1c32.md`, and the
name-mismatch analysis of 2026-10-02).
"""

from __future__ import annotations

import re

CAUSES = {
    "wolfram-rule-name": {
        "title": "The Wolfram rule for `.m` never fires (name mismatch)",
        "mechanism": (
            "Synid's Hyperpolyglot heuristics for `.m` include Linguist's Wolfram rule — `(\\*` and a line ending "
            "in `*)` — under the name \"Mathematica\". The strategy keeps only rules whose names are among the "
            "current candidates, compared as strings (`candidates.contains(syntax)`, "
            "`hyply_heuristics_strategy/mod.rs`); the candidate is named by its canonical name, \"Wolfram "
            "Language\", so the rule is filtered out even when the file matches it. The file stays undecided and "
            "the Pygments-heuristics strategy, which has no Wolfram heuristic, answers `Text`."),
        "evidence": "every file has `(*` and a line ending in `*)`; the port of Linguist's `.m` rules says Wolfram",
        "verified": ("renaming the rule's syntax to \"Wolfram Language\" in a local build of 48c3c45 makes all "
                     "four files right, with no other change (2026-10-02)"),
        "fix": ("compare syntax ids (`syntax::index`) rather than names when filtering rules — or use canonical "
                "names in the heuristics table. Four other rules have the same problem: `.v` \"Coq\", `.sql` "
                "\"PLpgSQL\", `.ch` \"xBase\", `.q` \"q\""),
    },
    "pygments-text-default": {
        "title": "`Text` by default when no heuristic matches (comment-free MATLAB/Octave)",
        "mechanism": (
            "Linguist's MATLAB rule needs a line starting with `%`, and Synid's Pygments heuristic for MATLAB a line "
            "starting with `%`, `!` or `function`; a comment-free script has none, so the file reaches the "
            "Pygments-heuristics strategy undecided. That strategy always returns one syntax — the best-scoring "
            "candidate, starting from `(0.0, \"Text\")` (`pygment_strategy/mod.rs`, `guess_syntax`) — so `Text` "
            "becomes final and the Bayesian classifier, which comes after it, never runs."),
        "evidence": ("no line starting with `%`, `!` or `function`; Synid without pygmentsheuristics lets the "
                     "classifier run, which answers MATLAB on 9 of the 10 files (`L9p3.m`: M)"),
        "verified": "Synid 48c3c45 with `[strategies] disable = [\"pygmentsheuristics\"]` (entry in the leaderboard)",
        "fix": ("when no candidate's heuristic scores, return the candidates unchanged instead of `Text` (or run "
                "the classifier first)"),
    },
    "out-of-candidates": {
        "title": "The language is not among Synid's candidates for `.m`",
        "mechanism": (
            "The extension strategy proposes the languages Linguist lists for `.m` (Objective-C, MATLAB, Mercury, "
            "M, Wolfram Language, Limbo, MUF, Mason); every later strategy can only narrow that list. Magma, which "
            "also uses `.m`, is not in it, nor is C saved under a `.m` name. `Text` is then the least-wrong answer "
            "(the classifier, if it ran, would pick a wrong candidate)."),
        "evidence": "expected language not in the candidate list",
        "verified": ("the candidate list Synid returns for `.m` when no content strategy decides — on the "
                     "non-UTF-8 files: Limbo, M, MATLAB, MUF, Mason, Mercury, Objective-C, Wolfram Language"),
        "fix": "add Magma to the `.m` candidates (as Linguist could); misnamed files are out of reach by design",
    },
    "non-utf8": {
        "title": "Content that is not valid UTF-8 → undecided",
        "mechanism": (
            "`synid file` reads files as strict UTF-8; when decoding fails, every content strategy is skipped and "
            "the extension's eight candidates are returned unchanged."),
        "evidence": ("bytes that are not UTF-8 (Latin-1 or GBK comments); decoded leniently, the file matches "
                     "Linguist's MATLAB rule (the port says MATLAB)"),
        "verified": "every strategy configuration returns the eight candidates on these files",
        "fix": "decode leniently (replacement characters), as Synid's S3 and Web-API content hosts already do",
    },
    "comment-free-objc": {
        "title": "Objective-C without comments eliminated by the comment strategy",
        "mechanism": (
            "Up to 9bc1c32 the comment strategy ran before the Hyperpolyglot heuristics; on Objective-C with no "
            "`//` or `/*` (here a decompiled file) it eliminated Objective-C, and the file ended as `Text`."),
        "evidence": "no `//` or `/*`; Synid without the comment strategy answers Objective-C",
        "verified": "fixed in 48c3c45, which runs the Hyperpolyglot heuristics (`@implementation`) first",
        "fix": "fixed (strategy order changed in 48c3c45)",
    },
}


def diagnose(case: dict, text: str, answers: dict) -> str | None:
    """Cause id for a failing case. `answers`: run label → answer (list or None)."""
    tags = set(filter(None, case.get("tags", "").split(";")))
    exp = case["expected"]
    if "non-utf8" in tags:
        return "non-utf8"
    if "out-of-candidates" in tags:
        return "out-of-candidates"
    if exp == "mathematica-wolfram" and re.search(r"\(\*", text) and re.search(r"(?m)\*\)\r?$", text):
        return "wolfram-rule-name"
    if exp == "matlab-family" and "comment-free-matlab" in tags:
        return "pygments-text-default"
    if exp == "objective-c" and "comment-free-objc" in tags:
        return "comment-free-objc"
    return None
