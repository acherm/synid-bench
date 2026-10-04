// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} from gengo's
// Language::pick (shebang, file name, path pattern, extension, then heuristics and priority), given the file
// name and the bytes, as gengo's directory analysis does (read limit 1 MiB, its default); a file with a NUL
// byte in that limit is binary to gengo and gets no answer. --labels: the languages of its languages.yaml.
use gengo_language::Language;
use std::fs;
use std::path::{Path, PathBuf};

const READ_LIMIT: usize = 1 << 20;

fn detect(d: &Path) -> Option<&'static str> {
    let f = fs::read_dir(d).ok()?.next()?.ok()?.path();
    let contents = fs::read(&f).ok()?;
    if contents.iter().take(READ_LIMIT).any(|&b| b == 0) {
        return None;
    }
    Language::pick(f.file_name()?, &contents, READ_LIMIT).map(|l| l.name())
}

fn main() {
    if std::env::args().any(|a| a == "--labels") {
        let names: Vec<String> = fs::read_to_string("/labels.txt").unwrap().lines().map(String::from).collect();
        println!("{}", serde_json::json!(names));
        return;
    }
    let mut dirs: Vec<PathBuf> = fs::read_dir("/in").unwrap().map(|e| e.unwrap().path()).collect();
    dirs.sort();
    // the heuristics' regexes are slow on some files: one thread per CPU, answers printed in order
    let n = std::thread::available_parallelism().map_or(1, |n| n.get());
    let chunk = dirs.len().div_ceil(n).max(1);
    let langs: Vec<Option<&str>> = std::thread::scope(|s| {
        let handles: Vec<_> = dirs.chunks(chunk)
            .map(|c| s.spawn(move || c.iter().map(|d| detect(d)).collect::<Vec<_>>()))
            .collect();
        handles.into_iter().flat_map(|h| h.join().unwrap()).collect()
    });
    for (d, lang) in dirs.iter().zip(langs) {
        let name = d.file_name().unwrap().to_string_lossy().to_string();
        println!("{}", serde_json::json!({"dir": name, "labels": lang.into_iter().collect::<Vec<_>>()}));
    }
}
