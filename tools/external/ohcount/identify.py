"""/in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} from `ohcount -d <file>`
(`<language>\t<path>`); a file ohcount does not recognise gets no answer. One ohcount process per file (one
thread per CPU): it crashes (SIGSEGV) on some files and loops on others (stopped after 60 s); those get no
answer. Labels are ohcount's language ids (`cpp`, `objective_c`, …). --labels: the LANG_* ids of the
package's src/languages.h."""
import json
import os
import subprocess
import sys
import threading
from pathlib import Path

if "--labels" in sys.argv:
    print(json.dumps(Path("/labels.txt").read_text().split()))
    sys.exit()


def detect(d: Path) -> list[str]:
    files = list(d.iterdir())
    if not files:
        return []
    try:
        p = subprocess.run(["ohcount", "-d", str(files[0])], capture_output=True, text=True, errors="replace",
                           timeout=60)
    except subprocess.TimeoutExpired:
        return []
    lang, _, path = p.stdout.partition("\n")[0].partition("\t")
    return [lang] if p.returncode == 0 and path and lang != "(null)" else []


dirs = sorted(Path("/in").iterdir())
labels: list[list[str]] = [[] for _ in dirs]
todo = iter(range(len(dirs)))
lock = threading.Lock()


def work() -> None:
    while True:
        with lock:
            i = next(todo, None)
        if i is None:
            return
        labels[i] = detect(dirs[i])


threads = [threading.Thread(target=work) for _ in range(os.cpu_count() or 1)]
for t in threads:
    t.start()
for t in threads:
    t.join()
for d, lab in zip(dirs, labels):
    print(json.dumps({"dir": d.name, "labels": lab}))
