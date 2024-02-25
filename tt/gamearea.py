#!/usr/bin/python

import json

with open('map.json') as mapfile:
    parsed = json.load(mapfile)

with open('world.tt', 'w') as f:
    for areas in parsed['areas']:
        
        areaname = areas['name']
        roomCnt =  areas['roomCount']
        if roomCnt == 0: continue
        areaid = areas['id']

        for rooms in areas['rooms']:
            if 'userData' in rooms:
                user = rooms['userData']
                if 'Game Area' in user:
                    break

        for rooms in areas['rooms']:

            roomid = rooms['id']

            if 'name' in rooms:
                roomname = rooms['name']

            coordinates = rooms['coordinates']
            environment = rooms['environment']

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
