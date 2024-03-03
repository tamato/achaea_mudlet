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

    for ext in room['exits']:
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

# d is expected to be a 'rdir', which is room direction
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
    cid = colormapping[mapping]
    bit24 = crowdcolors[cid] # TODO might need an offset.
    rgb = bit24["color24RGB"]

    color = "<F"
    color += hex(rgb[0])[2:].upper()
    color += hex(rgb[1])[2:].upper()
    color += hex(rgb[2])[2:].upper()
    color +=">"
    return color

def getRoom(areaId,roomId):
    pass

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

        #  print(f'Converting area {areaid}')
        #  print(f'RoomCnt {roomCnt}')

        for roomIdx, room in enumerate(area['rooms']):

            rid = room['id']

            rcoords = room['coordinates']

            feature = ''
            if 'userData' in room:
                user = room['userData']

                #  if 'Game Area' in user: ttroom['areaName'] = user['Game Area']
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

            # room flags - 8 is void room,4104
            croom = {
                'vnum':rid,
                'flags':'',
                'color':'',
                'name':rname,
                'sym':feature,
                'desc':'',
                'areaname':'',
                'note':'',
                'terain':'',
                'data':'',
                'weight':1.00,
                'roomid':areaid,
                'exits':[],
            }

            for exitIdx, portal in enumerate(room['exits']):
                exitid = portal['exitId']

                # check if this leads to the same area id
                direction = 'in'
                sameArea = True
                direction = portal['name']

                if portal['name'] not in dirs:
                    print(f'Weird portal: {portal["name"]}')
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
                    rdircmd = dirs[portal['name']]
                
                skipVoidRooms = ['in','out','u','d']
                if rdir in skipVoidRooms: continue

                simplelist = ['n','s','e','w','u','d','in','out']
                orlist = ['nw','ne','se','sw']
                dirbit = 0
                if rdir in simplelist: dirbit = dirBits[rdir]
                if rdir in orlist: dirbit = dirBits[rdir[0]] | dirBits[rdir[1]]

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
                croom['exits'].append(crexit)

                # If the exitid is not in allrooms, it is because it is a void room.
                if exitid not in allrooms: 
                    continue;

                x = abs(rcoords[0] - allrooms[exitid]['coords'][0])
                y = abs(rcoords[1] - allrooms[exitid]['coords'][1])
                while x > 1 or y > 1:
                    if sameArea == False:
                        break

                    #  print(f'Diffs {x}, {y}')
                    if x > 0: x = abs(x - 1)
                    if y > 0: y = abs(y - 1)

                    vid = nextRoomNum
                    nextRoomNum += 1

                    voidroom = {
                        'vnum':vid,
                        'flag':4104, 
                        'color':'',
                        'name':'',
                        'sym':'',
                        'desc':'',
                        'areaname':'',
                        'note':'',
                        'terain':'',
                        'data':'',
                        'weight':0.01,
                        'roomid':'',
                        'exits':[],
                    }
                    voidrooms.append(voidroom)

                    crexit['data'] = 'voidRoom'
                    vexit = {
                        'vnum':exitid,
                        'dir': rdir,
                        'dircmd':rdircmd,
                        'dirbit':dirbit,
                        'flag':'',
                        'data':'',
                        'weight':0.01,
                        'color':'',
                        'delay':0.0,
                    }
                    voidroom['exits'].append(vexit)

                    # connect what used to be this rooms exit, 
                    # to the newly created void room.
                    ext = {}
                    if exitid < voidRoomStart:
                        ext = getExit(exitid,rid)
                    else:
                        ext = getVoidExit(exitid,rid)
                    ext['vnum'] = vid

                    # ponit the exit to our newly created void room.
                    crexit['vnum'] = vid

                    # create another exit for this void room to point back to the current room
                    vexit = {
                        'vnum':croom['vnum'],
                        'dir': reverseDir(rdir)[1],
                        'dircmd': reverseDir(rdir)[1],
                        'dirbit': reverseDir(rdir)[0],
                        'flag':'',
                        'data':'',
                        'weight':0.01,
                        'color':'',
                        'delay':0.0,
                    }
                    voidroom['exits'].append(vexit)
                    
                    #done with the void room
                    writeRoom(f, voidroom)

                # done with the current exit.
            
            # done with current room, writ it out.
            writeRoom(f, croom)

        # done with the current area
        areaCount += 1
        if False and areaCount > 2:
            break
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

