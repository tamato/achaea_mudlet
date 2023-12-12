#!/usr/bin/lua

--https://wiki.mudlet.org/w/Manual:Advanced_Lua#Regex_in_Lua

local num = "2"
if type(num) == "string" then print("just a string") end
if type(num+0) == "number" then print("it is now a number") end
