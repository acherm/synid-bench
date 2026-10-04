"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [lexer name]}.
Default: guess_lexer_for_filename(name, text) (file name, then content among the matching lexers);
--content-only: guess_lexer(text). No lexer → no answer. --labels: every lexer name."""
import json
import sys
from pathlib import Path

from pygments.lexers import get_all_lexers, guess_lexer, guess_lexer_for_filename
from pygments.util import ClassNotFound

if "--labels" in sys.argv:
    print(json.dumps(sorted({lx[0] for lx in get_all_lexers()})))
    sys.exit()
content_only = "--content-only" in sys.argv
for d in sorted(Path("/in").iterdir()):
    f = next(d.iterdir())
    text = f.read_bytes().decode("utf-8", "replace")
    try:
        lexer = guess_lexer(text) if content_only else guess_lexer_for_filename(f.name, text)
        labels = [lexer.name]
    except ClassNotFound:
        labels = []
    print(json.dumps({"dir": d.name, "labels": labels}))
