import sys
from copyCat import Warrior


# EXECUTES THE PROGRAM

def startsys():
    userinput = input("--Do you want to calculate attack statistics for the Warrior Character Type? (y/n) ")
    if userinput[0].lower() == 'y':
        print('------------------------------------------------------------')
        print('--------------------  WELCOME NEW WARRIOR  -----------------')
        print('------------------------------------------------------------')
        print('')
        print('')
        print("--First we need to create a new Warrior.")
        print('')
        print('')
        new = Warrior()
        print("--Now we can start calculating the attack statistics.")
        new.attack()
        levelup = input("--Do you want to level up?! (y/n) ")
        if levelup[0].lower() == 'y':
            new.levelup()
        gamestatus = input("--Do you want to continue? (y/n) ")
        if gamestatus[0].lower() == 'n':
            print("--Have a great day!")
            sys.exit(1)
        if gamestatus[0].lower() == 'y':
            newgame = input("--Do you want to create a new Warrior? (y/n) ")
            if newgame[0].lower() == 'n':
                new.attack()
            else:
                startsys()
    else:
        print("--Sorry, no other Character Types exist at this time. But we're working on creatying more!")


startsys()
