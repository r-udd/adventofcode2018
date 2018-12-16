from unit import *
from mapmethods import *

area, units, elves, goblins = readmap('day15/testC')
printmap(area, units,[])
gameover = False
while not gameover:
    units.sort()
    elves.sort()
    goblins.sort()
    for unit in units:
        attackedunit = unit.attackifpossible(goblins,elves)
        goalpositions = set()
        if attackedunit == None:

            targets = unit.gettargets(units)
            if len(targets) == 0:
                gameover = True
                break

            for target in targets:
                goalpositions = goalpositions.union(getemptyadjecentsset(area, target.coord))
            goalpositions = list(goalpositions)
            goalpositions.sort() ##Remove??

            nextpos = None
            mincost = 100000
            #printmap(area, units, goalpositions)
            for goal in goalpositions:
                #printmap(area, units, [goal])
                position, cost = astar(area, unit.coord, goal, units)
                if cost < mincost:
                    mincost = cost
                    if nextpos != None:
                        nextpos = position
            if nextpos != None:
                move(area, unit.coord, nextpos)
                unit.coord = nextpos
            #print('Moved:')
            #printmap(area, units)
        elif attackedunit.hp <= 0:
            units.remove(attackedunit)
            if attackedunit.iself():
                elves.remove(attackedunit)
            elif attackedunit.isgoblin:
                goblins.remove(attackedunit)
            else: 
                print('ERROR')

    printmap(area, units)

