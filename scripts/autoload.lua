MAXENTRIES = 5000

local options = require 'mp.options'
fnx_prev = 0
fnx_next = 0
o = {
    disabled = false
}
options.read_options(o)

function Set (t)
    local set = {}
    for _, v in pairs(t) do set[v] = true end
    return set
end

EXTENSIONS = Set {
    'mkv', 'avi', 'mp4', 'ogv', 'webm', 'rmvb', 'flv', 'wmv', 'mpeg', 'mpg', 'm4v', '3gp',
    'mp3', 'wav', 'ogv', 'flac', 'm4a', 'wma',
}

mputils = require 'mp.utils'

function add_files_at(index, files)
    index = index - 1
    local oldcount = mp.get_property_number("playlist-count", 1)
    for i = 1, #files do
        mp.commandv("loadfile", files[i], "append")
        mp.commandv("playlist-move", oldcount + i - 1, index + i - 1)
    end
end

function get_extension(path)
    match = string.match(path, "%.([^%.]+)$" )
    if match == nil then
        return "nomatch"
    else
        return match
    end
end

table.filter = function(t, iter)
    for i = #t, 1, -1 do
        if not iter(t[i]) then
            table.remove(t, i)
        end
    end
end

function splitbynum(s)
    local result = {}
    for x, y in (s or ""):gmatch("(%d*)(%D*)") do
        if x ~= "" then table.insert(result, tonumber(x)) end
        if y ~= "" then table.insert(result, y) end
    end
    return result
end

function clean_key(k)
    k = (' '..k..' '):gsub("%s+", " "):sub(2, -2):lower()
    return splitbynum(k)
end

function alnumcomp(x, y)
    local xt, yt = clean_key(x), clean_key(y)
    for i = 1, math.min(#xt, #yt) do
        local xe, ye = xt[i], yt[i]
        if type(xe) == "string" then ye = tostring(ye)
        elseif type(ye) == "string" then xe = tostring(xe) end
        if xe ~= ye then return xe < ye end
    end
    return #xt < #yt
end

function find_and_add_entries()
    local path = mp.get_property("path", "")
    local dir, filename = mputils.split_path(path)
    if o.disabled or #dir == 0 then
        return
    end
    local pl_count = mp.get_property_number("playlist-count", 1)
    if (pl_count > 1 and autoload == nil) or
       (pl_count == 1 and EXTENSIONS[string.lower(get_extension(filename))] == nil) then
        return
    else
        autoload = true
    end

    local files = mputils.readdir(dir, "files")
    if files == nil then
        return
    end
    table.filter(files, function (v, k)
        if string.match(v, "^%.") then
            return false
        end
        local ext = get_extension(v)
        if ext == nil then
            return false
        end
        return EXTENSIONS[string.lower(ext)]
    end)
    table.sort(files, alnumcomp)

    if dir == "." then
        dir = ""
    end

    local pl = mp.get_property_native("playlist", {})
    local pl_current = mp.get_property_number("playlist-pos", 0) + 1
    local current
    for i = 1, #files do
        if files[i] == filename then
            current = i
            break
        end
    end
    if current == nil then
        return
    end

    local append = {[-1] = {}, [1] = {}}
    for direction = -1, 1, 2 do
        for i = 1, MAXENTRIES do
            local file = files[current + i * direction]
            local pl_e = pl[pl_current + i * direction]
            if file == nil or file[1] == "." then
                break
            end

            local filepath = dir .. file
            if pl_e then
                if pl_e.filename == filepath then
                    break
                end
            end

            if direction == -1 then
                if pl_current == 1 then
                    fnx_prev = fnx_prev + 1
                    table.insert(append[-1], 1, filepath)
                end
            else
		fnx_next = fnx_next + 1
                table.insert(append[1], filepath)
            end
        end
    end

    mp.msg.info("Total files prev: " .. fnx_prev)
    mp.msg.info("Total files next: " .. fnx_next)
    add_files_at(pl_current + 1, append[1])
    add_files_at(pl_current, append[-1])
end

mp.register_event("start-file", find_and_add_entries)
