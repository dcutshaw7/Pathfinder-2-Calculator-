

class Character: 
    def __init__(self, level=0, ability_mod=0, proficiency=0, 
    item_bonus=0, R_DC=0, W_DC=0, F_DC=0, P_DC=0, AC=10):
        self.level = level 
        self.ability_mod = ability_mod
        self.proficiency = proficiency
        self.item_bonus = item_bonus
        self.R_DC = R_DC
        self.W_DC = W_DC
        self.F_DC = F_DC
        self.P_DC = P_DC 
        self.AC = AC 
        self.off_guard = False 
        self.reflex = 0
        self.will = 0 
        self.fort = 0 

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

    def scale_to_level(self, target_level):
        self.level = target_level - self.level 
        self.R_DC += self.level 
        self.W_DC += self.level 
        self.F_DC += self.level 
        self.P_DC += self.level 
        self.AC += self.level

    def threat_level_scale(self, threat):
        if threat == "Below_level":
            self.R_DC -= 1
            self.W_DC -= 1
            self.F_DC -= 1
            self.P_DC -= 1
            self.AC -= 1
        elif threat == "Standard":
            return
        elif threat == "Low":
            self.R_DC += 1
            self.W_DC += 1
            self.F_DC += 1
            self.P_DC += 1
            self.AC += 1
        elif threat == "Moderate": 
            self.R_DC += 2
            self.W_DC += 2
            self.F_DC += 2
            self.P_DC += 2
            self.AC += 2
        else: 
            self.R_DC += 3
            self.W_DC += 3
            self.F_DC += 3
            self.P_DC += 3
            self.AC += 3

        
    
    def scale_to_level_tank(self, target_level):
        self.scale_to_level(target_level)
        
        if target_level >= 5: 
            
            self.F_DC += 2 
            self.W_DC += 2 
            self.P_DC += 2 
        if target_level >= 10: 
            
            self.F_DC += 2
            self.W_DC += 2
            self.P_DC += 2
            self.AC += 2 
        if target_level >= 15:
            
            self.F_DC += 2
            self.W_DC += 2 
            self.P_DC += 0
            self.AC += 4
        if target_level >= 20:
            
            self.F_DC += 2
            self.W_DC += 2
            self.R_DC += 2
            self.P_DC += 2
            self.AC += 2

    def apply_off_guard(self):
        if not self.off_guard: 
            self.AC -= 2
            self.off_guard = True 

    def apply_status_penalty(self, value):
            self.R_DC -= value
            self.W_DC -= value
            self.F_DC -= value
            self.P_DC -= value
            self.AC -= value
    
    def return_save_bonus(self): 
        reflex = self.R_DC - 10 
        will = self.W_DC - 10 
        fort = self.F_DC - 10 
        return reflex, will, fort 
    
    def scale_to_level_wizard(self, target_level):
        self.scale_to_level(target_level)
        
        if target_level >= 5: 
            
            self.F_DC += 0
            self.R_DC += 2
            self.W_DC += 2 
            self.P_DC += 0 
        if target_level >= 10: 
            self.R_DC += 0
            self.F_DC += 2
            self.W_DC += 2
            self.P_DC += 2
            self.AC += 0
        if target_level >= 15:
            self.R_DC += 0
            self.F_DC += 0
            self.W_DC += 4
            self.P_DC += 0
            self.AC += 2
        if target_level >= 20:
            
            self.F_DC += 2
            self.W_DC += 2
            self.R_DC += 2
            self.P_DC += 2
            self.AC += 0

    def scale_to_level_nimble(self, target_level):
        self.scale_to_level(target_level)
        
        if target_level >= 5: 
            
            self.F_DC += 0
            self.R_DC += 2
            self.W_DC += 2 
            self.P_DC += 2 
        if target_level >= 10: 
            self.R_DC += 2
            self.F_DC += 2
            self.W_DC += 0
            self.P_DC += 0
            self.AC += 2
        if target_level >= 15:
            self.R_DC += 2
            self.F_DC += 0
            self.W_DC += 0
            self.P_DC += 0
            self.AC += 4
        if target_level >= 20:
            
            self.F_DC += 0
            self.W_DC += 2
            self.R_DC += 2
            self.P_DC += 2
            self.AC += 2