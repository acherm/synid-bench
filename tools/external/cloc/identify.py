"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} from
`cloc --by-file --json`; a file cloc does not recognise gets no answer. --labels: `cloc --show-lang`."""
import json
import subprocess
import sys
from pathlib import Path

if "--labels" in sys.argv:
    out = subprocess.run(["cloc", "--show-lang"], capture_output=True, text=True).stdout
    langs = sorted({line.rsplit("(", 1)[0].strip() for line in out.splitlines() if "(" in line})
    print(json.dumps(langs))
    sys.exit()
res = subprocess.run(["cloc", "--by-file", "--json", "--skip-uniqueness", "--quiet", "--no-autogen",
                      "--follow-links", "/in"], capture_output=True, text=True)
by_path = {}
try:
    for k, v in json.loads(res.stdout or "{}").items():
        if isinstance(v, dict) and "language" in v:
            by_path[str(Path(k))] = v["language"]
except json.JSONDecodeError:
    pass
for d in sorted(Path("/in").iterdir()):
    files = list(d.iterdir())
    lang = by_path.get(str(files[0])) if files else None
    print(json.dumps({"dir": d.name, "labels": [lang] if lang else []}))
