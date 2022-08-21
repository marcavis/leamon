#!/usr/bin/python
import sys
from pyexcel_ods3 import get_data
def main(filename):
    try:
        data = get_data(filename)
    except:
        print ("File", filename, "is not a valid ODS spreadsheet")
        return

    #Defaults, needed by some other sheets
    try:
        defaultsPage = data["Defaults"]
    except:
        print ("File", filename, "has no Defaults sheet")
        return

    #Stats
    try:
        statsPage = data["Stats"]
    except:
        print ("File", filename, "has no Stats sheet")
        return

    statsPage = [x for x in statsPage if x!=[]]
    monTotal = len(statsPage) - 2

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
        #add 0 or more empty columns in case the data has fewer values
        #filled in than expected
        line = line + [""] * (len(default) - len(line))
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
    
    #Pokedex
    try:
        pokedexPage = data["Pokedex"]
    except:
        print ("File", filename, "has no Pokedex sheet")
        return
    pokedexPage = [x for x in pokedexPage if x!=[]]
    pCols = [
        'species',
        'speciesName',
        'pokedexText1',
        'pokedexText2',
        'pokedexText3',
        'pokedexText4',
        'pokedexCategory',
        'pokedexHeight',
        'pokedexWeight',
        'pokemonScale',
        'pokemonOffset',
        'trainerScale',
        'trainerOffset',
        'bodyColor',
        'noFlip',
        ]
    default = ['error', 'Error', 'Pokedex message.', "", "", "",
    "Category", 160, 600,
    256, 0, 256, 0, 'black', "FALSE"]

    for line in pokedexPage[2:]:
        #add 0 or more empty columns in case the data has fewer values
        #filled in than expected
        line = line + [""] * (len(default) - len(line))
        print("Outputting to {}.py".format(line[0]))
        #ignore species
        for i in range(1, len(pCols)):
            if line[i] == "":
                line[i] = default[i]
            
            if 'pokedexText1' == pCols[i]:
                print("pokedexText = [")
                print('"' + line[i] + '",')
                print('"' + line[i+1] + '",')
                print('"' + line[i+2] + '",')
                print('"' + line[i+3] + '"]')
            elif 'bodyColor' in pCols[i]:
                line[i] = 'BODY_COLOR_' + line[i].upper().replace(" ", "_")
            
            if 'pokedexText' not in pCols[i]:
                print(pCols[i] + '="' + str(line[i]) + '"')
    
    #Images
    try:
        imagePage = data["Images"]
    except:
        print ("File", filename, "has no Image sheet")
        return
    imagePage = [x for x in imagePage if x!=[]]
    iCols = [   
        'species',
        'folder',
        'frontAnim',
        'backAnim',
        'iconPalette'
        ]
    default = ['error', 'error',
    defaultsPage[5][5], defaultsPage[6][5], 0]

    for line in imagePage[2:]:
        #add 0 or more empty columns in case the data has fewer values
        #filled in than expected
        line = line + [""] * (len(default) - len(line))
        print("Outputting to {}.py".format(line[0]))
        #ignore species
        for i in range(1, len(iCols)):
            if line[i] == "":
                line[i] = default[i]

            if iCols[i] == "folder":
                line[i] = defaultsPage[7][5] + "/" + line[i]
            
            print(iCols[i] + '="' + str(line[i]) + '"')

    #LevelUpLearnset
    try:
        lulPage = data["Learnset"]
    except:
        print ("File", filename, "has no Learnset sheet")
        return
    for i in range(len(lulPage)):
        if len(lulPage[i]) < len(lulPage[2]):
            lulPage[i] += [""] * (len(lulPage[2]) - len(lulPage[i]))
    #print(lulPage)
    for col in range(1, monTotal * 2 + 2, 2):
        for line in range(2, len(lulPage)):
            if lulPage[line][col] != "":
                print(lulPage[line][col], lulPage[line][col+1])
    

if __name__ == "__main__":
    main(sys.argv[1])