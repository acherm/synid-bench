"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} (Guesslang reads the
text only; None when it does not take the text for source code). --labels: its supported languages."""
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
from guesslang import Guess  # noqa: E402

g = Guess()
if "--labels" in sys.argv:
    print(json.dumps(sorted(g.supported_languages)))
    sys.exit()
for d in sorted(Path("/in").iterdir()):
    text = next(d.iterdir()).read_bytes().decode("utf-8", "replace")
    try:
        name = g.language_name(text)
    except Exception:  # noqa: BLE001
        name = None
    print(json.dumps({"dir": d.name, "labels": [name] if name else []}), flush=True)
