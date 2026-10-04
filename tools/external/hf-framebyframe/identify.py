"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [label]}. A Hugging Face text-classification
model (baked into the image at /model) reads the text only: the bytes decoded as UTF-8 (invalid bytes replaced), cut
to the first MAX_CHARS characters when the model card says so, then to the first MAX_TOKENS tokens (the model's
maximum input). The label is the top one (argmax of the logits, no threshold), so every file gets an answer.
Float32 on CPU, 4 threads; files are batched by token length (padding is masked). --labels: the model's label set.
Same script in every tools/external/hf-*/ directory; the Dockerfile sets the model and the environment."""
import json
import os
import sys
from pathlib import Path

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MAX_TOKENS = int(os.environ["MAX_TOKENS"])
MAX_CHARS = int(os.environ.get("MAX_CHARS") or 0)
BATCH = 16
THREADS = 4  # fixed, so that several runs side by side do not oversubscribe the machine

torch.set_num_threads(THREADS)
torch.set_num_interop_threads(1)

attn = {"attn_implementation": os.environ["ATTN"]} if os.environ.get("ATTN") else {}
tok = AutoTokenizer.from_pretrained("/model")
model = AutoModelForSequenceClassification.from_pretrained("/model", dtype=torch.float32, **attn).eval()
id2label = model.config.id2label
if "--labels" in sys.argv:
    print(json.dumps(sorted(set(id2label.values()))))
    sys.exit()
dirs = sorted(Path("/in").iterdir())
ids = []  # one file at a time: memory stays bounded by the largest file
for d in dirs:
    text = next(d.iterdir()).read_bytes().decode("utf-8", "replace")
    ids.append(tok(text[:MAX_CHARS] if MAX_CHARS else text, truncation=True, max_length=MAX_TOKENS)["input_ids"])
order = sorted(range(len(dirs)), key=lambda i: (len(ids[i]), i))  # similar lengths together: little padding
labels = [None] * len(dirs)
with torch.inference_mode():
    for k in range(0, len(order), BATCH):
        idx = order[k:k + BATCH]
        batch = tok.pad({"input_ids": [ids[i] for i in idx]}, return_tensors="pt")
        for i, j in zip(idx, model(**batch).logits.argmax(-1).tolist()):
            labels[i] = id2label[j]
for d, label in zip(dirs, labels):
    print(json.dumps({"dir": d.name, "labels": [label]}))
