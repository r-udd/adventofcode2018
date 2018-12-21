from unit import *
from mapmethods import *
from manhattan import *

def removeifkilled(area, unit, dead):
    if unit.hp <= 0:
        removefrommap(area, attackedunit.coord)
        dead.append(attackedunit)
        if unit.iself():
            return True
    return False

tests = [('day15/testD', 29, 4988, 15), ('day15/testF', 33, 31284, 4), ('day15/testG', 37, 3478, 15), ('day15/testH', 39, 6474, 12), ('day15/testI', 30, 1140,34)]
tests.append(('day15/input', 28, 41972, 34))
#tests.append(('day15/edgeA', 0, 0))
#tests.append(('day15/edgeB', 0, 0))
#tests.append(('day15/edgeC', 0, 0))
#tests.append(('day15/edgeD', 0, 0))
#tests.append(('day15/testJ.2', 0, 0))
tests = tests[-1:]
for test in tests:
    
    elfpower = 3
    while True:
        elfpower += 1
        area, units = readmap(test[0], elfpower)
        #print('Initial')
        print('elf power', elfpower)
        #input()
        #printmap(area, units,[])
        gameover = False
        roundno = 0
        elfisdead = False
        while not gameover and not elfisdead:
            
            units.sort()
            dead = []
            for unit in units:
                if unit in dead:
                    continue
                attackedunit = unit.attackifpossible(area, units, dead)
                
                goalpositions = []
                if attackedunit != None:
                    elfisdead = removeifkilled(area, attackedunit, dead)
                    if elfisdead:
                        break
                else:
                    targets = unit.gettargets(units, dead)
                    if len(targets) == 0:
                        gameover = True
                        roundno -= 1
                        break

                    for target in targets:
                        goalpositions += getemptyadjecentsset(area, target.coord)
                    
                    nextpos = bfsearch(area, unit.coord, goalpositions, units)
                    
                    if nextpos != None:
                        move(area, unit.coord, nextpos)
                        unit.coord = nextpos
                        attackedunit = unit.attackifpossible(area, units, dead)
                        if attackedunit != None:
                            elfisdead = removeifkilled(area, attackedunit, dead)
                            if elfisdead:
                                roundno -= 1
                                break

            for unit in dead:
                units.remove(unit)

            roundno += 1
            totalhealth = 0
            for unit in units:
                if unit.isgoblin():
                    totalhealth += unit.hp
            print('round', roundno, 'health', totalhealth, 'outcome', totalhealth*roundno, 'elf power', elfpower)
            unitscopy = units.copy()
            unitscopy.sort()
            printmap(area, unitscopy)
        
        if elfisdead:
            totalhealth = 0
            for unit in units:
                if unit.isgoblin():
                    totalhealth += unit.hp
            print('Remaining goblin life', totalhealth)

        if not elfisdead and gameover:
            totalhealth = 0
            for unit in units:
                totalhealth += unit.hp
            expectedround = test[1]
            expectedscore = test[2]
            expectedpower = test[3]
            if expectedround == roundno and totalhealth*roundno == expectedscore and expectedpower == elfpower:
                print('Correct ' + test[0])
                break
            else:
                print('round', roundno, 'health', totalhealth, 'outcome', totalhealth*roundno, 'elf power', elfpower)
                print('ERROR' + test[0] + ' round ' + str(expectedround) + ' score: ' + str(expectedscore))
                break

#round 28 hp 1484 outcome 41552