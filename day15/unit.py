from abc import ABCMeta, abstractmethod
from manhattan import *

class Unit(metaclass=ABCMeta):

    def __init__(self, x, y, hp, ap, isgoblin):
        self.x = x
        self.y = y
        self.hp = hp
        self.ap = ap

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y < other.y
    
    def __eq__(self, other):
        '''Used from "in" operator'''
        print('in check')
        return self.x == other.x and self.y == other.y
    
    def iscolliding(self, other):
        '''Used for collision calculation, cant collide with itself'''
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return ' x: ' + str(self.x) + ' y: ' + str(self.y) + ' hp: ' + str(self.hp) + ' ap: ' + str(self.ap)

    def isgoblin(self):
        return False

    def iself(self):
        return False
    
    def isadjacent(self, other):
        return manhattan(self, other) == 1

    def takedamage(self, damage):
        hp -= damage

    @abstractmethod
    def attackifpossible (self, goblin, elves):
        pass

class Goblin(Unit):

    symbol = 'G'

    def gettargets(self, units):
        return [unit for unit in units if unit.iself()]

    def isgoblin(self):
        return True
        
    def attackifpossible (self, goblins, elves):
        for elf in elves:
            if self.isadjacent(elf):
                elf.takedamage(self.ap)
                return elf

class Elf(Unit):

    symbol = 'E'

    def gettargets(self, units):
        return [unit for unit in units if unit.isgoblin()]

    def iself(self):
        return True
        
    def attackifpossible (self, goblins, elves):
        for goblin in goblins:
            if self.isadjacent(goblin):
                goblin.takedamage(self.ap)
                return goblin

        
