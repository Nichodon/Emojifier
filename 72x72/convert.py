import json
import os
import os.path
from pprint import pprint

data = json.load(open('emojis.json'))

n=-1
while True:
    try:
        n += 1
        if data["emojis"][n]["unicode"] != "":
            print data["emojis"][n]["shortname"],
    except WindowsError:
        pass
