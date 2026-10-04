"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} from
`ctags --guess-language-eagerly --print-language`, which names the parser ctags would pick for each file
(file name, extension, and — eagerly, even when the name gives no hint — shebang and Emacs/Vim modelines;
content selectors for a few ambiguous extensions) without parsing it; `NONE` → no answer.
--labels: `ctags --list-languages`."""
import json
import subprocess
import sys
from pathlib import Path

CTAGS = "/opt/ctags/bin/ctags"
if "--labels" in sys.argv:
    out = subprocess.run([CTAGS, "--list-languages"], capture_output=True, text=True).stdout
    print(json.dumps(sorted({line.split()[0] for line in out.splitlines() if line.strip()})))
    sys.exit()
cases = sorted(Path("/in").iterdir())
files = [next(d.iterdir()) for d in cases]
res = subprocess.run([CTAGS, "--guess-language-eagerly", "--print-language", "-L", "-"], input="\n".join(map(str, files)) + "\n",
                     capture_output=True, text=True)
lang = {}
for line in res.stdout.splitlines():
    path, _, guess = line.rpartition(": ")
    lang[path] = guess.strip()
for d, f in zip(cases, files):
    g = lang.get(str(f), "NONE")
    print(json.dumps({"dir": d.name, "labels": [] if g in ("NONE", "") else [g]}))
