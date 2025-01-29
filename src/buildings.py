import re
import json
from pathlib import Path

with open("../data/Workshops.json") as file:
    workshops = json.load(file)

with open("../data/Farms.json") as file:
    workshops += json.load(file)

with open("../data/Institutions.json") as file:
    workshops += json.load(file)

with open("../data/RainCatchers.json") as file:
    workshops += json.load(file)

with open("../data/Extractors.json") as file:
    workshops += json.load(file)

with open("../data/Camps.json") as file:
    workshops += json.load(file)

with open("../data/FishingHuts.json") as file:
    workshops += json.load(file)

with open("../data/GathererHuts.json") as file:
    workshops += json.load(file)

for workshop in workshops:
    workshop["icon"] = f"img/buildings/{workshop['id'].replace(' ', '_')}_icon.png"
    del workshop["description"]
    for recipe in workshop["recipes"]:
        if "ingredients" in recipe:
            for ingredient_group in recipe["ingredients"]:
                for ingredient in ingredient_group:
                    ingredient["name"] = ingredient["name"].split("]")[-1].strip()
        if "product" in recipe:
            recipe["product"]["name"] = recipe["product"]["name"].split("]")[-1].strip()
        elif "servedNeed" in recipe:
            recipe["product"] = {"name": recipe["servedNeed"].strip()}
        elif "seekedResource" in recipe:
            recipe["product"] = {"name": recipe["seekedResource"].split("]")[-1].strip()}
        elif "seekedDeposits" in recipe:
            recipe["product"] = {"name": recipe["seekedDeposits"].split("]")[-1].strip(), "grade": recipe["grade"]}

        if "grade" in recipe:
            match recipe["grade"]:
                case "Grade0":
                    recipe["grade"] = "☆"
                case "Grade1":
                    recipe["grade"] = "★"
                case "Grade2":
                    recipe["grade"] = "★★"
                case "Grade3":
                    recipe["grade"] = "★★★"
        else:
            recipe["grade"] = ""
    
    for good in workshop["requiredGoods"]:
        good["name"] = good["name"].split("]")[-1].strip()

text = '\'' + json.dumps(workshops).replace("'", '\\\'') + '\''

with open('../js/buildings.json', 'w') as file:
    file.write(f'buildings_data = {text}')
