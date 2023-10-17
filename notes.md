Ratting script
----------------

Print GMCP to console in Mudlet

Find exits
- gmcp:  GMCP.Room.Info.exits
- ignore: up, down, in, and out
    - There is a door in the way, to the <>.


-- targets
local targets = {'^a.\*rat$'}

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



