// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language name]} (highlight.js auto-detection
// over every registered language that allows it; the best one's `name`; none when nothing beats plain text, i.e.
// relevance 0). --labels: the names of the languages auto-detection can return.
// highlightAuto(text) highlights the text with every language and keeps all the results before it sorts them:
// several GB on a large file. `best` keeps only each language's relevance and sorts them as highlightAuto does
// (same order, same comparison), so it makes the same choice. Every grammar runs over the whole text (~0.3 s a
// file), so the cases are shared among worker threads of this one process; the lines come out in case order.
const fs = require('fs');
const os = require('os');
const path = require('path');
const { Worker, isMainThread, parentPort } = require('worker_threads');
const hljs = require('highlight.js');

const WORKERS = Math.min(6, os.availableParallelism());
const AUTO = hljs.listLanguages().filter((id) => !hljs.getLanguage(id).disableAutodetect);

// highlight.js 11.12.0 (same in 11.9.0), src/highlight.js, highlightAuto: plain text first, then every language in the order
// registered; by relevance, a tie going to the base language over its superset (C++ over Arduino), else to the
// earlier one
function best(text) {
  const results = [{ relevance: 0 }]; // plain text
  for (const id of AUTO) {
    results.push({ language: id, relevance: hljs.highlight(text, { language: id, ignoreIllegals: false }).relevance });
  }
  results.sort((a, b) => {
    if (a.relevance !== b.relevance) return b.relevance - a.relevance;
    if (a.language && b.language) {
      if (hljs.getLanguage(a.language).supersetOf === b.language) return 1;
      if (hljs.getLanguage(b.language).supersetOf === a.language) return -1;
    }
    return 0;
  });
  return results[0].language && results[0].relevance > 0 ? results[0].language : null;
}

function identify(d) {
  const f = fs.readdirSync(path.join('/in', d))[0];
  const text = fs.readFileSync(path.join('/in', d, f)).toString('utf8');
  try {
    const id = best(text);
    return id ? [hljs.getLanguage(id).name] : [];
  } catch (e) {
    return [];
  }
}

if (!isMainThread) {
  parentPort.on('message', ({ i, d }) => parentPort.postMessage({ i, labels: identify(d) }));
} else if (process.argv.includes('--labels')) {
  console.log(JSON.stringify(AUTO.map((id) => hljs.getLanguage(id).name).sort()));
} else if (process.argv.includes('--check')) {
  // best(text) against hljs.highlightAuto(text) on every case (for testing; slow, memory-hungry)
  let diff = 0;
  for (const d of fs.readdirSync('/in').sort()) {
    const f = fs.readdirSync(path.join('/in', d))[0];
    const text = fs.readFileSync(path.join('/in', d, f)).toString('utf8');
    const r = hljs.highlightAuto(text);
    const a = r.language && r.relevance > 0 ? r.language : null;
    const b = best(text);
    if (a !== b) {
      diff++;
      console.log(JSON.stringify({ dir: d, highlightAuto: a, best: b }));
    }
  }
  console.log(JSON.stringify({ differences: diff }));
} else {
  const dirs = fs.readdirSync('/in').sort();
  const labels = new Array(dirs.length);
  let next = 0;
  let printed = 0;
  for (let w = 0; w < Math.min(WORKERS, dirs.length); w++) {
    const worker = new Worker(__filename);
    const feed = () => (next < dirs.length ? worker.postMessage({ i: next, d: dirs[next++] }) : worker.terminate());
    worker.on('message', ({ i, labels: l }) => {
      labels[i] = l;
      for (; printed < dirs.length && labels[printed]; printed++) {
        process.stdout.write(JSON.stringify({ dir: dirs[printed], labels: labels[printed] }) + '\n');
      }
      feed();
    });
    worker.on('error', (e) => {
      console.error(e);
      process.exit(1);
    });
    feed();
  }
}
