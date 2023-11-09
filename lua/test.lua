#!/usr/bin/lua
function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end


local tbl = {}
tbl = {"asdf", "dkddk", [6]={9} }

print("Print : ", dump(tbl))


function tbl:print(msg, m2) 
   print("hi " .. msg .. " " .. m2)
end
tbl:print("stuff", "other")


print("2nd")
tbl.print(tbl, "mmmm", "other")

