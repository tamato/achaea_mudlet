#!/usr/bin/python

import json
import sys

with open('map.json') as mapfile:
    parsed = json.load(mapfile)

allrooms = {}
for area in parsed['areas']:
    for room in area['rooms']:
        rid = room['id']
        if rid in allrooms: 
            print("Found Duplicate Room Num")
            sys.exit()

        allrooms[rid] = {'coords':room['coordinates'], 'areaid':area['id']} 

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

with open('world.map', 'w') as f:
    for area in parsed['areas']:
        areaname = area['name']
        roomCnt =  area['roomCount']
        if roomCnt == 0: continue
        
        areaid = area['id']
        if areaid < 0: continue

        for room in area['rooms']:
            ttroom = {}

            ttroom['areaId'] = areaid
            rid = room['id']

            rcoords = room['coordinates']

            feature = ''
            if 'userData' in room:
                user = room['userData']

                if 'Game Area' in user: ttroom['areaName'] = user['Game Area']
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
            rflag = 'flag'
            #  rcolor = colors(room['environment'])
            rcolor = "<101>"
            rsym = feature
            rdesc = 'desc'
            rarea = areaid
            rnote = 'note'; rterain = 'ter'; rdata = 'data'; rweight = '1.0'; 
            #TODO throw in area id somewhere.
            f.write(f'R {{{rid}}}{{{rflag}}}{{{rcolor}}}{{{rname}}}{{{rsym}}}')
            f.write(f'{{{rdesc}}}{{{rarea}}}{{{rnote}}}{{{rterain}}}')
            f.write(f'{{{rdata}}}{{{rweight}}}{{{areaid}}}\n')

            for portal in room['exits']:
                p = {}
                exitid = portal['exitId']
                p['vnum'] = exitid

                # check if this leads to the same area id
                direction = 'in'
                sameArea = False
                if allrooms[rid]['areaid'] == areaid:
                    direction = portal['name']
                    sameArea = True

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
                    p['dir'] = dirs[direction]
                    p['dircmd'] = dirs[portal['name']]
                
                skipVoidRooms = ['in','out','u','d']
                if p['dir'] in skipVoidRooms: continue

                x = abs(rcoords[0] - allrooms[exitid]['coords'][0])
                y = abs(rcoords[1] - allrooms[exitid]['coords'][1])
                z = abs(rcoords[2] - allrooms[exitid]['coords'][2])

                while x > 1 or y > 1:
                    print(f'Diffs {x}, {y}, {z}, dir {p["dir"]}/{p["dircmd"]}')
                    if x > 0: x = abs(x - 1)
                    if y > 0: y = abs(y - 1)

                    rid = len(allrooms) + len(voidrooms)
                    voidroom = {
                        'vnum':rid, 
                        'flag':4104, 
                        'color': '<270>',
                        'exits': [],
                    }
                    vexit = {'vnum':exitid}

                    voidrooms.append(voidroom)

                rexit = {
                    'vnum':rid
                    'dir':p['idr'],
                    'dircmd':p['dircmd']
                    'bitflag':0,
                    'flag':'',
                    'data':'',
                    'weight':1.00,
                    'color':'<270>',
                    'delay':0.0,
                }

                f.write(f'E {{{p["vnum"]}}}{{{p["dir"]}}}{{{p["dircmd"]}}}')
                f.write(f'{{{gotoexitdir}}}{{{eflag}}}{{{edata}}}')
                f.write(f'{{{eweight}}}{{{ecolor}}}{{{edelay}}}')
                f.write(f'\n')
            f.write(f'\n')

        break

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

