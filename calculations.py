import character 
import monsters

def calculate_success_chance(attack_bonus, monster, defense_type, num_strikes, MAP_pen):
    defense = get_target_value(monster, defense_type)
    results = []
    
    for strike in range(num_strikes):
        if strike == 0:
            penalty = 0
        elif strike == 1:
            penalty = MAP_pen
        else:
            penalty = MAP_pen * 2
    
        current_bonus = attack_bonus - penalty 
        crits = 0 
        hits = 0 
        for i in range(1, 21):
            if i == 20 or ((i + current_bonus) >= defense + 10 and i != 1): 
                hits += 1
                crits += 1
            elif i + current_bonus >= defense and i != 1: 
                hits += 1 
        hit_chance = round(hits/20 * 100)
        crit_chance = round(crits/20 * 100)
        results.append({'hit': hit_chance, 'crit': crit_chance})
    return results 

def get_target_value(monster, defense_type):
    
    if defense_type == "AC":
        return monster.AC
    elif defense_type == "Reflex":
        return monster.R_DC
    elif defense_type == "Will":
        return monster.W_DC
    elif defense_type == "Perception":
        return monster.P_DC
    elif defense_type == "Fortitude":
        return monster.F_DC
    else:
        raise ValueError(f"Unknown defense type: {defense_type}")


        
def print_results_in_english(results, action_type):
    for idx, outcome in enumerate(results, start=1):
        hit = round(outcome['hit'])
        crit = round(outcome['crit'])
        print(f"\n{action_type} {idx}: Hit Chance: {hit}%, Crit Chance: {crit}%")
    


