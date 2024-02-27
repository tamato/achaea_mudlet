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

def colors(mapping):
    cid = colormapping[mapping]
    bit24 = crowdcolors[cid] # TODO might need an offset.
    rgb = bit24["color24RGB"]

    color = "<"
    color += hex(rgb[0])[2:].upper()
    color += hex(rgb[1])[2:].upper()
    color += hex(rgb[2])[2:].upper()
    color +=">"
    return color

with open('world.tt', 'w') as f:
    for area in parsed['areas']:
        areaname = area['name']
        roomCnt =  area['roomCount']
        if roomCnt == 0: continue
        
        areaid = area['id']
        if areaid < 0: continue

        for room in area['rooms']:
            ttroom = {}
            ttroom['exits'] = []
            ttroom['areaName'] = ''
            ttroom['name'] = ''

            ttroom['areaId'] = areaid
            rid = room['id']

            rcoords = room['coordinates']
            ttroom['colorId'] = room['environment']

            harbour = False
            shop = False
            bank = False
            stronghold = False
            wilder = False
            ferry = False
            news = False
            arena = False
            post = False
            comm = False
            grate = False
            locksmith = False
            if 'userData' in room:
                user = room['userData']

                if 'Game Area' in user: ttroom['areaName'] = user['Game Area']
                if 'feature-harbour' in user: harbour = True;
                if 'feature-shop' in user: shop = True;
                if 'feature-bank' in user: bank = True;
                if 'feature-stronghold' in user: stronghold  = True;
                if 'feature-wilderness' in user: wilderness = True;
                if 'feature-ferry' in user: ferry = True;
                if 'feature-news' in user: news = True;
                if 'feature-arena' in user: arena = True;
                if 'feature-postoffice' in user: postoffice = True;
                if 'feature-commodityshop' in user: commodityshope = True;
                if 'feature-grate' in user: grate = True;
                if 'feature-locksmith' in user: locksmith = True;

            rname = ''
            if 'name' in room:
                rname = room['name']

            rexits = []
            for portal in room['exits']:
                exitid = portal['exitId']
                # check if this leads to the same area id
                direction = 'in'
                sameArea = False
                if allrooms[rid]['areaid'] == areaid
                    direction = portal['name']
                    sameArea = True

                x = abs(rcoords[0] - ecoords[0])
                y = abs(rcoords[1] - ecoords[1])

                # TODO needs to loop
                if x > 1 or y > 1 and sameArea:

                    void = {'dir': direction, 'flag':'void', 'number':globalRoomCnt+voidRoomOffset}
                    voidRoomOffset += 1


            # room flags - 8 is void room,4104
            rflag = ''
            rcolor = '<170>'
            rsym = ''
            rdesc = ''
            rarea = ttroom['areaName']
            rnote = ''; rterain = ''; rdata = ''; rweight = ''; rid = ''
            #TODO throw in area id somewhere.
            f.write(f'R{{{rid}}}{{{rflag}}}{{{rcolor}}}{{{rname}}}{{{rsym}}}')
            f.write(f'{{{rdesc}}}{{{rarea}}}{{{rnote}}}{{{rterain}}}')
            f.write(f'{{{rdata}}}{{{rweight}}}{{{areaid}}}\n')
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

getAreaIdsForRegion()
