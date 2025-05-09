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
        print(f"\n{action_type} {idx}: Success Chance: {hit}%, Critical Success Chance: {crit}%")
    
def calculate_damage_per_round(results, avg_dice_dmg, num_dice, static): 
    total_average = 0
    for strike in results: 
        hit = strike['hit'] / 100
        crit = strike['crit'] / 100
        total_average += (((avg_dice_dmg * num_dice) + static) * hit) + ((((avg_dice_dmg * num_dice) + static) * 2) * crit)
    return round(total_average, 1)

def calculate_failure_chance(defense, Spell_DC, monster):
    reflex, will, fort = monster.return_save_bonus()
    crit_success = 0
    success = 0 
    failure = 0
    crit_failure = 0 
    if defense == "reflex": 
        for i in range(1, 21):
            if i == 20 or ((i + reflex) >= Spell_DC + 10 and i != 1): 
                crit_success += 1
            elif i + reflex >= Spell_DC and i != 1: 
                success += 1 
            elif i + reflex < Spell_DC and i != 1:
                failure += 1 
            elif i == 1 or i + reflex < (Spell_DC + 10): 
                crit_failure += 1 
        crit_succ_chance = (crit_success/20) * 100  
        succ_chance = (success/20) * 100  
        fail_chance = (failure/20) * 100  
        crit_fail_chance = (crit_failure/20) * 100 
        return crit_succ_chance, succ_chance, fail_chance, crit_fail_chance
    
    elif defense == "will": 
        for i in range(1, 21):
            if i == 20 or ((i + will) >= Spell_DC + 10 and i != 1): 
                crit_success += 1
            elif i + will >= Spell_DC and i != 1: 
                success += 1 
            elif i + will < Spell_DC and i != 1:
                failure += 1 
            elif i == 1 or i + will < (Spell_DC + 10): 
                crit_failure += 1 
        crit_succ_chance = (crit_success/20) * 100  
        succ_chance = (success/20) * 100  
        fail_chance = (failure/20) * 100  
        crit_fail_chance = (crit_failure/20) * 100
        return crit_succ_chance, succ_chance, fail_chance, crit_fail_chance
    
    elif defense == "fort": 
        for i in range(1, 21):
            if i == 20 or ((i + fort) >= Spell_DC + 10 and i != 1): 
                crit_success += 1
            elif i + fort >= Spell_DC and i != 1: 
                success += 1 
            elif i + fort < Spell_DC and i != 1:
                failure += 1 
            elif i == 1 or i + fort < (Spell_DC + 10): 
                crit_failure += 1 
        crit_succ_chance = (crit_success/20) * 100  
        succ_chance = (success/20) * 100  
        fail_chance = (failure/20) * 100  
        crit_fail_chance = (crit_failure/20) * 100
        return crit_succ_chance, succ_chance, fail_chance, crit_fail_chance

 
def print_spell_result(crit_succ_chance, succ_chance, fail_chance, crit_fail_chance):
        crit_succ_chance = round(crit_succ_chance)
        succ_chance = round(succ_chance)
        fail_chance = round(fail_chance)
        crit_fail_chance = round(crit_fail_chance)
        
        print("\nSpell/effect chance per target:")
        print(f"\nCritical Success Chance: {crit_succ_chance}%, Success Chance: {succ_chance}%")
        print(f"\nFailure Chance: {fail_chance}%, Critical Failure Chance: {crit_fail_chance}%")
        print()
        
def calculate_spell_damage(crit_succ, succ, fail, num_targets, avg_dice_dmg, num_dice, static):
    crit_succ = crit_succ /100
    succ = succ/100
    fail = fail/100

    total_average = (((avg_dice_dmg * num_dice) + static) * succ) + (
        (((avg_dice_dmg * num_dice) + static) * 2) * crit_succ) + ((((avg_dice_dmg * num_dice) + static) /2) * fail)
    
    dpr = total_average * num_targets
    return round(dpr, 1) 



def print_average_damage(total_average):
    print(f"\nYour average damage per round is {total_average} ")
    print()

