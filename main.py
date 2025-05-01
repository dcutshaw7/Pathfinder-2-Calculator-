from character import Character
from user_inputs import *
from calculations import *

def main():
    print("PF2 Calculator V1")
    action_type, defense_type, damage_relevant = get_maneuver_type()
    attack_bonus, level = get_attack_bonus()
    monster = get_monster_type(level)
    num_attacks = 1 
    if action_type == "Strike/Spell Attack":
        num_attacks = get_number_of_strikes()
        MAP_pen = get_multiple_attack_penalty()
    results = calculate_success_chance(attack_bonus, monster, defense_type, num_attacks, MAP_pen)
    print_results_in_english(results)












if __name__ == "__main__":
    main()
            
