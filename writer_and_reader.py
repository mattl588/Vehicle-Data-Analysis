# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:33:44 2022

@author: Steve
"""

#Inputs: year, country, condition, color, edition, RHD/LHD, 

import json
from os.path import exists

year = input("What's the year?\n")

country = input("What country is it from?\n")

condition = input("Is the condition poor, fair, good, or excellent?\n")

color = input("What is the color?\n")

edition = input("Is this a 90 or 110?\n")

date = input("Date of listing in MM/DD/YY format?\n")

wheel = input("RHD or LHD?\n")

file = "data.json"
file_exists = exists(file)

vehicle = {
        "year": year,
        "country": country,
        "condition": condition,
        "color": color,
        "edition": edition,
        "wheel": wheel
}

if (file_exists):
    with open(file) as f:
        unpacked_data = json.load(f)
        if type(unpacked_data) is dict:
            unpacked_data = [unpacked_data]
        print(unpacked_data)
        unpacked_data.append(vehicle)
    with open(file, 'w') as json_file:
        json.dump(unpacked_data, json_file, indent = 4)

else: 
    with open ("data.json", 'w') as j:
        json.dump(vehicle, j, indent = 4)
