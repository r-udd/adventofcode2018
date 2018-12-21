from unit import *
from coord import *

def printmap (area,units, highlights=[], xspot=Coord(-1,-1)):
    for y, row in enumerate(area):
        for x, tile in enumerate(row):
            c = Coord(x,y)
            if c == xspot:
                print('X', end='')
            elif c in highlights:
                print('+', end='')
            else:
                print(tile, end='')
        print(end=' ')
        for unit in units:
            if unit.coord.y == y:
                print(unit, end=', ')
        print()
    print('\n')

def readmap (filename):
    area = []
    units = []
    goblins = []
    elves = []
    with open(filename) as f:
        for y, line in enumerate(f):
            arealine = []
            for x, char in enumerate(line):
                if char == '\n':
                    continue
                if char == 'G':
                    goblin = Goblin(Coord(x,y), 200, 3, True)
                    units.append(goblin)
                    goblins.append(goblin)
                elif char == 'E':
                    elf = Elf(Coord(x,y), 200, 3, False)
                    units.append(elf)
                    elves.append(elf)
                arealine.append(char)
            area.append(arealine)
    return area, units, elves, goblins

def isempty(area, coord):
    return area[coord.y][coord.x] == '.'

def getemptyadjecentsset(area, coord):
    return {pos for pos in coord.getadjecents() if isempty(area, pos)}

def getemptyclosecoordadjecents(area, attacker, target):
    return [pos for pos in target.getclosecoordadjecents(attacker) if isempty(area, pos)]

def getemptyadjecentslist(area, coord):
    return [pos for pos in coord.getadjecents() if isempty(area, pos)]

def move(area, old, new):
    if new != None:
        area[new.y][new.x] = area[old.y][old.x]
        area[old.y][old.x] = '.'

def removefrommap(area, coord):
    area[coord.y][coord.x] = '.'

class Node:

    def __init__(self, coord, cost, parent=None, firststep=None):
        self.coord = coord
        self.cost = cost
        self.parent = parent
    
    def __lt__(self, other):
        return self.cost < other.cost or (self.cost == other.cost and self.coord < other.coord)
        #return self.coord < other.coord
    
    def __eq__(self,other):
        return other != None and self.coord == other.coord

    def __str__(self):
        return str(self.coord) + ' parent: ' + str(self.parent)
        

def bfsearch(area, start, goals, units):
    closedset = []
    #open = getemptyadjecents(area, start)
    openset = [Node(start, 0)]
    foundgoals = []
    anyfound = False
    foundcost = 0
    while len(openset) != 0:
        #openset.sort()
        current = openset.pop(0)
        closedset.append(current)

        for adjacent in getemptyadjecentslist(area, current.coord):
            
            cost = current.cost + 1
            successor = Node(adjacent, cost, current)
            if successor in closedset:
                continue
            if anyfound and cost > foundcost:
                closedset.append(successor)
                continue
            elif anyfound and cost < foundcost:
                print('THIS SHOULD NOT HAPPEN')
            elif adjacent in goals:
                anyfound = True
                foundcost = successor.cost
                #closedset.append(successor)
                foundgoals.append(successor)
                '''elif successor in closedset:
                index = closedset.index(successor)
                if cost < closedset[index].cost:
                    closedset[index] = successor
                continue'''
            elif successor not in openset:
                openset.append(successor)
        '''if start.x == 22 and start.y == 13:
            printmap(area, units, [c.coord for c in closedset+openset], start)
        if found:
            anyfound = True
            node = successor
            highlight = []
            while node.cost != 1:
                highlight.append(node.coord)
                node = node.parent
            printmap(area, units, highlight, successor.coord)
            

            return node.coord'''
    if anyfound:
        foundgoals.sort()
        node = foundgoals[0]
        highlight = []

        while node.cost != 1:
            highlight.append(node.coord)
            node = node.parent
        return node.coord
    #    for goal in goalnodes
    #       firststep 
    return None