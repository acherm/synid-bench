// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [model language id]} (@vscode/vscode-languagedetection,
// the Guesslang model in TensorFlow.js, used as VS Code uses it: the first 10,000 characters; no answer under 20
// characters (the package's minimum); VS Code's confidence rules — see `answer`). --labels: the model's 54 ids.
const fs = require('fs');
const path = require('path');
const { ModelOperations } = require('@vscode/vscode-languagedetection');

// microsoft/vscode, src/vs/workbench/services/languageDetection/browser/languageDetectionWebWorker.ts
// (formerly languageDetectionSimpleWorker.ts), last changed in 3d6c0d4: the sample is the first 10,000
// characters; confidences are adjusted (+0.05, +0.025, or -0.5 for languages that caused wrong guesses), and the
// top language is answered only if its raw and adjusted confidences are >= 0.2 and the candidates down to the
// first gap of >= 0.2 all have a confidence above 0.2.
const SAMPLE = 10000;
const EXPECTED = 0.2;
const BONUS = { js: 0.05, html: 0.05, json: 0.05, ts: 0.05, css: 0.05, py: 0.05, xml: 0.05, php: 0.05,
  cpp: 0.025, sh: 0.025, java: 0.025, cs: 0.025, c: 0.025,
  bat: -0.5, ini: -0.5, makefile: -0.5, sql: -0.5, csv: -0.5, toml: -0.5 };

const adjust = (r) => ({ languageId: r.languageId, confidence: r.confidence + (BONUS[r.languageId] || 0) });

// VS Code's detectLanguagesImpl: the language it would pick (the first one yielded), or null
function answer(results) {
  if (!results.length || results[0].confidence < EXPECTED) return null;
  const first = adjust(results[0]);
  if (first.confidence < EXPECTED) return null;
  let highest = first;
  for (const r of results.slice(1)) {
    const cur = adjust(r);
    if (highest.confidence - cur.confidence >= EXPECTED) return first.languageId;
    if (cur.confidence <= EXPECTED) return null;
    highest = cur;
  }
  return null;
}

(async () => {
  const model = new ModelOperations();
  if (process.argv.includes('--labels')) {
    const all = await model.runModel('x = 1\nprint(x)\n# a sample long enough for the model\n');
    console.log(JSON.stringify(all.map((r) => r.languageId).sort()));
    return;
  }
  for (const d of fs.readdirSync('/in').sort()) {
    const f = fs.readdirSync(path.join('/in', d))[0];
    const text = fs.readFileSync(path.join('/in', d, f)).toString('utf8').slice(0, SAMPLE);
    let labels = [];
    try {
      const id = answer(await model.runModel(text));
      if (id) labels = [id];
    } catch (e) {
      // no answer
    }
    process.stdout.write(JSON.stringify({ dir: d, labels }) + '\n');
  }
})();
