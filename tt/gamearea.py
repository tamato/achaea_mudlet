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

for idx in parsed['areas']:
    if 'Minia' in idx['name']:
        print(f'id: {idx["id"]-1}  name: {idx["name"]} - {counter}')

print("[Room] -----------------------")
spot = parsed['areas'][12]
for k in spot.keys() :
    print(k)

print(f'[{spot["name"]}]: id:[{spot["id"]-1}] roomcount: {spot["roomCount"]}')
