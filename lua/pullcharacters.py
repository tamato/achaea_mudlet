#!/usr/bin/python

import urllib.request
import shutil

# Download the file from `url` and save it locally under `file_name`:
url = 'https://api.achaea.com/characters.json'
file_name = 'characters.json'
write = 'w'

#url ="http://pbs.twimg.com/media/CCROQ8vUEAEgFke.jpg" 
#file_name = 'pytest.jpg'
#write = 'wb'

with urllib.request.urlopen(url) as response, open(file_name, write) as out_file:
    shutil.copyfileobj(response, out_file)
    print ('finished')

    # load up the json object
    # parse out each character
    # create a dictionary of them

