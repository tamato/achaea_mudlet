#!/usr/bin/lua

--https://wiki.mudlet.org/w/Manual:Advanced_Lua#Regex_in_Lua
local rex = require("rex_pcre")

local rage = "Rage: 253"

amount = rex.match(rage, [[\d+]])
amount = tonumber(amount)
print(amount)

-- Break them up into indidivuals
local brAbilities = "You can use another Battlerage ability again. Available abilities: Harry, Temperance, Ruin, Fluctuate"
for a in rex.split(brAbilities, ",") do
   local ab = rex.match(a, " (\\w+$)")
   print(ab)
end

occult = 'occultist'
battleRageAbilities = battleRageAbilities or {}
battleRageAbilities[occult] = battleRageAbilities[occult] or {}

target = 0
alt_target = 0

local occRage = battleRageAbilities[occult]
occRage['harry'] = {
   ready = false,
   cmd = 'harry ' .. target,
   rage = 14,
   priority = 99,
}

occRage['temperance'] = {
   ready = false,
   cmd = 'temper ' .. alt_target,
   rage = 32,
   priority = 99,
}

occRage['ruin'] = {
   ready = false,
   cmd = 'ruin ' .. target,
   rage = 17,
   priority = 99,
}

occRage['chaosgate'] = {
   ready = false,
   cmd = 'chaosgate ' .. target,
   rage = 36,
   priority = 99,
}

occRage['fluctuate'] = {
   ready = false,
   cmd = 'fluctuate ' .. target,
   rage = 25,
   priority = 99,
}

occRage['stagnate'] = {
   ready = false,
   cmd = 'stagnate ' .. target,
   rage = 24,
   priority = 99,
}


botter = botter or {}
botter.events = {}
botter.events.cleanup = { "cleanup", function() print("Hi!") end }

for _,id in pairs(botter.events) do
   if type(id) == "function" then
      print("ID: " .. "func")
   end
end
print(botter)
