import character
from monsters import *


def get_character_level():
    while True:
        try:
            level = int(input("\nEnter character level(1-20): "))
            if 1 <= level <= 20:
                return level
            else:
                print("Level must be between 1-20")
        except:
            print("Please enter a valid number.")

def get_character_ability_mod():
    while True: 
        try:
            ability_mod = int(input("Enter ability modifier: "))
            if -5 <= ability_mod <= 10:
                return ability_mod
            else: 
                print("Ability modifier should typically be between -5 and 10.")
                confirm = input("Use this value anyway? y/n: ")
                if confirm.lower() == 'y':
                    return ability_mod
        except ValueError:
            print("Please enter a valid number.")

def get_proficiency_input():
    
    print("\nSelect proficiency rank:")
    print("1. Untrained")
    print("2. Trained")
    print("3. Expert")
    print("4. Master")
    print("5. Legendary")
    
    while True:
        try:
            choice = int(input("Enter choice (1-5): "))
            if 1 <= choice <= 5:
                ranks = ["untrained", "trained", "expert", "master", "legendary"]
                return ranks[choice - 1]
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

def get_item_bonus():
    
    while True:
        try:
            item_bonus = int(input("Enter item bonus: "))
            return item_bonus
        except ValueError:
            print("Please enter a valid number.")

def get_attack_bonus_choice():
    print("\nWould you like to:")
    print("1. Calculate your bonus")
    print("2. Input your bonus directly")
    
    while True:
        try:
            choice = int(input("Enter choice (1-2): "))
            if choice == 1:
                return "calculate"
            elif choice == 2:
                return "input"
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

def get_direct_attack_bonus():
    while True:
        try:
            bonus = int(input("\nEnter your bonus:+ "))
            return bonus
        except ValueError:
            print("Please enter a valid number.")

def get_attack_bonus(): 
    level = get_character_level()
    choice = get_attack_bonus_choice()
    if choice == "calculate":
        ability_mod = get_character_ability_mod()
        proficiency = get_proficiency_input()
        item_bonus = get_item_bonus()
        
        character = Character(level, ability_mod, proficiency, item_bonus)
        return character.attack_bonus(ability_mod,proficiency,item_bonus), level 
    else: 
        return get_direct_attack_bonus(), level 
    
def get_monster_type(level):
    print("\nWhat type of monster(s) would you like to test against?")
    print("1. A tanky/brutish monster")
    print("2. An arcane/caster monster")
    print("3. A nimble monster")

    while True:
        try: 
            choice = int(input("Enter your choice: "))
            if choice == 1: 
                monster = create_tank_template()
                monster.scale_to_level_tank(level)
                threat = get_threat_level()
                print(f"\nA level {level} tank monster appears!")
                return monster, threat
            
            elif choice == 2:
                monster = create_wizard_template()
                monster.scale_to_level_wizard(level)
                threat = get_threat_level()
                print(f"\nA level {level} arcane monster appears!")
                return monster, threat 
            
            elif choice == 3:
                monster = create_nimble_template()
                monster.scale_to_level_nimble(level)
                threat = get_threat_level()
                print(f"\nA level {level} nimble monster appears!")
                return monster, threat 

        except ValueError:
            print("Please choose valid monster type!")

def get_maneuver_type():
    print("\nWhat type of action are you attempting?")
    print("1. Strike/Spell Attack (rolls against AC)")
    print("2. Trip/Disarm (rolls against Reflex DC)")
    print("3. Demoralize (rolls against Will DC")
    print("4. Feint (rolls against Perception DC)")
    print("5. Athletic maneuver(rolls against Fortitude DC)")
    print("6. Effect requiring a saving throw that does damage")
    print("7. Effect requiring a saving throw with no damage")
    
    while True:
        try:
            choice = int(input("Enter your choice(1-7)"))
            if choice == 1:
                return "Strike/Spell Attack", "AC", True
            elif choice == 2:
                return "Athletics", "Reflex", True 
            elif choice == 3:
                return "Intimidate", "Will", True
            elif choice == 4:
                return "Deception", "Perception", True 
            elif choice == 5: 
                return "Athletics", "Fortitude", True 
            elif choice == 6: 
                return "Spell effect", "Spell DC", False 
            elif choice == 7:
                return "Spell effect no damage", "Spell DC", False 
            else: 
                print("Please choose a valid maneuver")
        except ValueError:
            print("Please enter a valid number.")

