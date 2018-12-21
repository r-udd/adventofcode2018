from unit import *
from mapmethods import *

tests = [('day15/testD', 47, 27730), ('day15/testE', 37, 36334), ('day15/testF', 46, 39514), ('day15/testG', 35, 27755), ('day15/testH', 54, 28944), ('day15/testI', 20, 18740)]
tests.append(('day15/input', 78, 221754))
#tests.append(('day15/testJ.2', 0, 0))
#tests.append(('day15/edgeA', 0, 0))
#tests.append(('day15/edgeB', 0, 0))
#tests.append(('day15/edgeC', 0, 0))
#tests.append(('day15/edgeD', 0, 0))
tests = tests[-1:]
for test in tests:
    area, units = readmap(test[0], 34)
    print('Initial')
    printmap(area, units,[])
    gameover = False
    roundno = 0
    while not gameover:
        
        units.sort()
        dead = []
        for unit in units:
            if unit in dead:
                continue
            attackedunit = unit.attackifpossible(area, units, dead)
            if attackedunit != None and attackedunit.hp <= 0:
                dead.append(attackedunit)
                removefrommap(area, attackedunit.coord)
            goalpositions = []
            if attackedunit == None:

                targets = unit.gettargets(units, dead)
                if len(targets) == 0:
                    gameover = True
                    break

                for target in targets:
                    goalpositions += getemptyadjecentsset(area, target.coord)
                
                nextpos = bfsearch(area, unit.coord, goalpositions, units)
                
                if nextpos != None:
                    move(area, unit.coord, nextpos)
                    unit.coord = nextpos
                    attackedunit = unit.attackifpossible(area, units, dead)
                    if attackedunit != None and attackedunit.hp <= 0:
                        dead.append(attackedunit)
                        removefrommap(area, attackedunit.coord)
        for unit in dead:
            units.remove(unit)
        totalhealth = 0
        for unit in units:
            totalhealth += unit.hp
        if gameover:
            expectedround = test[1]
            expectedscore = test[2]
            if expectedround == roundno and totalhealth*roundno == expectedscore:
                print('Correct' + test[0])
            else:
                print('round', roundno, 'health', totalhealth, 'outcome', totalhealth*roundno)
                print('ERROR round ' + str(expectedround) + ' score: ' + str(expectedscore))
                break

        print('round', roundno, 'health', totalhealth, 'outcome', totalhealth*roundno)
        unitscopy = units.copy()
        unitscopy.sort()
        printmap(area, unitscopy)
        roundno += 1