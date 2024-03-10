

#VARIABLE {gmcp[room][info]}
{
    {area} {Ashtan}
    {coords} {49,4,-11,0}
    {details} {}
    {environment} {Urban}
    {exits}
    {
        {ne} {448}
    }
    {map} {www.achaea.com/irex/maps/clientmap.php?map=49&building=0&level=0 20 41}
    {name} {Parade of Zarathustra before a statue}
    {num} {438}
}


Don't use the events. Check if finished my self.

order of operations

path walk is called
internal map is updated
eventually onRoomInfo is called
delay calls path walk again

WHEN we reach the end a new destination is found
calls path walk, updates internal map before onRoomInfo has a chance to catchup.
During this time onRoomInfo is called
which tries to call path walk a second time
    Now internal map is out of sync to where we are


What should happen

Find destination
start traversing
in onRoomInfo, have we reach destination?
    yes - find next
    no - continue walking
