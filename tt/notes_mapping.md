C #roomcount

V #versionnumber

C<colorname> colorvalue

F #mapflags

G #globalvnum

I #lastroomvnum

L {legendgroupname} {legendname} {legendsymbol}

T {terrainname} {terrainflags} {terrainsymbol}

R {#roomvnum}{#roomflags}{roomcolor}{roomname}{roomsymbol}{roomdesc}{roomarea}{roomnote}{roomterrain}{roomdata}{#roomweight}{roomid}
E
    #vnum
    name
    cmd
    #dir -- seems like a bitflag for possible directions from this exit.
    #flags -- get_exit_color, colors exit based on HIDE,INVI,AVOID,BLOCK
    data -- can see it with #map exit, with no args.
    #3f weight
    color
    #2f delay


-- in mapper.c
fprintf(file, "\nR {%d}{%d}{%s}{%s}{%s}{%s}{%s}{%s}{%s}{%s}{%.3f}{%s}\n",
fprintf(file, "E {%d}{%s}{%s}{%d}{%d}{%s}{%.3f}{%s}{%.2f}\n",



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


regex to match on the following
Just match on the upper case?

{%* [A-Z]%*},
find the vnum, #map find {roomname}{%2?},
then subsitutue in roomnumber.
Add in distance too?
Save found shops to visit each?

2000gp     a group of 100 pieces of irid moss Golden Dragon's Lair


