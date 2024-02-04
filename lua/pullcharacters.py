#!/usr/bin/python

import urllib.request
import json

import os
from os import listdir
from os.path import isfile, join

# Download the file from `url` and save it locally under `file_name`:
url = 'https://api.achaea.com/characters.json'
file_name = 'characters.json'

with urllib.request.urlopen(url) as response:
    # load up the json object
    jsondata = json.loads(response.read())
    print ('finished downloading list of characters')
    print(jsondata['count'])

    # parse out each character
    for c in jsondata['characters']:
        uri = c['uri']
        name = c['name']
        with urllib.request.urlopen(uri) as charuri:
            charjson = json.loads(charuri.read())
            with open(f'../characters/{name}.json', 'w') as charfile:
                json.dump(charjson, charfile)



print ('finished characters')

# load up all the character files
path = f'{os.environ["HOME"]}/repos/achaea_mudlet/characters'
allcharacters = [f for f in listdir(path) if isfile(join(path, f))]

characters = {}
fg_magenta = '<Fff33ff>'
fg_yellow = '<Fffff00>'
fg_red = '<Fff0000>'

with open(f'{path}/../tt/character_highlights.tt', 'w') as hi:
    hi.write(f'#class chardatabase kill\n')
    hi.write(f'#class chardatabase open\n\n')
    hi.write('#alias {whois} { #var chardb[%0] }\n\n')
    hi.write('#ticker {updatechardb} {#read character_highlights.tt} {60}\n\n')

    for file in allcharacters:
        with open(f'{path}/{file}', 'r') as charfile:
            char = json.load(charfile)
            try:
                # create a dictionary of them
                #  print(char['name'])
                # could use 24 bit colors, format is <F000000> <FFFFFFF>
                color = fg_yellow

                city = char['city']
                if 'ashtan'     in city: color = fg_magenta
                if 'hashan'     in city: color = '<400>'+color   # underscore
                if 'targosas'   in city: color = '<500>'+color   # blink
                if 'underworld' in city: color = '<414>'          # underscore, read, blue
                if 'mhaldor'    in city: color = '<110>'   

                char['color'] = color
                characters[char['name']] = char
                hi.write(f'#highlight {{{{{char["name"]}(,| )}}}} {{{color}}}\n')
            except Exception as inst:
                print("bad")
                print(type(inst))    # the exception type
                print(inst.args)     # arguments stored in .args
                print(inst)          # __str__ allows args to be printed directly,
                                     # but may be overridden in exception subclasses
                break
# {"name":"Aaraka","fullname":"Aaraka","city":"cyrene","house":"(none)","level":"5","class":"blademaster","mob_kills":"9","player_kills":"0","xp_rank":"0","explorer_rank":"1257"}


    hi.write('\n')
    hi.write('#var {chardb}\n')
    hi.write('{\n')
    for char in characters.items():
        hi.write(f'\t{{{char[0]}}} {{\n')

        hi.write(f'\t\t{{lvl}}\t\t{{{char[1]["level"]}}}\n')
        hi.write(f'\t\t{{city}}\t{{{char[1]["city"]}}}\n')
        hi.write(f'\t\t{{pvp}}\t\t{{{char[1]["player_kills"]}}}\n')
        hi.write(f'\t\t{{class}}\t{{{char[1]["class"]}}}\n')
        hi.write(f'\t\t{{xp}}\t\t{{{char[1]["xp_rank"]}}}\n')
        hi.write(f'\t\t{{explorer}} {{{char[1]["explorer_rank"]}}}\n')
        hi.write(f'\t\t{{color}}\t{{{char[1]["color"]}}}\n')

        hi.write('\t};\n\n')
    hi.write('};\n\n')


    hi.write(f'#class chardatabase close\n')
    hi.write(f'#class chardatabase save\n')


