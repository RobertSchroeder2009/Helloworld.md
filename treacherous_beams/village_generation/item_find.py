import random, time 

def shop_randomising():

    #prints the first random value for the store
    slot1 = random.randint(1, 6)
    if 1 == slot1:
        storeA = 1
        print('Their first item was a rusty sheet of metal that looks like its has been cut to be some kind of sword')

    elif 2 == slot1:
        storeA = 2
        print('Their first item was a old shattered sword')

    elif 3 == slot1:
        storeA = 3
        print('Their first item was a worn out [insert medium quality weapon]')
        
    elif 4 == slot1:
        storeA = 4
        print('Their first item was a [high quality weapon]')
        
    elif 5 == slot1:
        storeA = 5
        print('Their first item was a pristine sword that must have been crafted back in the old world')

    elif 6 == slot1:
        storeA = 6
        print('The store was missing anything that could be used as a weapon')

    else:
        print('error')


    #prints the second random value for the store
    slot2 = random.randint(1, 6)
    if 1 == slot2:
        storeB = 1
        print('The store had nothing that was edible')

    elif 2 == slot2:
        storeB = 2
        print('There was a rotten fruit on a table, what fruit it was is unknown because of the layers of green and black rot that covered it, you could eat it... but it will cost you your health')
        
    elif 3 == slot2:
        storeB = 3
        print('')
        
    elif 4 == slot2:
        storeB = 4
        print('There was a small can of dog food, that must have been been made before... this... happened to the world')

    elif 5 == slot2:
        storeB = 5
        print('They had some sort of meat roasting of a spit')

    elif 6 == slot2:
        storeB = 6
        print('They had what looked to be fresh apples, untouched by the harsh environments that surrounds them')
    
    else:
        print('error')

    #prints the third random value for the store
    slot3 = random.randint(1, 5)
    if 1 == slot3:
        storeC = 1

    elif 2 == slot3:
        storeC = 2
        
    elif 3 == slot3:
        storeC = 3
        
    elif 4 == slot3:
        storeC = 4
        
    elif 5 == slot3:
        storeC = 5
    else:
        print('error')

        #prints the fourth random value for the store
    slot4 = random.randint(1, 5)
    if 1 == slot4:
        storeD = 1

    elif 2 == slot4:
        storeD = 2
        
    elif 3 == slot4:
        storeD = 3
        
    elif 4 == slot4:
        storeD = 4
        
    elif 5 == slot4:
        storeD = 5
    else:
        print('error')
    
        #prints the fifth random value for the store
    slot5 = random.randint(1, 5)
    if 1 == slot5:
        storeE = 1

    elif 2 == slot5:
        storeE = 2
        
    elif 3 == slot5:
        storeE = 3
        
    elif 4 == slot5:
        storeE = 4
        
    elif 5 == slot5:
        storeE = 5
    else:
        print('error')
    
    return storeA, storeB, storeC, storeD, storeE



storeA, storeB, storeC, storeD, storeE = shop_randomising()

print(storeA, storeB, storeC, storeD, storeE)