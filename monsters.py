from character import Character

def create_tank_template():
    tank = Character(level = 1, 
                     R_DC=15, 
                     W_DC=15,
                     F_DC=17,
                     P_DC=15, 
                     AC=18, 
                     )
    return tank

def create_wizard_template():
    wizard = Character(level = 1,
                       R_DC=15,
                       W_DC=17,
                       F_DC=14,
                       AC=15)
    return wizard 

def create_nimble_template():
    nimble = Character(level = 1,
                      R_DC=19,
                      W_DC=18,
                      F_DC=14,
                      AC=20)
    return nimble