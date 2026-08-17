
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
RESET = "\033[0m"  

import random, time 
Sty = ""
options = ["1", "2", "3"]
travel = False

def visit():
    print('What do you want to visit?')
    Sty = input("")
    print('')

    while Sty not in options:
       print(f"{RED}Please enter a valid number{RESET}")
       Sty = input("")

    if '1' in Sty:
        travel = 1

    elif '2' in Sty:
        travel = 2

    elif '3' in Sty:
        travel = 3

    return travel

#HOW TO CALL ON CODE
# [NEW_VALUE_NAME] = visit()