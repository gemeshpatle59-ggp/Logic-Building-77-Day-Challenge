# Create a to-do manager using a list/dictionary with add, update, delete, complete, search, and numbering.

import json
import os

To_do = {
    "learn python" : True,
    "Hit GYM" : False
}

def load_data():
    global To_do

    if os.path.exists("To_do.json"):
        with open("To_do.json", "r") as file:
            To_do = json.load(file)

    else:
        save_data()

def save_data():
    with open("To_do.json","w") as file:
        json.dump(To_do,file,indent=4)

