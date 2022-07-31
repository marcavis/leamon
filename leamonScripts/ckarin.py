#!/usr/bin/python
#do not put spaces between the variable and the value!
#e.g. SPECIES=CYuria, not SPECIES = "CYuria" (the quotes are not needed)
species="CKarin"
images="leamon/ckarin"
animate=[(0,1)] #must be a list of tuples, like [(0,10),(1,20)]
frontSpriteSize = (64,64)
frontYOffset = 0
backSpriteSize = (64,64)
backYOffset = 0
frontAnim = "ANIM_V_SQUISH_AND_BOUNCE"
backAnim = "BACK_ANIM_H_VIBRATE"
iconPalette = 0 #0, 1 or 2
#don't put newlines in here
pokedexText = [
"Slowly recovering her self-control.",
"",
"",
""]

pokedexCategory="Fox-deer"
pokedexHeight=17 #in meters/10
pokedexWeight=530 #in kilos/10
pokemonScale=256
pokemonOffset=0
trainerScale=256
trainerOffset=0


baseHP=40
baseAttack=50
baseDefense=30
baseSpAttack=60
baseSpDefense=90
baseSpeed=70
type1="TYPE_GHOST"
type2="TYPE_FAIRY"
catchRate=150
expYield=70
evHP=0
evAttack=0
evDefense=0 
evSpeed=0
evSpAttack=0
evSpDefense=1
item1="ITEM_NONE"
item2="ITEM_NONE"
genderRatio="PERCENT_FEMALE(50)"
eggCycles=20
friendship=100
growthRate="GROWTH_MEDIUM_SLOW"
eggGroup1="EGG_GROUP_HUMAN_LIKE"
eggGroup2="EGG_GROUP_HUMAN_LIKE"
ability1="ABILITY_INSOMNIA"
ability2="ABILITY_NONE"
ability3="ABILITY_NONE"
bodyColor="BODY_COLOR_BROWN"
noFlip="FALSE"

#dark allure level 30?
learnset="""
static const struct LevelUpMove s""" + species + """LevelUpLearnset[] = {
    LEVEL_UP_MOVE( 1, MOVE_TACKLE),
    LEVEL_UP_MOVE( 1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(26, MOVE_POWER_GEM),
    LEVEL_UP_MOVE(41, MOVE_CALM_MIND),
    LEVEL_UP_MOVE(46, MOVE_SHADOW_BALL),
    LEVEL_UP_END
};"""
#declare sprites
counter = 0
with open("include/graphics.h", "r") as in_file:
    buf = in_file.readlines()

with open("include/graphics.h", "w") as out_file:
    for line in buf:
        if "Calyrex[]" in line:
            counter += 1
            if "gMonFrontPic_" in line:
                line = line + "extern const u32 gMonFrontPic_"+species+"[];\n"
            if "gMonBackPic_" in line:
                line = line + "extern const u32 gMonBackPic_"+species+"[];\n"
            if "gMonShinyPalette_" in line:
                line = line + "extern const u32 gMonShinyPalette_"+species+"[];\n"
            if "gMonPalette_" in line:
                line = line + "extern const u32 gMonPalette_"+species+"[];\n"
            if "gMonIcon_" in line:
                line = line + "extern const u8 gMonIcon_"+species+"[];\n"
            if "gMonFootprint_" in line:
                line = line + "extern const u8 gMonFootprint_"+species+"[];\n"
        out_file.write(line)
print(counter, "of 6 sprite declarations inserted")

counter = 0
with open("src/data/graphics/pokemon.h", "r") as in_file:
    buf = in_file.readlines()

with open("src/data/graphics/pokemon.h", "w") as out_file:
    for line in buf:
        if "Calyrex[]" in line:
            counter += 1
            if "gMonFrontPic_" in line:
                line = line + "const u32 gMonFrontPic_"+species+"[] = "
                line = line + 'INCBIN_U32("graphics/'+images+'/front.4bpp.lz");\n'
            if "gMonBackPic_" in line:
                line = line + "const u32 gMonBackPic_"+species+"[] = "
                line = line + 'INCBIN_U32("graphics/'+images+'/back.4bpp.lz");\n'
            if "gMonShinyPalette_" in line:
                line = line + "const u32 gMonShinyPalette_"+species+"[] = "
                line = line + 'INCBIN_U32("graphics/'+images+'/shiny.gbapal.lz");\n'
            if "gMonPalette_" in line:
                line = line + "const u32 gMonPalette_"+species+"[] = "
                line = line + 'INCBIN_U32("graphics/'+images+'/normal.gbapal.lz");\n'
            if "gMonIcon_" in line:
                line = line + "const u8 gMonIcon_"+species+"[] = "
                line = line + 'INCBIN_U8("graphics/'+images+'/icon.4bpp");\n'
            if "gMonFootprint_" in line:
                line = line + "const u8 gMonFootprint_"+species+"[] = "
                line = line + 'INCBIN_U8("graphics/'+images+'/footprint.1bpp");\n'
        out_file.write(line)
