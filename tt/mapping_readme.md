C #roomcount

V #versionnumber

C<colorname> colorvalue

F #mapflags

G #globalvnum

I #lastroomvnum

L {legendgroupname} {legendname} {legendsymbol}

T {terrainname} {terrainflags} {terrainsymbol}

R {#roomvnum}{#roomflags}{roomcolor}{roomname}{roomsymbol}{roomdesc}{roomarea}{roomnote}{roomterrain}{roomdata}{#roomweight}{roomid}
E {#exitvnum}{exitname}{exitcommand}{#exitdir}{#exitflags}{exitdata}{#exitweight}{exitcolor}{#exitdelay}



#nop Coords
#nop first number is the Map Id
#nop then horizton
#nop then vertical
#nop #VARIABLE {gmcp[room][info]}
#nop {
#nop     {area} {Ashtan}
#nop     {coords} {49,6,-9,0}

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


#VARIABLE {gmcp[room][info]}
{
    {area} {Ashtan}
    {coords} {49,6,-9,0}
    {details} {}
    {environment} {Urban}
    {exits}
    {
        {sw} {438}
    }
    {map} {www.achaea.com/irex/maps/clientmap.php?map=49&building=0&level=0 22 39}
    {name} {Parade of Zarathustra east of a statue}
    {num} {448}
}

