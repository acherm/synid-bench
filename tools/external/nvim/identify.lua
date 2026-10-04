-- /in/<case>/<file> → one JSON line per case: {"dir": case, "labels": [filetype]} from
-- vim.filetype.match({ filename = path, contents = lines }) (file name, extension, path patterns, then the content
-- where the name is ambiguous or unknown); no filetype → no answer. --content-only:
-- vim.filetype.match({ contents = lines }), as for a buffer without a name (its content checks: shebang, first
-- lines). Not done: the editor's "conf" fallback for unknown files whose first lines start with "#", and modelines.
-- Lines are the file split on "\n", a trailing "\r" removed. --labels: every filetype Neovim knows,
-- getcompletion('', 'filetype') (those with runtime files) and vim.filetype._get_known_filetypes().
local args = _G.arg or {}
local function has(flag)
  for _, a in ipairs(args) do
    if a == flag then return true end
  end
  return false
end

if has('--labels') then
  local set = {}
  for _, ft in ipairs(vim.fn.getcompletion('', 'filetype')) do set[ft] = true end
  for ft in pairs(vim.filetype._get_known_filetypes()) do set[ft] = true end
  local out = vim.tbl_keys(set)
  table.sort(out)
  io.stdout:write(vim.json.encode(out), '\n')
  return
end

local content_only = has('--content-only')
local dirs = {}
for name in vim.fs.dir('/in') do table.insert(dirs, name) end
table.sort(dirs)
for _, d in ipairs(dirs) do
  local labels = {}
  local file = vim.fs.dir('/in/' .. d)()
  if file then
    local path = '/in/' .. d .. '/' .. file
    local f = io.open(path, 'rb')
    local text = f and f:read('*a') or ''
    if f then f:close() end
    local lines = vim.split(text, '\n', { plain = true })
    if lines[#lines] == '' then table.remove(lines) end
    for i, l in ipairs(lines) do lines[i] = l:gsub('\r$', '') end
    local ok, ft = pcall(vim.filetype.match, content_only and { contents = lines } or { filename = path, contents = lines })
    if ok and ft then labels = { ft } end
  end
  io.stdout:write('{"dir": ', vim.json.encode(d), ', "labels": ', #labels > 0 and vim.json.encode(labels) or '[]', '}\n')
end
