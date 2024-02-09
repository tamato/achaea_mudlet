#!/usr/bin/python

import json

with open('map.json') as mapfile:
    parsed = json.load(mapfile)

with open('world.tt', 'w') as f:
    tabs = 0
    f.write("#VARIABLE worldmap {\n")

    tabs = 1
    f.write(tabs*'\t'+'{areas} {\n')
    for areas in parsed['areas']:
        
        areaname = areas['name']
        #  print(f'Area name: {name}')

        roomCnt =  areas['roomCount']
        if roomCnt == 0: continue
        areaid = areas['id']

        f.write(2*'\t'+f'{{{areaname}}} {{\n')

        for rooms in areas['rooms']:
            if 'userData' in rooms:
                user = rooms['userData']
                if 'Game Area' in user:
                    f.write(3*'\t'+f'{{greaterArea}} {{{user["Game Area"]}}}\n')
                    break

        f.write(3*'\t'+f'{{roomCount}} {{{roomCnt}}}\n')
        f.write(3*'\t'+f'{{rooms}} {{\n')
        for rooms in areas['rooms']:

            roomid = rooms['id']
            f.write(4*'\t'+f'{{{roomid}}} {{\n')

            if 'name' in rooms:
                roomname = rooms['name']
                f.write(5*'\t'+f'{{name}} {{{roomname}}}\n')

            coordinates = rooms['coordinates']
            f.write(5*'\t'+f'{{x}} {{{coordinates[0]}}}\n')
            f.write(5*'\t'+f'{{y}} {{{coordinates[1]}}}\n')
            f.write(5*'\t'+f'{{z}} {{{coordinates[2]}}}\n')

            environment = rooms['environment']
            f.write(5*'\t'+f'{{env}} {{{environment}}}\n')

            f.write(5*'\t' + '{exits} {\n')
            for exits in rooms['exits']:
                f.write(6*'\t' + f'{{{exits["exitId"]}}} {{{exits["name"]}}}\n')
            f.write(5*'\t'+'}\n') # close room

            f.write(4*'\t'+'}\n') # close room

        f.write(3*'\t'+'}\n') # close roomS
        f.write(2*'\t'+'}\n') # close area id

    f.write(1*'\t'+'}\n') # close areas

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
  
#  print("-----------------------")
#  print(parsed['areaCount'])
#  print(parsed['roomCount'])
#  print(parsed['customEnvColors']
#  print(parsed['formatVersion'])
#  print(parsed['labelCount'])
#
#  print("[Areas]-----------------------")
#  print(len(parsed['areas']))

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

#  print("[[[ ------------------------------ ]]]")
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
#  print(foundroom['name'])
#  print(foundroom['environment'])
#  print(foundroom['userData']['Game Area'])
#  print(inarea['name'])
#  print("[[[ ------------------------------ ]]]")

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


