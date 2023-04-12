#!/usr/bin/env python3
import webbrowser
import pyfiglet
import keyboard
import json
import sys,getopt
text = pyfiglet.figlet_format("LazyHunter")
TARGET = sys.argv[1]

with open("data.json", "r") as file:
    siteMap = json.load(file)['url'][0]

for site in siteMap.keys():
    siteURL = siteMap[site]
    webbrowser.open_new_tab(f"{siteURL}{TARGET}")
    print("Press enter Key to Continue")
    keyboard.wait('enter')

