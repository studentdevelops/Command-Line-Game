import random

from classes.game import person

class spell(object):
    
    def __init__(self, name , dmg, cost, tpe):
        self.name = name
        self.dmg = dmg
        self.cost = cost
        self.tpe = tpe

    def spell_dmg(self):
        dmgl = self.dmg - 5
        dmgh = self.dmg + 5
        return random.randrange(dmgl, dmgh)
        

    def spell_cost(self):
        return self.cost
