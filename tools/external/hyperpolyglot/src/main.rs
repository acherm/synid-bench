// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} (hyperpolyglot::detect:
// file name, extension, shebang, heuristics, classifier). --labels: the languages of its languages.yml.
use std::fs;

fn main() {
    if std::env::args().any(|a| a == "--labels") {
        let names: Vec<String> = fs::read_to_string("/labels.txt").unwrap().lines().map(String::from).collect();
        println!("{}", serde_json::json!(names));
        return;
    }
    let mut dirs: Vec<_> = fs::read_dir("/in").unwrap().map(|e| e.unwrap().path()).collect();
    dirs.sort();
    for d in dirs {
        let file = fs::read_dir(&d).unwrap().next().map(|e| e.unwrap().path());
        let labels: Vec<String> = match file.map(|f| hyperpolyglot::detect(&f)) {
            Some(Ok(Some(det))) => vec![det.language().to_string()],
            _ => vec![],
        };
        let name = d.file_name().unwrap().to_string_lossy().to_string();
        println!("{}", serde_json::json!({"dir": name, "labels": labels}));
    }
}
