"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [content type]} (Magika reads
the bytes only; the label is its content-type label, e.g. "python", "txt"). --labels: every output label.
Magika 0.5's API: the label is `output.ct_label`, there is no `ok` (an unreadable file gets a label such as
"permission_error": no answer) and no list of output labels (the model's labels after its overwrite map,
plus the labels it gives without the model)."""
import json
import sys
from pathlib import Path

from magika import Magika
from magika.content_types import ContentType

ERRORS = {ContentType.FILE_DOES_NOT_EXIST, ContentType.PERMISSION_ERROR}

m = Magika()
if "--labels" in sys.argv:
    labels = {m._model_output_overwrite_map.get(x, x) for x in m._target_labels_space_np}
    labels |= {ContentType.GENERIC_TEXT, ContentType.UNKNOWN, ContentType.EMPTY, ContentType.DIRECTORY,
               ContentType.SYMLINK}
    print(json.dumps(sorted(str(x) for x in labels)))
    sys.exit()
dirs = sorted(Path("/in").iterdir())
paths = [next(d.iterdir()) for d in dirs]
for d, res in zip(dirs, m.identify_paths(paths)):
    label = str(res.output.ct_label) if res.output.ct_label not in ERRORS else None
    print(json.dumps({"dir": d.name, "labels": [label] if label else []}))
