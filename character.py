

class Character: 
    def __init__(self, level=0, ability_mod=0, proficiency=0, 
    item_bonus=0, R_DC=0, W_DC=0, F_DC=0, P_DC=0, AC=10, damage_die=0, num_die=0, actions=3):
        self.level = level 
        self.ability_mod = ability_mod
        self.proficiency = proficiency
        self.item_bonus = item_bonus
        self.R_DC = R_DC
        self.W_DC = W_DC
        self.F_DC = F_DC
        self.P_DC = P_DC 
        self.AC = AC 
        self.damage_die = damage_die
        self.num_die = num_die
        self.actions = 3

    def apply_quickened(self):
        self.actions = 4 

    def get_proficiency_rank(self, proficiency):
        if proficiency == 1:
            return 0
        elif proficiency == 2:
            return 2 + self.level 
        elif proficiency == 3:
            return 4 + self.level 
        elif proficiency == 4:
            return 6 + self.level 
        elif proficiency == 5:
            return 8 + self.level 
        else:
            raise ValueError(f"Invalid proficiency rank {proficiency}")
    
    def attack_bonus(self, proficiency, ability_mod, item_bonus=0):
        prof_bonus = self.get_proficiency_rank(proficiency)
        return self.item_bonus + prof_bonus + self.ability_mod

    def scale_to_level_tank(self, target_level):
        self.level = target_level
        if target_level >= 5: 
            self.num_die += 1
            self.F_DC += 2 
            self.W_DC += 2 
            self.P_DC += 2 
        if target_level >= 10: 
            self.num_die += 1
            self.F_DC += 2
            self.W_DC += 2
            self.P_DC += 2
            self.AC += 2 
        if target_level >= 15:
            self.num_die +=1 
            self.F_DC += 2
            self.W_DC += 2 
            self.P_DC += 0
            self.AC += 4
        if target_level >= 20:
            self.num_die += 1
            self.F_DC += 2
            self.W_DC += 2
            self.R_DC += 2
            self.P_DC += 2
            self.AC += 2

