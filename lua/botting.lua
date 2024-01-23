
local stopTimer = false
function timer(time)
   tempTimer(1.0, function() 
      if stopTimer == true then
         return
      end

      
   end)
end



----------------------------
-- Target rooms for quests
----------------------------
-- forest watch
-- MUST use battle abilites here
local fwStart = 7694

-- Genji
local genjiStart = 10129

-- Manara room with roots from outside
local first = 47880

-- level 4
local ebra = 19164
local roots4 = 18869

-- level 3
local roots3 = 16490
local iofio = 99
-- level 2
local roots2 = 18316
local thriel = 18157

-- level 1
local roots1 = 16349
local bissa = 17736


---------------------------
-- Great rock
--------------------------
local greatStart = 4230
local lotash = 276
local kasha = 4254
local bearnath = 4252

local finishedHunt =  function()
  cecho("<yellow>Scripts/TravelRooms/Bashing finished\n")
end

registerNamedEventHandler("Mine", "finishedHunt", "mmapper arrived", finishedHunt)


--local currentRoom = mmp.currentroom


