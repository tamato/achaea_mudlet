#!/usr/bin/lua

-- retrieve the content of a URL
local http = require("socket.http")
local body, code = http.request("http://pbs.twimg.com/media/CCROQ8vUEAEgFke.jpg")
if not body then error(code) end

-- save the content to a file
local f = assert(io.open('luatest.jpg', 'wb')) -- open in "binary" mode
f:write(body)
f:close()
