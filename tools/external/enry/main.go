// /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} (enry.GetLanguage:
// file name and content; "" when unknown). --labels: every language enry can name.
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sort"

	"github.com/go-enry/go-enry/v2"
	"github.com/go-enry/go-enry/v2/data"
)

func main() {
	if len(os.Args) > 1 && os.Args[1] == "--labels" {
		names := []string{}
		for _, info := range data.LanguageInfoByID {
			names = append(names, info.Name)
		}
		sort.Strings(names)
		b, _ := json.Marshal(names)
		fmt.Println(string(b))
		return
	}
	dirs, _ := os.ReadDir("/in")
	for _, d := range dirs {
		files, _ := os.ReadDir(filepath.Join("/in", d.Name()))
		labels := []string{}
		if len(files) > 0 {
			name := files[0].Name()
			content, err := os.ReadFile(filepath.Join("/in", d.Name(), name))
			if err == nil {
				if lang := enry.GetLanguage(name, content); lang != "" {
					labels = append(labels, lang)
				}
			}
		}
		b, _ := json.Marshal(map[string]interface{}{"dir": d.Name(), "labels": labels})
		fmt.Println(string(b))
	}
}