print(counter, "of 6 sprite declarations inserted")
#animate

with open("src/data/pokemon_graphics/front_pic_anims.h", "r") as in_file:
    buf = in_file.readlines()

with open("src/data/pokemon_graphics/front_pic_anims.h", "w") as out_file:
    spot = False
    for line in buf:
        if "AnimCmd sAnim_" in line and spot:
            oldline = line[:]
            line = "static const union AnimCmd sAnim_" + species.upper() + "_1[] =\n"
            line = line + "{\n"
            for animFrame in animate:            
                line = line + "    ANIMCMD_FRAME"+str(animFrame)+",\n"
            line = line + "    ANIMCMD_END,\n"
            line = line + "};\n\n" + oldline
            spot = False
        elif "sAnim_CALYREX_" in line:
            spot = True
        out_file.write(line)

with open("src/data/pokemon_graphics/front_pic_anims.h", "r") as in_file:
    buf = in_file.readlines()

with open("src/data/pokemon_graphics/front_pic_anims.h", "w") as out_file:
    spot = False
    for line in buf:
        if "sAnims_" in line and spot:
            oldline = line[:]
            line = "static const union AnimCmd *const sAnims_" + species.upper() + "[] ={\n"
            line = line + "    sAnim_GeneralFrame0,\n"
            line = line + "    sAnim_" + species.upper() + "_1,\n"
            line = line + "};\n\n" + oldline
            spot = False
        elif "sAnims_CALYREX[]" in line:
            spot = True
        out_file.write(line)

with open("src/data/pokemon_graphics/front_pic_anims.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon_graphics/front_pic_anims.h", "w") as out_file:
    for line in buf:
        if "ANIM_CMD(CALYREX)" in line:
            line = line + "    ANIM_CMD(" + species.upper() + "),\n"
        out_file.write(line)


