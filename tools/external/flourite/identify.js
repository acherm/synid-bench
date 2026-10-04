// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} (flourite on the first 10,000
// characters, with its default options; "Unknown" is no answer). --labels: its 25 languages, plus "Bash" (a
// `#!/bin/bash` line); a `#!/usr/bin/env <x>` line makes it answer <x> capitalised, which no list can hold.
// flourite is a snippet detector and its patterns backtrack badly on long lines: on a whole file it can run for
// hours (a minified jQuery: over 20 min, not finished); on 10,000 characters it takes seconds at most.
const fs = require('fs');
const path = require('path');
const flourite = require('flourite');

const SAMPLE = 10000;

if (process.argv.includes('--labels')) {
  const langs = Object.keys(flourite('x').statistics).filter((l) => l !== 'Unknown');
  console.log(JSON.stringify([...langs, 'Bash'].sort()));
  process.exit(0);
}
for (const d of fs.readdirSync('/in').sort()) {
  const f = fs.readdirSync(path.join('/in', d))[0];
  const text = fs.readFileSync(path.join('/in', d, f)).toString('utf8').slice(0, SAMPLE);
  let labels = [];
  try {
    const lang = flourite(text).language;
    if (lang && lang !== 'Unknown') labels = [lang];
  } catch (e) {
    // no answer
  }
  process.stdout.write(JSON.stringify({ dir: d, labels }) + '\n');
}