def get_number_of_targets():
    while True: 
        try:
            num_targets = int(input("\nHow many opponents are you targeting: "))
            if num_targets >= 1: 
                return num_targets
        except ValueError:
            print("Please enter a valid number.")

def get_defense_type():
    print("\nWhat type of save is the monster(s) making?")
    print("1. Reflex. ")
    print("2. Will. ")
    print("3. Fortitude. ")

    while True: 
        try:
            choice = int(input("Please choose one of the following(1-3) "))
            if choice == 1: 
                return "reflex"
            elif choice == 2:
                return "will"
            elif choice == 3:
                return "fort"
        except ValueError:
            print("Please choose a valid option.")


def get_number_of_strikes():
    while True:
        try:
            num_strikes = int(input("\nHow many strikes will you make? (1-3): "))
            if 1 <= num_strikes <= 3:
                return num_strikes
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def get_multiple_attack_penalty(): 
    
    while True:
        try:
            value = int(input("\nWhat is your multiple attack penalty(Enter a positive integer) ?"))
            if value >= 0:
                return value
        except ValueError:
            print("Please enter a valid number.")

def get_threat_level():
    print("\nChoose an appropriate threat level for the monster.")
    print("1. Below level -1.")
    print("2. Standard +0.")
    print("3. Low +1.")
    print("4. Moderate +2.")
    print("5. Extreme +3.")

    while True:
        try: 
            choice = int(input("Please select monster threat level(1-5) "))
            if choice == 1:
                return "Below_level"
            elif choice == 2:
                return "Standard"
            elif choice == 3:
                return "Low"
            elif choice == 4:
                return "Moderate"
            elif choice == 5:
                return "Extreme"
            else:
                print("Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def get_off_guard(monster):
    print("\nIs the target off guard?")
    print("1. Yes.")
    print("2. No.")
    while True:
        try:
            choice = int(input("Please select one of the above(1-2): "))
            if choice == 1:
                monster.apply_off_guard()
            elif choice == 2:
                return
            else:  
                print("Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number. ")

def get_status_penalty():
    print("\nDoes the target have any relevant status penalties?")
    print("1. Yes.")
    print("2. No.")
    while True: 
        try: 
            choice = int(input("Please select one of the above(1-2): "))
            if choice == 1:
                value = int(input("\nPlease enter the value of the status penalty: "))
                return value
            elif choice == 2:
                return 0
            else: 
                print("Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number. ")
    
def get_damage_dice():
    print("\nWhat size damage dice does your character use?")
    print("1. D4.")
    print("2. D6.")
    print("3. D8.")
    print("4. D10.")
    print("5. D12.")
    while True: 
        try:
            choice = int(input("Please select one of the above (1-5): "))
            if choice == 1:
                return 2.5
            elif choice == 2:
                return 3.5
            elif choice == 3: 
                return 4.5 
            elif choice == 4:
                return 5.5
            elif choice == 5:
                return 6.5 
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Please select a valid option.")
    
def get_num_damage_die():
    print("\nHow many damage die does your character roll?")
    while True:
        try: 
            value = int(input("Enter number of damage die: "))
            if value >= 1:
                return value 
            else:
                print("Please enter a valid number.")
    
        except ValueError:
            print("Please enter a valid number.")

def get_spell_DC():
    while True:
        try: 
            value = int(input("\nPlease enter your spell DC: "))
            if value >= 10:
                return value
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def get_static_damage():
    print("\nDoes your character have any static bonuses to damage?")
    print("1. Yes.")
    print("2. No.")
    while True:
        try:
            choice = int(input("Please choose one of the following(1-2): "))
            if choice == 1:
                value = int(input("Enter your static damage bonus: "))
                return value 
            elif choice == 2:
                return 0
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Please choose a valid option.")
        