#!/usr/bin/python

import json

with open('map.json') as mapfile:
    parsed = json.load(mapfile)
  
for idx in parsed:
    print(idx)

print("-----------------------")
print(parsed['areaCount'])
print(parsed['roomCount'])
#print(parsed['customEnvColors'])
print(parsed['formatVersion'])
print(parsed['labelCount'])

print("[Areas]-----------------------")
print(len(parsed['areas']))

#  ids = []
#  counter = 0
#  for idx in parsed['areas']:
#      if 'Ashtan' in idx['name']:
#          ids.append(counter)
#          print(f'id: {idx["id"]}  name: {idx["name"]}, counter: {counter}')
#      counter += 1

#  print("[Room] -----------------------")
#  spot = parsed['areas'][47]
#  for k in spot.keys() :
#      print(k)

#  print(f'[{spot["name"]}]: id:[{spot["id"]}] roomcount: {spot["roomCount"]}')
#  print("[List of Rooms] -----------------------")
#  rooms = parsed['areas'][47]['rooms']
#  for k in rooms[1].items() :
#      print(f'{k}\n')
#      print(f'{k[0]}\n')
#      print(f'{k[1]}\n')
#      print("--")

print("[[[ ------------------------------ ]]]")
# find a specific room number, 436 (in Ashtan, Entering the main gate..)
# rooms are in 'areas'
foundroom = {}
inarea = {}
for areas in parsed['areas']:
    # areas is a list
    # each area has a directionary of rooms
    for room in areas['rooms']:
        if room['id'] == 436:
            foundroom = room
            inarea = areas
            break

# when loading in and getting the gmcp message with a room number
# we can find which area we are in.
# and then load the map for that location.
# Then when changing rooms, check if the 'area' has changed. 
#  If it has, load up the new area. 
print(foundroom['name'])
print(foundroom['environment'])
print(foundroom['userData']['Game Area'])
print(inarea['name'])
print("[[[ ------------------------------ ]]]")

# use top level userData for special glpyhs for rooms
# use envToColorMapping with 'environment' for colors
