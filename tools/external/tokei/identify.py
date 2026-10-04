"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} from
`tokei --output json`, whose keys are tokei's display names (as `tokei --languages` prints them); a file tokei
does not recognise gets no answer. --labels: every display name of its languages.json (`name`, else the key)."""
import json
import subprocess
import sys
from pathlib import Path

if "--labels" in sys.argv:
    langs = json.loads(Path("/languages.json").read_text())["languages"]
    print(json.dumps(sorted({v.get("name", k) for k, v in langs.items()})))
    sys.exit()
# --hidden and --no-ignore: count dot files, and do not let a case's .gitignore hide anything
res = subprocess.run(["tokei", "--output", "json", "--hidden", "--no-ignore", "/in"], capture_output=True, text=True)
by_path = {}
try:
    for lang, v in json.loads(res.stdout or "{}").items():
        # top-level reports only: "children" holds the code blocks embedded in another language's file
        for r in (v.get("reports") or []) if isinstance(v, dict) else []:
            by_path[str(Path(r["name"]))] = lang
except json.JSONDecodeError:
    pass
for d in sorted(Path("/in").iterdir()):
    files = list(d.iterdir())
    lang = by_path.get(str(files[0])) if files else None
    print(json.dumps({"dir": d.name, "labels": [lang] if lang else []}))
