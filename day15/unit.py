from abc import ABCMeta, abstractmethod
from manhattan import *
from coord import *

class Unit(metaclass=ABCMeta):

    def __init__(self, coord, hp, ap, isgoblin):
        self.coord = coord
        self.hp = hp
        self.ap = ap

    def __lt__(self, other):
        return self.coord < other.coord
    
    '''def __eq__(self, other):
        "Used from "in" operator"
        print('in check')
        return self.x == other.x and self.y == other.y'''
    
    '''def iscolliding(self, other):
        "Used for collision calculation, cant collide with itself"
        return self.x == other.x and self.y == other.y'''

    def __str__(self):
        return self.symbol + '(' + str(self.hp) + ')'
        #return ' x: ' + str(self.coord.x) + ' y: ' + str(self.coord.y) + ' hp: ' + str(self.hp) + ' ap: ' + str(self.ap)

    def isgoblin(self):
        return False

    def iself(self):
        return False
    
    def isadjacent(self, other):
        return manhattanuu(self, other) == 1

    def takedamage(self, damage):
        self.hp -= damage

    @abstractmethod
    def attackifpossible (self, area, units, goblins, elves):
        raise NotImplementedError('subclasses must override attackifpossible()!')

    @abstractmethod
    def gettargets (self, units, dead):
        raise NotImplementedError('subclasses must override gettargets()!')

class Goblin(Unit):

    symbol = 'G'

    def gettargets(self, units, dead):
        return [unit for unit in units if unit.iself() and unit not in dead]

    def isgoblin(self):
        return True
        
    def attackifpossible (self, area, units, dead):
        target = None
        coords = self.coord.getadjecents()
        elves = [unit for unit in units if unit.iself() and unit.coord in coords and unit not in dead]
        for elf in elves:
            if target == None:
                target = elf
            elif elf.hp < target.hp:
                target = elf
            elif elf.hp == target.hp and elf.coord < target.coord:
                target = elf
        if target != None:
            target.takedamage(self.ap)
        return target

class Elf(Unit):

    symbol = 'E'

    def gettargets(self, units, dead):
        return [unit for unit in units if unit.isgoblin() and unit not in dead]

    def iself(self):
        return True
        
    def attackifpossible (self, area, units, dead):
        target = None
        coords = self.coord.getadjecents()
        goblins = [unit for unit in units if unit.isgoblin() and unit.coord in coords and unit not in dead]
        for goblin in goblins:
            if target == None:
                target = goblin
            elif goblin.hp < target.hp:
                target = goblin
            elif goblin.hp == target.hp and goblin.coord < target.coord:
                target = goblin
        if target != None:
            target.takedamage(self.ap)
        return target
