
local occultism = {
   "Ague",
   "Auraglance",
   "Warp",
   "Night",
   "Shroud",
   "Bodywarp",
   "Eldritchmists",
   "Mask",
   "Attend",
   "Enervate",
   "Encipher",
   "Quicken",
   "Astralvision",
   "Regress",
   "Shrivel",
   "Readaura",
   "Karma",
   "Heartstone",
   "Simulacrum",
   "Entities",
   "Timewarp",
   "Distortaura",
   "Pinchaura",
   "Impart",
   "Transcendence",
   "Unnamable",
   "Devolve",
   "Cleanseaura",
   "Tentacles",
   "Chaosrays",
   "Interlink",
   "Instill",
   "Whisperingmadness",
   "Devilmark",
   "Truename",
   "Astralform",
   "Enlighten",
   "Unravel",
   "Compel",
   "Transmogrify",
}

local abs = occultism
for k,i in ipairs(abs) do
   tempTimer(k, function()
      send("ab occultism " .. i)
      end)
end

local tarot = {
   "Inscribing",
   "Sun",
   "Cardpacks",
   "Emperor",
   "Magician",
   "Priestess",
   "Fool",
   "Chariot",
   "Hermit",
   "Empress",
   "Lovers",
   "Hangedman",
   "Tower",
   "Wheel",
   "Creator",
   "Justice",
   "Star",
   "Aeon",
   "Lust",
   "Universe",
   "Devil",
   "Moon",
   "Death",
   "Heretic",
   "Ruinate",
}

local abs = tarot
for k,i in ipairs(abs) do
   tempTimer(k, function()
      send("ab tarot " .. i)
      end)
end


local domination = {
   "Skyrax",
   "Rixil",
   "Eerion",
   "Arctar",
   "Scrag",
   "Pyradius",
   "Golgotha",
   "Dameron",
   "Palpatar",
   "Nin'kharsag",
   "Istria",
   "Marduk",
   "Primebond",
   "Nemesis",
   "Buul",
   "Cadmus",
   "Piridon",
   "Danaeus",
   "Xenophage",
   "Lycantha",
   "Tarotlink",
   "Hecate",
   "Covenant",
   "Glaaki",
}
local abs = domination
for k,i in ipairs(abs) do
   tempTimer(k, function()
      send("ab domination " .. i)
      end)
end

