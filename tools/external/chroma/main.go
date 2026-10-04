// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [lexer name]}. As the chroma CLI picks a
// lexer for "autodetect" (cmd/chroma/main.go, selexer): lexers.Match(file name) — the highest-priority lexer among
// those whose file globs match — and when none matches, lexers.Analyse(content); no lexer → no answer.
// --content-only: lexers.Analyse(content). --labels: every lexer name.
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sort"

	"github.com/alecthomas/chroma/v2"
	"github.com/alecthomas/chroma/v2/lexers"
)

func main() {
	contentOnly := false
	for _, a := range os.Args[1:] {
		if a == "--labels" {
			names := []string{}
			for _, l := range lexers.GlobalLexerRegistry.Lexers {
				names = append(names, l.Config().Name)
			}
			sort.Strings(names)
			b, _ := json.Marshal(names)
			fmt.Println(string(b))
			return
		}
		contentOnly = contentOnly || a == "--content-only"
	}
	dirs, _ := os.ReadDir("/in")
	for _, d := range dirs {
		files, _ := os.ReadDir(filepath.Join("/in", d.Name()))
		labels := []string{}
		if len(files) > 0 {
			name := files[0].Name()
			content, err := os.ReadFile(filepath.Join("/in", d.Name(), name))
			if err == nil {
				var lexer chroma.Lexer
				if !contentOnly {
					lexer = lexers.Match(name)
				}
				if lexer == nil {
					lexer = lexers.Analyse(string(content))
				}
				if lexer != nil {
					labels = append(labels, lexer.Config().Name)
				}
			}
		}
		b, _ := json.Marshal(map[string]interface{}{"dir": d.Name(), "labels": labels})
		fmt.Println(string(b))
	}
}
