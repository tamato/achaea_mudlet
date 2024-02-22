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
    # areas["rooms"][idx]["userData"]["Game Area"]
    # ^ a region.
    pass

def getRoomsForRegion():
    # areas["rooms"][idx]["userData"]["Game Area"]
    # ^ a region.
    pass


