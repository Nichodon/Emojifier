import json
import os
import os.path
from pprint import pprint

data = json.load(open('emojis.json'))

n=-1
while True:
    try:
        n += 1
        if os.path.isfile(data["emojis"][n]["unicode"] + ".png"):
            print "h"
        if data["emojis"][n]["unicode"] != "":
            os.rename(data["emojis"][n]["unicode"] + ".png",
                      data["emojis"][n]["shortname"].replace(":", "") + ".png")
            print "success"
    except WindowsError:
        pass
