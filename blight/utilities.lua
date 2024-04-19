-- Common use items

local handle = io.popen('cat ~/.config/blight/settings')
local result = handle:read("*a")
handle:close()

print('-------------')
local settings = assert(load(result))()
print('pw: ' .. settings.pw)
print('root: ' .. settings.rootdir)

-- Load device settings
-- local ROOTDIR ='/home/tamausb/repos/achaea_mudlet/blight'
-- SETTINGS = require "settings"
-- print(SETTINGS.PASSWD)

