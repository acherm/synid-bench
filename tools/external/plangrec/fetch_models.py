"""Build time: download PLangRec's trained models (the URLs of common/model.py at 3fb01dd), check their sha256,
unzip them into /model (BRNN/ = the line model, ensemble-meta-model.h5 = the meta-model)."""
import hashlib
import io
import urllib.request
import zipfile

BASE = "https://reflection.uniovi.es/bigcode/download/2024/plangrec/"
MODELS = [("BRNN.zip", "c02626870a8ca8d4b22846ca40f21e2c8b3e09435c791228e38239a70a9ed966", "/model/BRNN"),
          ("ensemble-meta-model.zip", "89e2d8d9a83c81d6b6632f392f515fbe61932a06f040ae1eb55af20db7860fc0", "/model")]
for name, sha256, dest in MODELS:
    data = urllib.request.urlopen(BASE + name).read()
    if hashlib.sha256(data).hexdigest() != sha256:
        raise SystemExit(f"{name}: sha256 differs from the pinned one")
    z = zipfile.ZipFile(io.BytesIO(data))
    z.extractall(dest, members=[m for m in z.namelist() if not m.startswith("__MACOSX")])
