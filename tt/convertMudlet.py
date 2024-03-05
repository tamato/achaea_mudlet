#!/usr/bin/python

import json
import sys

def writeRoom(f, room):
    f.write(f'\n') 

    f.write(f'R ')
    for k,v in room.items():
        if k == 'exits':
            continue

        f.write(f'{{{v}}}') 
    f.write(f'\n') 

    for _,ext in room['exits'].items():
        f.write(f'E ')
        for _,v in ext.items():
            f.write(f'{{{v}}}') 
        f.write(f'\n') 

with open('map.json') as mapfile:
    parsed = json.load(mapfile)

voidrooms = []

nextRoomNum = 0
voidRoomStart = 0
allrooms = {}
for area in parsed['areas']:
    for room in area['rooms']:
        rid = room['id']

        if rid > nextRoomNum: nextRoomNum = rid

        if rid in allrooms: 
            print("Found Duplicate Room Num")
            sys.exit()

        allrooms[rid] = {'coords':room['coordinates'], 'areaid':area['id']} 


voidRoomStart = nextRoomNum
print(f'VoidStart {voidRoomStart}')

crowdcolors = parsed['customEnvColors']
colormapping = parsed['envToColorMapping']

globalRoomCnt = parsed['roomCount']
voidRoomOffset = 0

dirs = {
    "north": "n",
    "northeast": "ne",
    "east": "e",
    "southeast": "se",
    "south": "s",
    "southwest": "sw",
    "west": "w",
    "northwest": "nw",

    "in": "in",
    "out": "out",

    "up": "u",
    "down": "d",
}

#define MAP_EXIT_
dirBits = {
    'n':1,
    'e':2,
    's':4,
    'w':8,
    'u':16,
    'd':32,
    'in':64,
    'out':128,
}

# d is expected to be a 'rdircmd', which is room direction
def reverseDir(d):

    if d == 'n': return (4,'s')
    if d == 's': return (1,'n')
    if d == 'e': return (8,'w')
    if d == 'w': return (2,'e')

    if d == 'nw': return (4|2,'se')
    if d == 'ne': return (4|8,'sw')
    if d == 'sw': return (1|2,'ne')
    if d == 'se': return (1|8,'nw')

    if d == 'in':  return (128,'out')
    if d == 'out': return (64,'in')

    if d == 'u': return (32,'d')
    if d == 'd': return (16,'u')

def colors(mapping):
    cid = colormapping[str(mapping)]

    bit24 = [255,0,0]
    for color in crowdcolors:
        if color['id'] == cid:
            bit24 = color["color24RGB"]
            break;

    hex1 = hex(bit24[0])[2:]
    hex2 = hex(bit24[1])[2:]
    hex3 = hex(bit24[2])[2:]
    color = "<F"
    color += hex1.zfill(2)
    color += hex2.zfill(2)
    color += hex3.zfill(2)
    color += ">"
    return color

def getRoom(areaId,roomId):
    pass

def getArea(roomId):
    if roomId > voidRoomStart: return -1

    for area in parsed['areas']:
        for room in area['rooms']:
            if roomId == room['id']:
                return area['id']

def getExit(roomId,exitId):
    for area in parsed['areas']:
        for room in area['rooms']:
            if roomId == room['id']:
                for ext in room['exits']:
                    if exitId == ext['exitId']: 
                        return ext;
    #  print(f'room FOUND NOTHING {roomId}, {exitId}')
    return {}

def getVoidExit(roomId,exitId):
    for vroom in voidrooms:
        if roomId == vroom['vnum']:
            for vexit in vroom['exits']:
                if exitId == vexit['vnum']:
                    return vexit;

    print(f'FOUND NOTHING {roomId}, {exitId}')
    sys.exit(1)
    return {}

