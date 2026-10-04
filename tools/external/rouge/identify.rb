# /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [lexer title]} from
# Rouge::Lexer.guess(filename:, source:) (file name globs, modeline, shebang/source detection, disambiguation rules);
# --content-only: Rouge::Lexer.guess(source:). Several lexers left (Rouge::Guesser::Ambiguous) → all of them
# (undecided); the PlainText lexer (no clue) → "Text". Bytes are read as UTF-8, invalid sequences replaced.
# --labels: every lexer title (PlainText as "Text").
require 'rouge'
require 'json'

def label(lexer)
  lexer == Rouge::Lexers::PlainText ? 'Text' : lexer.title
end

if ARGV.include?('--labels')
  puts JSON.generate(Rouge::Lexer.all.map { |l| label(l) }.uniq.sort)
  exit
end
content_only = ARGV.include?('--content-only')
Dir.children('/in').sort.each do |d|
  dir = File.join('/in', d)
  path = File.join(dir, Dir.children(dir).first)
  source = File.binread(path).force_encoding(Encoding::UTF_8).scrub
  labels = begin
    [label(content_only ? Rouge::Lexer.guess(source: source) : Rouge::Lexer.guess(filename: path, source: source))]
  rescue Rouge::Guesser::Ambiguous => e
    e.alternatives.map { |l| label(l) }
  rescue StandardError
    []
  end
  puts JSON.generate({ dir: d, labels: labels })
end
