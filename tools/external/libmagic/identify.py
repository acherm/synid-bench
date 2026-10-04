"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [label], "description": ..., "mime": ...}
from file(1) (libmagic; reads the bytes only). The label is `file -b`'s description up to its first comma
("Python script, ASCII text executable" → "Python script"); "description" keeps it whole and "mime" is
`file -b --mime-type`. --labels: the descriptions of libmagic's text tests, of its entries with a text/* MIME type and of those
that name a source/script/program (`file -l`), cut the same way (and without the final " text"/" executable"
that file drops on a text file), plus the labels of file's own checks (encodings, JSON, CSV) — an
approximation of what it can answer on text files."""
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

JOBS = os.cpu_count() or 1


def label(desc: str) -> str:
    return desc.split(",")[0].strip()


def file_b(paths: list[str], *opts: str) -> list[str]:
    """`file -b` over paths (names read from a list file): one output line per path, in order."""
    with tempfile.NamedTemporaryFile("w", suffix=".lst", delete=False) as f:
        f.write("\n".join(paths) + "\n")
    out = subprocess.run(["file", "-b", *opts, "-f", f.name], capture_output=True, text=True,
                         errors="replace").stdout.splitlines()
    if len(out) != len(paths):
        raise SystemExit(f"file printed {len(out)} lines for {len(paths)} files")
    return out


def file_all(paths: list[str], *opts: str) -> list[str]:
    """file_b in parallel over chunks of the paths (file is slow: thousands of magic tests per file)."""
    chunks = [paths[i::JOBS] for i in range(JOBS)]
    with ThreadPoolExecutor(JOBS) as ex:
        outs = list(ex.map(lambda c: file_b(c, *opts) if c else [], chunks))
    res = [""] * len(paths)
    for i, out in enumerate(outs):
        res[i::JOBS] = out
    return res


if "--labels" in sys.argv:
    out = subprocess.run(["file", "-l"], capture_output=True, text=True, errors="replace").stdout
    labels, text_set = set(), False
    for line in out.splitlines():
        if line.endswith("patterns:"):
            text_set = line.startswith("Text")
        m = re.match(r"Strength = +\d+@\d+: (.*) \[([^\]]*)\]$", line)
        if not m or "%" in m.group(1):
            continue
        desc, mime = m.groups()
        if text_set or mime.startswith("text/") or re.search(r"\b(source|script|program)\b", desc, re.I):
            # on a text file, file drops a final " text" / " executable" and adds the encoding after a comma
            lab = re.sub(r"( text)?( executable)?$", "", label(desc))
            if lab:
                labels.add(lab)
    # file's own checks (not in the magic database): encodings, JSON, CSV, and the no-answer labels
    labels |= {"ASCII text", "Unicode text", "ISO-8859 text", "Non-ISO extended-ASCII text", "EBCDIC text",
               "International EBCDIC text", "JSON text data", "CSV ASCII text", "CSV Unicode text", "empty", "data",
               "very short file (no magic)"}
    print(json.dumps(sorted(labels)))
    sys.exit()
dirs = sorted(Path("/in").iterdir())
paths = [str(next(d.iterdir())) for d in dirs]
descs = file_all(paths)
mimes = file_all(paths, "--mime-type")
for d, desc, mime in zip(dirs, descs, mimes):
    lab = label(desc)
    print(json.dumps({"dir": d.name, "labels": [lab] if lab else [], "description": desc, "mime": mime}))