convertedRooms = {}
with open('world.map', 'w') as f:

    # prepand the header junk
    with open('mapheader') as header:
        for line in header:
            f.write(line)

    areaCount = 0
    for areaIdx,area in enumerate(parsed['areas']):
        areaname = area['name']
        roomCnt =  area['roomCount']
        if roomCnt == 0: continue
        
        areaid = area['id']
        if areaid < 0: continue

        print(f'Converting area {areaid}')
        #  print(f'RoomCnt {roomCnt}')

        for roomIdx, room in enumerate(area['rooms']):

            rid = room['id']
            rcoords = room['coordinates']
            feature = '';gameArea = ''
            if 'userData' in room:
                user = room['userData']

                if 'Game Area' in user: gameArea = user['Game Area']
                if 'feature-stronghold' in user: feature = 'h'
                if 'feature-ferry' in user: feature = 'F'
                if 'feature-news' in user: feature = 'N'
                if 'feature-arena' in user: feature = 'A'
                if 'feature-postoffice' in user: feature = 'O'
                if 'feature-commodityshop' in user: feature = 'C'
                if 'feature-grate' in user: feature = 'G'
                if 'feature-wilderness' in user: feature = 'W'
                if 'feature-harbour' in user: feature = 'H'
                if 'feature-shop' in user: feature = 'S'
                if 'feature-bank' in user: feature = '$'
                if 'feature-locksmith' in user: feature = 'L'

            rname = ''
            if 'name' in room:
                rname = room['name']

            envi = room['environment']
            color = colors(envi)
            coords = room["coordinates"]
            croom = {
                'vnum':rid,
                'flags':0, # hide all room, with 4102, ROOM_FLAG_HIDE
                'color':color,
                'name':rname,
                'sym':feature,
                'desc':'',
                'area':areaname,
                'note':'',
                'terain':'',
                'data':coords,
                'weight':1.00,
                'roomid':areaid,
                'exits':{},
            }
            convertedRooms[rid] = croom

            for exitIdx, portal in enumerate(room['exits']):
                exitid = portal['exitId']

                # check if this leads to the same area id
                direction = portal['name']

                if portal['name'] not in dirs:
                    #  print(f'Weird portal: {portal["name"]}')
                    direction = 'special'
                    cmd = 0
                    continue
                    #  sys.exit(1)
                else:
                    #TODO need to account for 
                    #   sendAll, send
                    #   script
                    #   push, pull, turn .*here
                    #       figure, idol, jar, vine, carving, callibius, opal, horn
                    #   embrace
                    #   enter
                    #   kneel
                    #   "say .*"
                    rdir = dirs[direction]
                    rdircmd = dirs[direction]

                simplelist = ['n','s','e','w','u','d','in','out']
                orlist = ['nw','ne','se','sw']
                dirbit = 0
                if rdircmd in simplelist: dirbit = dirBits[rdircmd]
                if rdircmd in orlist: dirbit = dirBits[rdircmd[0]] | dirBits[rdircmd[1]]

                if rdir != rdircmd: 
                    color = '<118>'
                    croom['color'] = color

                crexit = {
                    'vnum':exitid,
                    'dir': rdir,
                    'dircmd':rdircmd,
                    'dirbit':dirbit,
                    'flag':'',
                    'data':'',
                    'weight':1.00,
                    'color':'',
                    'delay':0.0,
                }
                croom['exits'][exitid] = crexit
                # done with the current exit.
            
            # done with current room, writ it out.

        # done with the current area
        areaCount += 1
        if areaCount > 2:
            break

    # End of loop for areas
    print(f'Done collection rooms')
    for roomid,room in convertedRooms.items():
        if roomid > voidRoomStart: continue

        voidRooms = {}
        for exitid, rexit in room['exits'].items():
            if rexit['vnum'] > voidRoomStart: 
                continue

            # temporary
            if exitid not in convertedRooms: continue

            exitroom = convertedRooms[exitid]

            # some are one way?
            if roomid not in exitroom['exits']: continue
            returnexit = exitroom['exits'][roomid]

            # Coords are stored in Data
            ccoords = room['data']
            ecoords = exitroom['data']

            #skip rooms that won't need void rooms
            # TODO add special exits here
            voidList = ['u','d','in','out']
            if rexit['dir'] in voidList: continue

            # Get the deltas
            dx = abs(ccoords[0] - ecoords[0])
            dy = abs(ccoords[1] - ecoords[1])

            # getting ready to create a void room.
            while dx > 1 or dy > 1:
                dx = abs(dx -1)
                dy = abs(dy -1)
                nextRoomNum += 1
                vid = nextRoomNum 

                voidroom = {
                    'vnum':vid,
                    'flags':4104, # void room flag
                    'color':'',
                    'name':'',
                    'sym':'',
                    'desc':'',
                    'area':'',
                    'note':'',
                    'terain':'',
                    'data':'',
                    'weight':0.01,
                    'roomid':'',
                    'exits':{},
                }
                voidRooms[vid] = voidroom

                # exit going back to the current room
                vexit = {
                    'vnum':roomid,
                    'dir': returnexit['dir'],
                    'dircmd': returnexit['dir'],
                    'dirbit': returnexit['dirbit'],
                    'flag':'',
                    'data':'',
                    'weight':0.01,
                    'color':'',
                    'delay':0.0,
                }
                voidroom['exits'][roomid] = vexit
                # exit contining through to the exit
                vexit = {
                    'vnum':exitid,
                    'dir': rexit['dir'],
                    'dircmd': rexit['dir'],
                    'dirbit': rexit['dirbit'],
                    'flag':'',
                    'data':'',
                    'weight':0.01,
                    'color':'',
                    'delay':0.0,
                }
                voidroom['exits'][exitid] = vexit

                # point this room to the new void room.
                rexit['vnum'] = vid

                # point the old exit to this void room.
                returnexit['vnum'] = vid
                # done with potential extra rooms

        # done generating void rooms for the current room.
        writeRoom(f, room)
        for _,vr in voidRooms.items():
            writeRoom(f, vr)

    print(f'Total rooms b4 {globalRoomCnt}, after {globalRoomCnt + len(voidrooms)}, void index {nextRoomNum}')

    # room 4271 goes to road, to id 4100

def getAreaIdsForRegion():
    for area in parsed['areas']:
        areaid = area["id"]
        for room in area['rooms']:
            if 'userData' in room:
                user = room['userData']
                if 'Game Area' in user:
                    print(f'{areaid}:Region: {user["Game Area"]}, sub: {area["name"]}')
            else: 
                if "name" not in room: print(f'Room has no name: {room["id"]}')
                else: print(f'Room has no user Data: {room["id"]}, {room["name"]}')

def getRoomsForRegion():
    # areas["rooms"][idx]["userData"]["Game Area"]
    # ^ a region.
    pass

def listRegions():
    currentRegion = ''
    for areas in parsed['areas']:
        for rooms in areas['rooms']:
            if 'userData' in rooms:
                user = rooms['userData']
                if 'Game Area' in user:
                    region = user["Game Area"]
                    if region == currentRegion: 
                        break
                    
                    currentRegion = user["Game Area"]

                    test = region.lower()
                    print(f'Region: {user["Game Area"]}')

