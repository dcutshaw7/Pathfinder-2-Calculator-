from character import Character
from user_inputs import *
from calculations import *

def main():
    print("PF2 Success Calculator V1")
    action_type, defense_type, bool = get_maneuver_type()
    if bool == True: 
        attack_bonus, level = get_attack_bonus()
        monster, threat = get_monster_type(level)
        monster.threat_level_scale(threat)
        stat_value = get_status_penalty()
        monster.apply_status_penalty(stat_value)
        num_attacks = 1 
        MAP_pen = 0
        if action_type == "Strike/Spell Attack":
            get_off_guard(monster)
            num_attacks = get_number_of_strikes()
            MAP_pen = get_multiple_attack_penalty()
            avg_dice_dmg = get_damage_dice()
            num_damage_die = get_num_damage_die()
            static = get_static_damage()
        results = calculate_success_chance(attack_bonus, monster, defense_type, num_attacks, MAP_pen)
        print_results_in_english(results, action_type)
        if action_type == "Strike/Spell Attack":
            dpr = calculate_damage_per_round(results, avg_dice_dmg, num_damage_die, static)
            print_average_damage(dpr)
    if bool == False: 
        level = get_character_level()
        defense = get_defense_type()
        spell_DC = get_spell_DC()    
        num_targets = get_number_of_targets()
        if action_type == "Spell effect":
            avg_dice_dmg = get_damage_dice()
            num_damage_die = get_num_damage_die()
            static = get_static_damage()
        monster, threat = get_monster_type(level)
        stat_value = get_status_penalty()
        monster.apply_status_penalty(stat_value)
        crit_succ, succ, fail, crit_fail = calculate_failure_chance(defense, spell_DC, monster)
        print_spell_result(crit_succ, succ, fail, crit_fail)
        if action_type == "Spell effect":
            dpr = calculate_spell_damage(crit_succ, succ, fail, num_targets, avg_dice_dmg, num_damage_die, static)
            print_average_damage(dpr)
        


    
    












if __name__ == "__main__":
    main()
            
