"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]}. PLangRec (Rodriguez-Prieto, Pato
and Ortin, Future Generation Computer Systems 166, 2025) reads the text only (UTF-8, invalid bytes replaced): a
character-level bidirectional LSTM gives the language probabilities of each line (the stripped line, its first 40
characters; printable ASCII, anything else one out-of-vocabulary code); a stacking meta-model (an MLP over a 100-bin
histogram of the line probabilities of each of the 21 languages) gives the file's. As `predict` in PLangRec's
common/model.py (3fb01dd): when a single line has 10 characters or more, that line alone (line model); when none,
the first line; otherwise the meta-model over every line of the file, empty ones included. The answer is the top
language (no threshold). Same computation, batched over all files; identical lines are predicted once.
--labels: the 21 languages."""
import json
import os
import sys
from pathlib import Path

import numpy as np

LANGUAGES = ["Assembly", "C", "C++", "C#", "CSS", "Go", "HTML", "Java", "JavaScript", "Kotlin", "Matlab", "Perl",
             "PHP", "Python", "R", "Ruby", "Scala", "SQL", "Swift", "TypeScript", "Unix Shell"]  # common/languages.py
if "--labels" in sys.argv:
    print(json.dumps(sorted(LANGUAGES)))
    sys.exit()

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
import tensorflow as tf  # noqa: E402

tf.config.threading.set_intra_op_parallelism_threads(4)  # fixed, so that several runs side by side do not
tf.config.threading.set_inter_op_parallelism_threads(1)  # oversubscribe the machine


def encode(line: str) -> bytes:
    """common/model.py `_parse_line` on a stripped line: ASCII 32..126 → 2..96, other characters → 1 (OOV),
    padded with 0 to 40."""
    return bytes(ord(c) - 30 if 32 <= ord(c) < 127 else 1 for c in line[:40]).ljust(40, b"\0")


dirs = sorted(Path("/in").iterdir())
plans = []  # per file: (meta-model?, row of each line)
rows: dict[bytes, int] = {}
for d in dirs:
    text = next(d.iterdir()).read_bytes().decode("utf-8", "replace")
    lines = [line.strip() for line in text.split("\n")]
    long = [line for line in lines if len(line) >= 10]
    meta = len(long) > 1
    plans.append((meta, [rows.setdefault(encode(line), len(rows)) for line in (lines if meta else long or lines[:1])]))

model = tf.keras.models.load_model("/model/BRNN", compile=False)
meta_model = tf.keras.models.load_model("/model/ensemble-meta-model.h5", compile=False)
X = np.frombuffer(b"".join(rows), dtype=np.uint8).reshape(-1, 40).astype(np.int32)
P = model.predict(X, batch_size=256, verbose=0)  # small batches: less memory (the VM may be short of it)
best = [0] * len(dirs)
features = {}
for k, (meta, idx) in enumerate(plans):
    p = P[idx]
    if not meta:
        best[k] = int(p[0].argmax())
        continue
    hist = np.stack([np.histogram(p[:, i], bins=100, range=(0, 1))[0] for i in range(len(LANGUAGES))])
    features[k] = (hist / (len(idx) * len(LANGUAGES))).reshape(-1)
if features:
    out = meta_model.predict(np.array(list(features.values())), batch_size=256, verbose=0)
    for k, o in zip(features, out):
        best[k] = int(o.argmax())
for d, j in zip(dirs, best):
    print(json.dumps({"dir": d.name, "labels": [LANGUAGES[j]]}))
