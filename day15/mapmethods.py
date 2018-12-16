from unit import *
from coord import *

def printmap (area,units, highlights=[]):
    for y, row in enumerate(area):
        for x, tile in enumerate(row):
            if Coord(x,y) in highlights:
                print('+', end='')
            else:
                print(tile, end='')
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

def getemptyadjecentslist(area, coord):
    return [pos for pos in coord.getadjecents() if isempty(area, pos)]

def move(area, old, new):
    if new != None:
        area[new.y][new.x] = area[old.y][old.x]
        area[old.y][old.x] = '.'

class Node:

    def __init__(self, coord, f, g, h, parent=None):
        self.coord = coord
        self.f = f
        self.g = g
        self.h = h
        self.parent = parent
    
    def __lt__(self, other):
        return self.coord < other.coord

    def __str__(self):
        return str(self.coord) + ' parent: ' + str(self.parent)
        

def astar(area, start, goal, units):
    closedset = []
    goalnodes = []
    #open = getemptyadjecents(area, start)
    openset = [Node(start, 0, 0, 0)]
    goalcost = 100000
    while len(openset) != 0:
        openset.sort()
        current = openset.pop(0)
        for adjacent in getemptyadjecentslist(area, current.coord):

            skip = False
            g = current.g + 1
            h = manhattancc(adjacent, goal)
            f = g + h
            successor = Node(adjacent, f, g, h, current)
            if g > goalcost:
                break

            if adjacent == goal and g < goalcost:
                goalnodes = [successor]
                goalcost = g
            elif adjacent == goal and g == goalcost:
                goalnodes.append(successor)

            for opened in openset:
                if opened.coord == adjacent and opened.f < f:
                    skip = True
                    break

            for closed in closedset:
                if closed.coord == adjacent and closed.f < f:
                    skip = True
                    break
            if not skip:
                openset.append(successor)
        
        closedset.append(current)

    prev = goalnodes[0]
    node = goalnodes[0]
    highlight = [node.coord]
    while node.parent != None:
        highlight.append(node.parent.coord)
        prev = node
        node = node.parent
    #printmap(area, units, highlight)

    return prev.coord, goalnodes[0].g
#    for goal in goalnodes
 #       firststep 