#!/bin/bash
#do not put spaces between the variable and the value!
#e.g. SPECIES=CYuria, not SPECIES = "CYuria" (the quotes are not needed)
SPECIES=CYuria
images=aa/cyuria
#sed '/^anothervalue=.*/a after=me' test.txt
sed -i '/gMonFrontPic_Calyrex\[\]/a extern const u32 gMonFrontPic_'"$SPECIES"'\[\];' include/graphics.h
sed -i '/gMonBackPic_Calyrex\[\]/a extern const u32 gMonBackPic_'"$SPECIES"'\[\];' include/graphics.h
sed -i '/gMonShinyPalette_Calyrex\[\]/a extern const u32 gMonShinyPalette_'"$SPECIES"'\[\];' include/graphics.h
sed -i '/gMonPalette_Calyrex\[\]/a extern const u32 gMonPalette_'"$SPECIES"'\[\];' include/graphics.h
sed -i '/gMonIcon_Calyrex\[\]/a extern const u8 gMonIcon_'"$SPECIES"'\[\];' include/graphics.h
sed -i '/gMonFootprint_Calyrex\[\]/a extern const u8 gMonFootprint_'"$SPECIES"'\[\];' include/graphics.h

#after=CALYREX
echo extern const u32 gMonFrontPic_$SPECIES";"
frontanim=ANIM_H_VIBRATE
backanim=ANIM_V_SQUISH_AND_BOUNCE
animdelay=0
levitationpixels=0
frontpic_sizex=64 #8 to 64, divisible by 8
frontpic_sizey=64 #8 to 64, divisible by 8
frontpic_yoffset=0
iconpalette=0 #0 to 2

hoenndex=true
pokedex1="blah\n" 
pokedex2="blah\n"
pokedex3="blah\n"
pokedex4="blah\n"

pokedex_category="Fox-deer"
pokedex_height=15 #in meters/10
pokedex_weight=410 #in kilos/10
pokemonScale=256
pokemonOffset=0
trainerScale=256
trainerOffset=0

basehp=40
baseattack=70
basedefense=30
basespeed=25
basespattack=40
basespdefense=85
type1="dark"
type2="dark"
catchrate=150
expyield=70
evhp=0
evattack=0
evdefense=0 
evspeed=1
evspattack=0
evspdefense=0
item1=item_none
item2=item_none
genderRatio="PERCENT_FEMALE(50)"
eggCycles=20
friendship=100
growthRate=GROWTH_MEDIUM_SLOW
eggGroup1=EGG_GROUP_HUMAN_LIKE
eggGroup2=EGG_GROUP_HUMAN_LIKE
ability1=ABILITY_INSOMNIA
ability2=ABILITY_NONE
bodyColor=BODY_COLOR_BROWN
noFlip=FALSE

echo "Learnset is up to you"
echo "Cry is up to you"
echo "evolutions are up to you"
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


