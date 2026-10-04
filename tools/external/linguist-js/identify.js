// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} (linguist-js analyseRawContent over
// all files at once: attributes, modeline, filename, shebang, extension, then Linguist's heuristics; the first
// candidate when the heuristics do not decide — it has no classifier). Offline: the Linguist data files bundled
// in the package, never fetched. Child languages (not their group), vendored files kept. --labels: every
// language in the bundled languages.yml.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import yaml from 'js-yaml';
import linguist from 'linguist-js';

if (process.argv.includes('--labels')) {
  const pkg = path.dirname(createRequire(import.meta.url).resolve('linguist-js/package.json'));
  const langs = yaml.load(fs.readFileSync(path.join(pkg, 'ext', 'languages.yml'), 'utf8'));
  console.log(JSON.stringify(Object.keys(langs).sort()));
  process.exit(0);
}
const files = {};
const dirOf = {};
for (const d of fs.readdirSync('/in').sort()) {
  const f = path.join('/in', d, fs.readdirSync(path.join('/in', d))[0]);
  files[f] = fs.readFileSync(f).toString('utf8');
  dirOf[f] = d;
}
const opts = { offline: true, childLanguages: true, keepVendored: true, calculateLines: false };
const out = (await linguist.analyseRawContent(files, opts)).files.results;
for (const [f, d] of Object.entries(dirOf)) {
  const lang = out[f];
  process.stdout.write(JSON.stringify({ dir: d, labels: lang ? [lang] : [] }) + '\n');
}
