from unit import *
from mapmethods import *
from manhattan import *

area, units, elves, goblins = readmap('day15/testJ.2')
printmap(area, units,[])
gameover = False
roundno = 0
while not gameover:
    
    units.sort()
    elves.sort()
    goblins.sort()
    dead = []
    for unit in units:
        if unit in dead:
            break
        attackedunit = unit.attackifpossible(area, units, goblins,  elves)
        if attackedunit != None and attackedunit.hp <= 0:
            dead.append(attackedunit)
        goalpositions = []
        if attackedunit == None:

            targets = unit.gettargets(units, dead)
            if len(targets) == 0:
                gameover = True
                break

            for target in targets:
                goalpositions += getemptyadjecentsset(area, target.coord)
            
            nextpos = None
            #printmap(area, units, goalpositions)
            #for goal in goalpositions:
                #printmap(area, units, [goal])
                #if manhattanuc(unit,goal):
            nextpos = bfsearch(area, unit.coord, goalpositions, units)
            
            if nextpos != None:
                move(area, unit.coord, nextpos)
                unit.coord = nextpos
                attackedunit = unit.attackifpossible(area, units, goblins, elves)
                if attackedunit != None and attackedunit.hp <= 0:
                    removefrommap(area, attackedunit.coord)
            #print('Moved:')
            #printmap(area, units)
        elif attackedunit.hp <= 0:
            removefrommap(area, attackedunit.coord)
    for unit in dead:
        units.remove(unit)
    totalhealth = 0
    for unit in units:
        totalhealth += unit.hp
    print('round', roundno, 'health', totalhealth, 'outcome', totalhealth*roundno)
    printmap(area, units)
    input()
    roundno += 1