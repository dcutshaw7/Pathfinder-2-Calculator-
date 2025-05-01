import character 
import monsters

def calculate_success_chance(attack_bonus, monster, defense_type, num_strikes, MAP_pen):
    defense = get_target_value(monster, defense_type)
    results = []
    
    if defense_type == "AC":
        
        for i in range(min(3, num_strikes)):
            
            current_penalty = 0 if i == 0 else MAP_pen if i == 1 else MAP_pen * 2
            effective_bonus = attack_bonus - current_penalty
            target_number = defense - effective_bonus
            auto_crit = 0.05
            auto_miss = 0.05

            std_crit_chance = max(0, min(0.90, (21 - (target_number + 10)) / 20)) - auto_crit
            std_hit_chance = max(0, min(0.90, (21 - target_number) / 20)) - std_crit_chance - auto_crit
            crit_chance = std_crit_chance + auto_crit
            hit_chance = std_hit_chance
            miss_chance = 1 - (hit_chance + crit_chance)

            results.append({
                "attack_number": i + 1,
                "crit_chance": crit_chance * 100,
                "hit_chance": hit_chance * 100,
                "miss_chance": miss_chance * 100,
                "total_chance": (crit_chance + hit_chance) * 100
            })
        
        return results
        
    else:
        auto_crit = 0.05   
        auto_miss = 0.05 
        
        target_number = defense - attack_bonus
        std_crit_chance = max(0, min(0.90, (21 - (target_number + 10)) / 20)) - auto_crit
        std_hit_chance = max(0, min(0.90, (21 - target_number) / 20)) - std_crit_chance - auto_crit
        
        crit_chance = std_crit_chance + auto_crit
        hit_chance = std_hit_chance
        miss_chance = 1 - (crit_chance + hit_chance)

        results.append({
                "attack_number": 1,
                "crit_chance": crit_chance * 100,
                "hit_chance": hit_chance * 100,
                "miss_chance": miss_chance * 100,
                "total_chance": (crit_chance + hit_chance) * 100
            })
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

def print_results_in_english(results, defense_type):
    print(f"Results for {defense_type} check:")

    for attack in results: 
        attack_num = attack["attack_number"]
        crit = round(attack["crit_chance"])
        hit = round(attack["hit_chance"])
        miss = round(attack["miss_chance"])
        total = round(attack["total_chance"])

        if attack_num == 1:
            attack_des = "Your first attack/maneuver"
        if attack_num == 2:
            attack_des = "Your second attack"
        if attack_num == 3:
            attack_des = "Your third attack"
        
def print_results_in_english(results):
    
    for result in results:
        attack_num = result["attack_number"]
        crit = round(result["crit_chance"])        
        hit = round(result["hit_chance"])
        miss = round(result["miss_chance"])
        
        
        if attack_num == 1:
            attack_desc = "Your first attack"
        elif attack_num == 2:
            attack_desc = "Your second attack"
        else:
            attack_desc = "Your third attack"
            
        print()
        print(f"{attack_desc} has a: ")
        
        print(f"  • {crit}% chance to critically hit")
        print(f"  • {hit}% chance to hit")
        print(f"  • {miss}% chance to miss")
        print() 


