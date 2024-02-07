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
#  for areas in parsed['areas']:
#      # areas is a list
#      # each area has a directionary of rooms
#      for room in areas['rooms']:
#          if room['id'] == 436:
#              foundroom = room
#              inarea = areas
#              break


with open('world.map', 'w') as f:
    f.write("#VARIABLE worldmap {")

    f.write("\t{areas} {\n")
    for areas in parsed['areas']:
        roomid = areas['id']
        name = areas['name']
        roomCnt =  areas['roomCount']

        f.write(f'\t\t{{{roomid}}} {{\n')
        f.write(f'\t\t\t{{name}} {{{name}}}\n')
        f.write(f'\t\t\t{{roomCount}} {{{roomCnt}}}\n')
        f.write(f'\t\t\t{{rooms}} {{\n')
        for rooms in areas['rooms']:
            if 'name' not in rooms:
                break;
            if 'userData' not in rooms:
                break;
            
            name = rooms['name']
            coordinates = rooms['coordinates']
            environment = rooms['environment']
            roomid = rooms['id']
            exits = rooms['exits']
            user = rooms['userData']
            f.write(f'\t\t\t\t{{{roomid}}} {{\n')
            f.write(f'\t\t\t\t\t{{name}} {{{name}}}\n')

        f.write('\t\t\t\t}\n')
        f.write('\t\t\t}\n')
        f.write('\t\t}\n')

    f.write("\t}\n")

    f.write("\t{areaCount} {467}\n")
    f.write("\t{cusmtomEnvColors} {\n")
    f.write("\t}\n")
    f.write("\t{envToColorMapping} {\n")
    f.write("\t}\n")
    f.write("\t{formatVersion} {1}\n")
    f.write("\t{roomCount} {29871}\n")
    f.write("\t{userData} {\n")
    f.write("\t\t{mapFeatures} {\n")
    f.write("\t\t\t{subdivision} {S}\n")
    f.write("\t\t\t{ferry} {F}\n")
    f.write("\t\t\t{grate} {G}\n")
    f.write("\t\t\t{commdityshop} {C}\n")
    f.write("\t\t\t{news} {N}\n")
    f.write("\t\t\t{stronghold} {M}\n")
    f.write("\t\t\t{shop} {$}\n")
    f.write("\t\t\t{locksmith} {L}\n")
    f.write("\t\t\t{harbour} {H}\n")
    f.write("\t\t\t{wilderness} {W}\n")
    f.write("\t\t\t{arena} {A}\n")
    f.write("\t\t\t{postoffice} {P}\n")
    f.write("\t\t\t{bank} {B}\n")
    f.write("\t\t}\n")
    f.write("\t}\n")
    f.write("};\n")


