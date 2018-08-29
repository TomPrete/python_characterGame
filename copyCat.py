import sys
import characters





## WARRIOR CLASS
class Warrior():

  # INITIALIZE OBJECT (FUNCTION)
    def __init__(self):
      # charName = input("What's your warrior's name? ")
        charlevel = input("Input your warriors level: ")
        charstr = input("Input your warriors strength: ")
        # charVit = input("Input your warriors vitality: ")
        # charArmor = input("What kind of armor does your warrior wear? ")
        if int(charlevel) < 90 and int(charlevel) > 1 and int(charstr) > 0:
            try:
                self.level = int(charlevel)
                self.type = "warrior"
                # self.name = charName
                self.strength = int(charstr)
                # self.vitality = int(charVit)
                # self.armor = charArmor
            except: # Executes when there is a TYPE ERROR
                print("There was a Type Error! Make sure you're entering numbers when ")
                sys.exit(1)
            else:
                print('')
                print("New Warrior Created")
                print('')
        else:
            print("Level input must be between 1 and 90 and strength must be positive. Run program again.")
            sys.exit(1)
            return

  ## ATTACK OBJECT (FUNCTION)
    def attack(self):
        try:
            weapon_type = input("Input your weapon (axe, mace, or sword): ")
            mindamage = int(input("Input your weapons minimum damage: "))
            maxdamage = int(input("Input your weapons maximum damage: "))
            element_type = input("Input element type (physical, fire, cold): ")
            element_percentage = int(input("Input element percentage (between 5-15%): "))/100
            warriordata = characters.characters["warrior"]
            strpercentage = self.strength/100
            if (mindamage > maxdamage) or mindamage < 1 or maxdamage < 1 or element_percentage > .15 or (element_percentage < .05 and element_percentage > 0) or element_percentage < 0:
                # print("ERROR: One or more of your inputs are not in the correct range.")
                sys.exit(1)
            else:

                damage = [mindamage, maxdamage]
                weaponaps = 1
                for elem in warriordata["weapons"]:
                    if elem == weapon_type.lower():
                        weaponaps = warriordata["weapons"][elem]["aps"]
                print('---------| MINIMUM | MAXIMUM |   DPS   |')
                attackvalues = {}
                for attack in warriordata["attacks"]:
                    damagearr = [0, 0]
                    damagearr[0] = (round((damage[0] +(damage[0] * strpercentage)) * warriordata["attacks"][attack]["percDMG"] * 1000) /1000)
                    damagearr[1] = (round((damage[1] +(damage[1] * strpercentage)) * warriordata["attacks"][attack]["percDMG"] * 1000) / 1000)
                    if warriordata["attacks"][attack]["elem"] == element_type.lower():
                        damagearr[0] = (round((damagearr[0] +(damagearr[0] * element_percentage))* 1000) /1000)
                        damagearr[1] = (round((damagearr[1] +(damagearr[1] * element_percentage))* 1000) /1000)
                    avgdamage = ((damagearr[0] + damagearr[1]) / 2)
                    weapondps = (round((weaponaps * avgdamage * warriordata["attacks"][attack]["percAPS"]) * 1000) /1000)
                    print(" " + attack.upper() +  "   |   " + str(damagearr[0]) + "   |   " + str(damagearr[1]) + "   |   " + str(weapondps) + "   |")
                    attackvalues[attack] = {
                        'minimum': damagearr[0],
                        'maximum': damagearr[1],
                        'dps': weapondps
                    }
                attackstats = str(attackvalues)
                newfile = open('attackStatistics.py', 'w')
                newfile.write(attackstats)
        except:
            print('ERROR: Looks like one of your inputs is incorrect.')
        else:
            print("Done...")


    def levelup(self):
        if self.level == 90:
            print("Maximum Level met")
        else:
            self.level += 1
            self.strength += 10
            # self.vitality += 5
            print("New Level: ", self.level)
            print("New Strength: ", self.strength)





