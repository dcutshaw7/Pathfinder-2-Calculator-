from character import Character

def create_tank_template():
    tank = Character(level = 1, 
                     ability_mod=4,
                     R_DC=15, 
                     W_DC=15,
                     F_DC=17,
                     P_DC=15, 
                     AC=18, 
                     damage_die=10, 
                     num_die=1)
    return tank