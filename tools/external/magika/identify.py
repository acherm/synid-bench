"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [content type]} (Magika reads
the bytes only; the label is its content-type label, e.g. "python", "txt"). --labels: every output label."""
import json
import sys
from pathlib import Path

from magika import Magika

m = Magika()
if "--labels" in sys.argv:
    print(json.dumps(sorted(str(x) for x in m.get_output_content_types())))
    sys.exit()
dirs = sorted(Path("/in").iterdir())
paths = [next(d.iterdir()) for d in dirs]
for d, res in zip(dirs, m.identify_paths(paths)):
    label = str(res.output.label) if res.ok else None
    print(json.dumps({"dir": d.name, "labels": [label] if label else []}))
