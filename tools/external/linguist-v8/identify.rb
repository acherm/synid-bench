# /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [language]} (Linguist.detect: modeline,
# filename, shebang, extension, XML, man page, heuristics, classifier; nil for binary or empty files).
# --labels: every language Linguist can name.
require 'linguist'
require 'json'
if ARGV.include?('--labels')
  puts JSON.generate(Linguist::Language.all.map(&:name).sort)
  exit
end
Dir.children('/in').sort.each do |d|
  dir = File.join('/in', d)
  path = File.join(dir, Dir.children(dir).first)
  lang = begin
    Linguist.detect(Linguist::FileBlob.new(path))
  rescue StandardError
    nil
  end
  puts JSON.generate({ dir: d, labels: lang ? [lang.name] : [] })
end
