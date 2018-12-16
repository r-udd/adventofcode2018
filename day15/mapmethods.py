from unit import *

def printmap (area,units):
    for y, row in enumerate(area):
        for x,tile in enumerate(row):
            for unit in units:
                if unit.x == x and unit.y == y:
                    print(unit.symbol, end='')
                    break
            else:
                print(tile, end='')
        print()
    print('\n')

def readmap ():
    area = []
    units = []
    goblins = []
    elves = []
    with open('day15/testA') as f:
        for y, line in enumerate(f):
            arealine = []
            for x, char in enumerate(line):
                if char == '\n':
                    continue
                if char == 'G':
                    goblin = Goblin(x,y, 200, 3, True)
                    units.append(goblin)
                    goblins.append(goblin)
                    arealine.append('.')
                elif char == 'E':
                    elf = Elf(x,y, 200, 3, False)
                    units.append(elf)
                    elves.append(elf)
                    arealine.append('.')
                else:
                    arealine.append(char)
            area.append(arealine)
    return area, units, elves, goblins