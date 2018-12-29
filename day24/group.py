from math import ceil
class Group:
    
    def __init__(self, index, units, hp, attack, attacktype, initiative, 
    weaknesses, immunities, isinfection=False, isimmune=False):
        self.index = index
        self.units = units
        self.hp = hp
        self.attack = attack
        self.attacktype = attacktype
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.isinfection = isinfection
        self.isimmune = isimmune
    
    def effective(self):
        return self.attack * self.units

    def possibledamage(self, effective, attacktype):
        
        if attacktype in self.immunities:
            damage = 0
        elif attacktype in self.weaknesses:
            damage = effective * 2
        else:
            damage = effective
        #print (damage, 'damage potentially taken by', self.index)
        return damage
    
    def takedamage(self, effective, attacktype):
        if attacktype in self.immunities:
            print("This shouldn't happen!")
        elif attacktype in self.weaknesses:
            damage = effective * 2
        else:
            damage = effective
        #print('units dead', damage, int(damage/self.hp))
        #print('before', self.units, 'remaining units', ceil((self.units * self.hp - damage) / self.hp))
        self.units = ceil((self.units * self.hp - damage) / self.hp)
        return int(damage/self.hp)
        
    