import character
from monsters import *


def get_character_level():
    while True:
        try:
            level = int(input("Enter character level(1-20): "))
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
    print("What type of monster(s) would you like to test against?")
    print("1. A tanky/brutish monster")

    while True:
        try: 
            choice = int(input("Enter your choice: "))
            if choice == 1: 
                monster = create_tank_template()
                monster.scale_to_level_tank(level)
                print(f"A level {level} tank monster appears!")
                return monster
            
        except ValueError:
            print("Please choose valid monster type!")

def get_maneuver_type():
    print("\nWhat type of maneuver are you attempting?")
    print("1. Strike/Spell Attack (rolls against AC)")
    print("2. Trip (rolls against Reflex DC)")
    print("3. Demoralize (rolls against Will DC")
    print("4. Feint (rolls against Perception DC)")
    print("5 Athletic maneuver(rolls against Fortitude DC)")
    
    while True:
        try:
            choice = int(input("Enter your choice(1-5)"))
            if choice == 1:
                return "Strike/Spell Attack", "AC", True
            elif choice == 2:
                return "Athletics", "Reflex", False
            elif choice == 3:
                return "Intimidate", "Will", False
            elif choice == 4:
                return "Deception", "Perception DC", False
            elif choice == 5: 
                return "Athletics", "Fortitude DC", False 
            else: 
                print("Please choose a valid maneuver")
        except ValueError:
            print("Please enter a valid number.")


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
    print("\nChoose your Multiple Attack Penalty progression:")
    print("1. Standard (-5/-10)")
    print("2. Agile Weapon (-4/-8)")
    print("3. Reduced MAP (-3/-6)")
    print("4. No MAP")
    
    
    while True:
        try:
            choice = int(input("What is your multiple attack penalty(1-3) ?"))
            if choice == 1: 
                return -5
            elif choice == 2:
                return -4
            elif choice == 3:
                return -3
            elif choice == 4:
                return 0
            else:
                print("Please choose valid number.")
        except ValueError:
            print("Please enter a valid number.")