with open("src/pokemon.c", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/pokemon.c", "w") as out_file:
    spot = False
    for line in buf:
        if "const u8 sMonFrontAnimIdsTable" in line:
            spot = True
        if "SPECIES_CALYREX - 1" in line and spot:
            newline = "    [SPECIES_" + species.upper() + " - 1]"
            newline = newline + " "*(32 - len(newline))
            newline = newline + "= " + frontAnim + ",\n"
            line = line + newline
            spot = False
        out_file.write(line)

if backAnim not in [0, ""]:
    with open("src/pokemon_animation.c", "r") as in_file:
        buf = in_file.readlines()
                
    with open("src/pokemon_animation.c", "w") as out_file:
        spot = False
        for line in buf:
            if "const u8 sSpeciesToBackAnimSet" in line:
                spot = True
            if "SPECIES_CHIMECHO" in line and spot:
                newline = "    [SPECIES_" + species.upper() + "]"
                newline = newline + " "*(25 - len(newline))
                newline = newline + "= " + backAnim + ",\n"
                line = line + newline
                spot = False
            out_file.write(line)

print ("If you want to delay the time between when the Pokémon appears and when the animation starts, you can add an entry to sMonAnimationDelayTable")
print("Edit src/pokemon.c")

print("\nIf you want your Pokémon to fly above the ground, you can add an entry to gEnemyMonElevation.")
print("Edit src/data/pokemon_graphics/enemy_mon_elevation.h")

print("\nRearranging the pokedex is best done after adding all monsters")

"""update tables"""
with open("src/data/pokemon_graphics/front_pic_table.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon_graphics/front_pic_table.h", "w") as out_file:
    for line in buf:
        if "SPECIES_SPRITE(CALYREX," in line:
            line = line + "    SPECIES_SPRITE(" + species.upper() + ", "
            line = line + "gMonFrontPic_" + species + "),\n"
        out_file.write(line)


with open("src/data/pokemon_graphics/back_pic_table.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon_graphics/back_pic_table.h", "w") as out_file:
    for line in buf:
        if "SPECIES_SPRITE(CALYREX," in line:
            line = line + "    SPECIES_SPRITE(" + species.upper() + ", "
            line = line + "gMonBackPic_" + species + "),\n"
        out_file.write(line)

with open("src/data/pokemon_graphics/front_pic_coordinates.h", "r") as in_file:
    buf = in_file.readlines()

with open("src/data/pokemon_graphics/front_pic_coordinates.h", "w") as out_file:
    spot = False
    for line in buf:
        if "[SPECIES_" in line and spot:
            oldline = line[:]
            line = "    [SPECIES_" + species.upper() + "] =\n    {\n"
            line = line + "        .size = MON_COORDS_SIZE"+str(frontSpriteSize)+",\n"
            if frontYOffset != 0:
                line = line + "        .y_offset = " + str(frontYOffset) + ",\n"
            line = line + "    },\n" + oldline
            spot = False
        elif "[SPECIES_CALYREX]" in line:
            spot = True
        out_file.write(line)

with open("src/data/pokemon_graphics/back_pic_coordinates.h", "r") as in_file:
    buf = in_file.readlines()

with open("src/data/pokemon_graphics/back_pic_coordinates.h", "w") as out_file:
    spot = False
    for line in buf:
        if "[SPECIES_" in line and spot:
            oldline = line[:]
            line = "    [SPECIES_" + species.upper() + "] =\n    {\n"
            line = line + "        .size = MON_COORDS_SIZE"+str(backSpriteSize)+",\n"
            if frontYOffset != 0:
                line = line + "        .y_offset = " + str(backYOffset) + ",\n"
            line = line + "    },\n" + oldline
            spot = False
        elif "[SPECIES_CALYREX]" in line:
            spot = True
        out_file.write(line)

with open("src/data/pokemon_graphics/footprint_table.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon_graphics/footprint_table.h", "w") as out_file:
    for line in buf:
        if "[SPECIES_CALYREX]" in line:
            line = line + "    [SPECIES_" + species.upper() + "] = "
            line = line + "gMonFootprint_" + species + ",\n"
        out_file.write(line)

with open("src/data/pokemon_graphics/palette_table.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon_graphics/palette_table.h", "w") as out_file:
    for line in buf:
        if "SPECIES_PAL(CALYREX," in line:
            line = line + "    SPECIES_PAL(" + species.upper() + ", "
            line = line + "gMonPalette_" + species + "),\n"
        out_file.write(line)

with open("src/data/pokemon_graphics/shiny_palette_table.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon_graphics/shiny_palette_table.h", "w") as out_file:
    for line in buf:
        if "SPECIES_SHINY_PAL(CALYREX," in line:
            line = line + "    SPECIES_SHINY_PAL(" + species.upper() + ", "
            line = line + "gMonShinyPalette_" + species + "),\n"
        out_file.write(line)

with open("src/pokemon_icon.c", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/pokemon_icon.c", "w") as out_file:
    for line in buf:
        if "[SPECIES_CALYREX]" in line:
            if any(["0" in line, "1" in line, "2" in line]): #icon palette
                line = line + "    [SPECIES_" + species.upper() + "] = " + str(iconPalette) + ",\n"
            else:   #icon image
                line = line + "    [SPECIES_" + species.upper() + "] = "
                line = line + "gMonIcon_" + species + ",\n"
        out_file.write(line)

#declare a species constant
previousLastMon = ""
with open("include/constants/species.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("include/constants/species.h", "w") as out_file:
    for line in buf:
        if "#define FORMS_START" in line:
            previousLastMon = line.split("_")[-1].strip()
            line = "#define FORMS_START SPECIES_" + species.upper() + "\n"
        out_file.write(line)

with open("include/constants/species.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("include/constants/species.h", "w") as out_file:
    for line in buf:
        if ("#define SPECIES_" + previousLastMon + " ") in line:
            previousLastMonNumber = int(line.split(" ")[-1].strip())
            previousLastMonNumber = str(previousLastMonNumber + 1)
            line = line + "#define SPECIES_" + species.upper() + " " + previousLastMonNumber + "\n"
        out_file.write(line)

#devise a name
with open("src/data/text/species_names.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/text/species_names.h", "w") as out_file:
    for line in buf:
        if ("[SPECIES_CALYREX]") in line:
            line = line + "    [SPECIES_" + species.upper() + "] = _("
            line = line + '"' + species + '"' + "),\n"
        out_file.write(line)

#define pokedex entry
previousLastNatMon = "CALYREX"
previousLastHoennMon = "DEOXYS"
with open("include/constants/pokedex.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("include/constants/pokedex.h", "w") as out_file:
    for line in buf:
        if ("#define NATIONAL_DEX_COUNT") in line:
            previousLastNatMon = line.split("_")[-1].strip()
        if ("#define HOENN_DEX_COUNT") in line:
            previousLastHoennMon = line.split("_")[-1].strip()
        out_file.write(line)

with open("include/constants/pokedex.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("include/constants/pokedex.h", "w") as out_file:
    for line in buf:
        if ("NATIONAL_DEX_" + previousLastNatMon + ",") in line:
            line = line + "    NATIONAL_DEX_" + species.upper() + ",\n"
        if ("NATIONAL_DEX_" + previousLastHoennMon + ",") in line:
            line = line + "    HOENN_DEX_" + species.upper() + ",\n"
        out_file.write(line)



with open("include/constants/pokedex.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("include/constants/pokedex.h", "w") as out_file:
    for line in buf:
        if ("#define NATIONAL_DEX_COUNT") in line:
            line = "#define NATIONAL_DEX_COUNT  NATIONAL_DEX_" + species.upper() + "\n"
        if ("#define HOENN_DEX_COUNT") in line:
            line = "#define HOENN_DEX_COUNT (HOENN_DEX_" + species.upper() + " + 1)\n"
        out_file.write(line)

with open("src/pokemon.c", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/pokemon.c", "w") as out_file:
    for line in buf:
        if ("SPECIES_TO_NATIONAL(CALYREX)") in line:
            line = line + "    SPECIES_TO_NATIONAL(" + species.upper() + "),\n"
        if ("SPECIES_TO_HOENN(DEOXYS)") in line:
            line = line + "    SPECIES_TO_HOENN(" + species.upper() + "),\n"
        if ("HOENN_TO_NATIONAL(DEOXYS)") in line:
            line = line + "    HOENN_TO_NATIONAL(" + species.upper() + "),\n"
        out_file.write(line)

with open("src/data/pokemon/pokedex_text.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon/pokedex_text.h", "w") as out_file:
    #endLine = buf[-1]
    for line in buf:
        out_file.write(line)
    line = "\nconst u8 g" + species + "PokedexText[] = _(\n"
    line += '    "' + pokedexText[0] + '\\n"\n'
    line += '    "' + pokedexText[1] + '\\n"\n'
    line += '    "' + pokedexText[2] + '\\n"\n'
    line += '    "' + pokedexText[3] + '");\n'
    out_file.write(line)


with open("src/data/pokemon/pokedex_entries.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon/pokedex_entries.h", "w") as out_file:
    for line in buf[:-1]:
        out_file.write(line)
    tab = " " * 4
    line = "\n" + tab + "[NATIONAL_DEX_" + species.upper() + "] =\n"
    line += tab + "{\n"
    line += tab + tab + '.categoryName = _("' + pokedexCategory + '"),\n'
    line += tab + tab + ".height = " + str(pokedexHeight) + ",\n"
    line += tab + tab + ".weight = " + str(pokedexWeight) + ",\n"
    line += tab + tab + ".description = g" + species + "PokedexText,\n"
    line += tab + tab + ".pokemonScale = " + str(pokemonScale) + ",\n"
    line += tab + tab + ".pokemonOffset = " + str(pokemonOffset) + ",\n"
    line += tab + tab + ".trainerScale = " + str(trainerScale) + ",\n"
    line += tab + tab + ".trainerOffset = " + str(trainerOffset) + ",\n"
    line += tab + "},\n};\n"
    out_file.write(line)

#TODO: proper orderings
with open("src/data/pokemon/pokedex_orders.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon/pokedex_orders.h", "w") as out_file:
    for line in buf:
        if ("    NATIONAL_DEX_CALYREX,") in line:
            line = line + "    NATIONAL_DEX_" + species.upper() + ",\n"
        out_file.write(line)

#base stats
with open("src/data/pokemon/base_stats.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon/base_stats.h", "w") as out_file:
    for line in buf[:-1]:
        out_file.write(line)
    tab = " " * 4
    line = "\n" + tab + "[SPECIES_" + species.upper() + "] =\n"
    line += tab + "{\n"
    line += tab + tab + ".baseHP        = " + str(baseHP) + ",\n"
    line += tab + tab + ".baseAttack    = " + str(baseAttack) + ",\n"
    line += tab + tab + ".baseDefense   = " + str(baseDefense) + ",\n"
    line += tab + tab + ".baseSpeed     = " + str(baseSpeed) + ",\n"
    line += tab + tab + ".baseSpAttack  = " + str(baseSpAttack) + ",\n"
    line += tab + tab + ".baseSpDefense = " + str(baseSpDefense) + ",\n"
    line += tab + tab + ".type1 = " + str(type1) + ",\n"
    line += tab + tab + ".type2 = " + str(type2) + ",\n"
    line += tab + tab + ".catchRate = " + str(catchRate) + ",\n"
    line += tab + tab + ".expYield = " + str(expYield) + ",\n"
    if evHP > 0:
        line += tab + tab + ".evYield_HP = " + str(evHP) + ",\n"
    if evAttack > 0:
        line += tab + tab + ".evYield_Attack = " + str(evAttack) + ",\n"
    if evDefense > 0:
        line += tab + tab + ".evYield_Defense = " + str(evDefense) + ",\n"
    if evSpeed > 0:
        line += tab + tab + ".evYield_Speed = " + str(evSpeed) + ",\n"
    if evSpAttack > 0:
        line += tab + tab + ".evYield_SpAttack = " + str(evSpAttack) + ",\n"
    if evSpDefense > 0:
        line += tab + tab + ".evYield_SpDefense = " + str(evSpDefense) + ",\n"
    if item1 != "ITEM_NONE":
        line += tab + tab + ".item1 = " + str(item1) + ",\n"
    if item2 != "ITEM_NONE":
        line += tab + tab + ".item2 = " + str(item2) + ",\n"
    line += tab + tab + ".genderRatio = " + genderRatio + ",\n"
    line += tab + tab + ".eggCycles = " + str(eggCycles) + ",\n"
    line += tab + tab + ".friendship = " + str(friendship) + ",\n"
    line += tab + tab + ".growthRate = " + growthRate + ",\n"
    line += tab + tab + ".eggGroup1 = " + eggGroup1 + ",\n"
    line += tab + tab + ".eggGroup2 = " + eggGroup2 + ",\n"
    abils = ability1 + ", " + ability2 + ", " + ability3
    line += tab + tab + ".abilities = {" + abils + "},\n"
    line += tab + tab + ".bodyColor = " + bodyColor + ",\n"
    line += tab + tab + ".noFlip = " + noFlip + ",\n"
    line += tab + "},\n};\n"
    out_file.write(line)

#learnsets
with open("src/data/pokemon/level_up_learnsets.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon/level_up_learnsets.h", "w") as out_file:
    for line in buf[:-1]:
        out_file.write(line)
    line = "};\n" + learnset[:] + "\n"
    out_file.write(line)

with open("src/data/pokemon/level_up_learnset_pointers.h", "r") as in_file:
    buf = in_file.readlines()
            
with open("src/data/pokemon/level_up_learnset_pointers.h", "w") as out_file:
    for line in buf:
        if "[SPECIES_CALYREX]" in line:
            line = line + "    [SPECIES_" + species.upper() + "] = "
            line = line + "s" + species + "LevelUpLearnset,\n"
        out_file.write(line)

#TODO: define cry
#TODO: define evolutions
#TODO: easy chat? does anyone care
print("edit src/data/wild_encounters.json to add it to the wilderness!")



"""
frontanim=ANIM_H_VIBRATE
backanim=ANIM_V_SQUISH_AND_BOUNCE
animdelay=0
levitationpixels=0
frontpic_sizex=64 #8 to 64, divisible by 8
frontpic_sizey=64 #8 to 64, divisible by 8
frontpic_yoffset=0
iconpalette=0 #0 to 2







echo "Learnset is up to you"
echo "Cry is up to you"
echo "evolutions are up to you"
"""



#easy-chat - find the first letter? ignore so far probably

#*"edit src/data/pokemon_graphics/front_pic_anims.h to configure the animations!

#*find which pics are in the folder; expansion puts them all in src/data/graphics/pokemon.h
#*pics data are in include/graphics.h and src/data/graphics/pokemon.h
#*if anim_front.png is there, use it and ignore front.png; otherwise use front.png

#static const union AnimCmd sAnim_CALYREX_1[] =
#{
#    ANIMCMD_FRAME(0, 1),
#--
#};

#static const union AnimCmd *const sAnims_CALYREX[] ={
#    sAnim_GeneralFrame0,
#    sAnim_CALYREX_1,
#};

#src/pokemon.c
#[SPECIES_MEWTHREE - 1]    =ANIM_GROW_VIBRATE,


