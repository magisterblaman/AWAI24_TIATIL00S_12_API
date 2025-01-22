import json

import requests


name = input("Vad heter du? ")

params = {
    "name": name
}

response = requests.get("https://api.nationalize.io", params)

data = response.json()

# Hannes - Möjliga nationaliteter
#  - Sverige (20%)
#  - Norge (13%)

f = open("country_codes.json", encoding="utf-8")
# contents = f.read()

country_codes = json.load(f)

print(data["name"] + " - Möjliga nationaliteter")

for i in range(len(data["country"])):
    country_code = data["country"][i]["country_id"]
    probability = round(data["country"][i]["probability"] * 100)
    country_name = country_codes[country_code]

    print("  - " + country_name + " (" + str(probability) + "%)")