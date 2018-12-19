from unit import *
from mapmethods import *
from manhattan import *

area, units, elves, goblins = readmap('day15/input')
printmap(area, units,[])
gameover = False
roundno = 0
while not gameover:
    units.sort()
    elves.sort()
    goblins.sort()
    for unit in units:
        attackedunit = unit.attackifpossible(area, units, goblins,  elves)
        goalpositions = []
        if attackedunit == None:

            targets = unit.gettargets(units)
            if len(targets) == 0:
                gameover = True
                break

            for target in targets:
                goalpositions += getemptyclosecoordadjecents(area, unit.coord, target.coord)
            goalpositions.sort() ##Remove??

            nextpos = None
            mincost = 100000
            #printmap(area, units, goalpositions)
            for goal in goalpositions:
                #printmap(area, units, [goal])
                if manhattanuc(unit,goal) < mincost:
                    position, cost = astar(area, unit.coord, goal, units)
                    if position != None and cost < mincost:
                        mincost = cost
                        nextpos = position
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

    totalhealth = 0
    for unit in units:
        totalhealth += unit.hp
    print('round', roundno, 'health', totalhealth, 'outcome', totalhealth*roundno)
    printmap(area, units)
    roundno += 1