from character import Character

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
            bonus = int(input("\nEnter your bonus: +"))
            return bonus
        except ValueError:
            print("Please enter a valid number.")

def get_attack_bonus(): 
    choice = get_attack_bonus_choice()
    if choice == "calculate":
        level = get_character_level()
        ability_mod = get_character_ability_mod()
        proficiency = get_proficiency_input()
        item_bonus = get_item_bonus()
        
        character = Character(level, ability_mod, proficiency, item_bonus)
        return character.attack_bonus(ability_mod,proficiency,item_bonus)
    else: 
        return get_direct_attack_bonus()