"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} from
`scc --by-file --format json`; a file scc does not recognise (or takes for binary) gets no answer.
--labels: `scc --languages`."""
import json
import subprocess
import sys
from pathlib import Path

if "--labels" in sys.argv:
    out = subprocess.run(["scc", "--languages"], capture_output=True, text=True).stdout
    print(json.dumps(sorted({line.rsplit("(", 1)[0].strip() for line in out.splitlines() if "(" in line})))
    sys.exit()
# no ignore files, and count .gitignore-like files; scc always skips lock files (package-lock.json, Cargo.lock, …)
res = subprocess.run(["scc", "--by-file", "--format", "json", "--no-ignore", "--no-scc-ignore", "--no-gitignore",
                      "--no-gitmodule", "--count-ignore", "--no-cocomo", "--no-complexity", "/in"],
                     capture_output=True, text=True)
by_path = {}
try:
    for v in json.loads(res.stdout or "[]"):
        for f in v.get("Files") or []:
            by_path[str(Path(f["Location"]))] = f["Language"]
except json.JSONDecodeError:
    pass
for d in sorted(Path("/in").iterdir()):
    files = list(d.iterdir())
    lang = by_path.get(str(files[0])) if files else None
    print(json.dumps({"dir": d.name, "labels": [lang] if lang else []}))
