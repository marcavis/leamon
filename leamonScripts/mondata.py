#!/usr/bin/python
from pyexcel_ods3 import get_data
data = get_data("mondata.ods")

statsPage = data["Stats"]
statsPage = [x for x in statsPage if x!=[]]
sCols = [
    'species',
    'baseHp',
    'baseAttack',
    'baseDefense',
    'baseSpAttack',
    'baseSpDefense',
    'baseSpeed',
    'BST',
    'type1',
    'type2',
    'ability1',
    'ability2',
    'ability3',
    'evHp',
    'evAttack',
    'evDefense',
    'evSpAttack',
    'evSpDefense',
    'evSpeed',
    'itemCommon',
    'itemRare',
    'catchRate',
    'expYield',
    'genderRatio',
    'eggCycles',
    'friendship',
    'growthRate',
    'eggGroup1',
    'eggGroup2',
    ]
default = ['error', 10, 10, 10, 10, 10, 10, 60,
"normal", "normal", "none", "none", "none",
0, 0, 0, 0, 0, 0,
"none", "none", 255, 70, 50, 20, 70, "medium slow",
"human like", "human like"]
for line in statsPage[2:]:
    print("Outputting to {}.py".format(line[0]))
    for i in range(len(sCols)):
        if 'type' in sCols[i]:
            line[i] = "TYPE_" + line[i].upper()
        elif "eggGroup" in sCols[i]:
            if "1" in sCols[i] and line[i] == "":
                line[i] = default[i]
            line[i] = 'EGG_GROUP_' + line[i].upper().replace(" ", "_")

        if line[i] in ["TYPE_", "EGG_GROUP_"]:
            #copy first type or eggGroup if second is empty
            line[i] = line[i-1]

        if line[i] == "":
            line[i] = default[i]
        
        if 'ability' in sCols[i]:
            line[i] = 'ABILITY_' + line[i].upper().replace(" ", "_")
        elif 'item' in sCols[i]:
            line[i] = 'ITEM_' + line[i].upper().replace(" ", "_")
        elif 'genderRatio' in sCols[i]:
            if line[i] == "genderless":
                line[i] = "MON_GENDERLESS"
            else:
                line[i] = "PERCENT_FEMALE({})".format(line[i])
        elif 'growthRate' in sCols[i]:
            line[i] = 'GROWTH_' + line[i].upper().replace(" ", "_")
        


        print(sCols[i] + '="' + str(line[i]) + '"')