import random, time 

def shop_randomising():
    print('')

 #prints the first random value for the store
    slot1 = random.randint(1, 6)

    if 1 == slot1:
        storeA = 1
        print('The store was missing anything that could be used as a weapon')
        print('')

    elif 2 == slot1:
        storeA = 2
        print('Their first item was a rusty sheet of metal that looks like its has been cut to be some kind of sword')
        print('')

    elif 3 == slot1:
        storeA = 3
        print('Their first item was a old shattered sword that must have seen years upon years of uses')
        print('')

    elif 4 == slot1:
        storeA = 4
        print('Their first item was a blunt sword that must have been forged by either a really young or a really old blacksmith...')
        print('')
        
    elif 5 == slot1:
        storeA = 5
        print('Their first item was a steel sword that looked newly sharpened and free of the touch of rust')
        print('')
        
    elif 6 == slot1:
        storeA = 6
        print('Their first item was a freshly sharpened pristine sword that must have stolen much blood, sweat and tears from the blacksmiths that forged such a weapon of its caliber')
        print('')

    #=========================================================================================
    print('')

    

 #prints the second random value for the store
    slot2 = random.randint(1, 6)
    if 1 == slot2:
        storeB = 1
        print('The store had nothing that was edible')
        print('')

    elif 2 == slot2:
        storeB = 2
        print("There was a rotten fruit on a table, what fruit it was is unknown because of the layers of rot of all colours that covered it, you could eat it... but it will cost you your health... \nand who's saying you wouldn't just vomit it back up.")
        print('')
        
    elif 3 == slot2:
        storeB = 3
        print('Some old world food sat on the table, it was wrapped in some sort of foil bag, painted on the outside, and reflective on the inside,\n though it is already touched by the air, it could calm your hunger for now, but theirs not enough to last you that long')
        print('')
        
    elif 4 == slot2:
        storeB = 4
        print('There was a small can of dog food, that must have been been made before... this... happened to the world... should be safe, but not the most appetizing thing.')
        print('')

    elif 5 == slot2:
        storeB = 5
        print("They had some sort of meat roasting on a spit, the fire sitting under it should make have cleansed it of any bacteria... like the sun to it's humans...")
        print('')

    elif 6 == slot2:
        storeB = 6
        print('They had what looked to be fresh apples, untouched by the harsh environments that surrounds them')
        print('')

    #=========================================================================================
    print('')

    

 #prints the third random value for the store,
    slot3 = random.randint(1, 6)

    if 4 == slot3:
        storeC = 4
        print('In a corner of the room there was a metal can, rusted and dented, but still contained a hadful of water, clean and drinkable')   

    elif 5 == slot3:
        storeC = 5
        print('In a corner of the room there was a metal can, rusted and dented, but still contained a hadful of water, clean and drinkable')   
        
    elif 6 == slot3:
        storeC = 6
        print('On display was a metal cyclical can... perfectly formed... and reflective from all angles, filled with a liquid that not only is untouched by air, \nbut also is energizing through some sort of magic in the water. ')

    else:
        storeC = 1
        print('They had nothing that even held a drop of water')
        
    #=========================================================================================
    print('')



 #prints the fourth random value for the store
    slot4 = random.randint(1, 10)
        
        
    if 8 == slot4:
        storeD = 2
        print('[INSERT RARE WEAPON]')
        
        
    elif 9 == slot4:
        storeD = 3
        print('[INSERT RARE FOOD]')
        
        
    elif 10 == slot4:
        storeD = 4
        print('[INSERT RARE WATER]')

    else:
        storeD = 1
        print('The store had nothing unique')
        
    #=========================================================================================
    print('')

    

    return storeA, storeB, storeC, storeD



storeA, storeB, storeC, storeD = shop_randomising()

print(storeA, storeB, storeC, storeD)