Ratting script
----------------
Variables needed
- autoBashing
- target
- listOfTargets
- listOfApproveTargets

rat enters room
- append to list of targets
- if no target, set it to the first entry of list

rat leaves room
- does it match the target
    - clear target
    - check list, set first entry

Print GMCP to console in Mudlet, gives full list.
lua gmpc

Find exits
- gmcp:  GMCP.Room.Info.exits
- ignore: up, down, in, and out
    - There is a door in the way, to the <>.


-- list of exits
local prohibited_exits = {'up', 'down', 'in', 'out'}
prohibited_rooms = prohibited_rooms or {} -- add id for Gates of Ashtan

for dir,id in pairs(GMCP.Room.Info.exits) do
    if dir in prohibited_exits then
        if id in prohibited_rooms then
            continue
        continue
    end

    -- check balances
    -- have it runing the whole time
    enableTrigger("CheckBlocked") 
        -- possibly adds id to prohibited_rooms
        -- restarts this script on failure
    break
end

send(dir)



