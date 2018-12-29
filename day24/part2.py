from group import *
from copy import deepcopy
def getweakorimmunities(splitted, weakorimmune):
    gathered = []
    if weakorimmune in splitted:
        index = splitted.index(weakorimmune) + 2
        remaining = True
        while remaining:
            weakness = splitted[index]
            if weakness.endswith(';') or weakness.endswith(')'):
                remaining = False
                weakness = weakness[:-1]
            elif weakness.endswith(','):
                weakness = weakness[:-1]
            gathered.append(weakness)
            index += 1
    return gathered

originfection = []
origimmune = []
with open('day24/input') as f:
    for line in f:
        if line.startswith('Immune'):
            index = 1
            current = origimmune
            isinfection = False
            isimmune = True
        elif line.startswith('Infection'):
            index = 1
            current = originfection
            isinfection = True
            isimmune = False
        elif 'unit' in line:
            splitted = line.split()
            units = int(splitted[0])
            hp = int(splitted[4])
            doesindex = splitted.index('does')
            attack = int(splitted[doesindex+1])
            attacktype = splitted[doesindex+2]
            initiative = int(splitted[-1])
            splitted[7] = splitted[7][1:] #remove '('
            
            weaknesses = getweakorimmunities(splitted, 'weak')
            immunities = getweakorimmunities(splitted, 'immune')
            current.append(Group(index, units, hp, attack, attacktype, initiative, weaknesses, immunities, isinfection, isimmune))
            index += 1

boost = 1
while True:
    infection = deepcopy(originfection)
    immune = deepcopy(origimmune)
    for group in immune:
        group.attack += boost
    allgroups = infection + immune
    while infection and immune:
        allgroups = sorted(allgroups, key=lambda group: (group.effective(), group.initiative), reverse=True)
        alreadytargeted = []
        targetpairs = []
        for group in allgroups:
            if group.isimmune:
                targets = infection
            elif group.isinfection:
                targets = immune

            targets = sorted(targets, key=lambda target: (target.possibledamage(group.effective(), group.attacktype), target.effective(), target.initiative), reverse=True)
            for target in targets:
                if target not in alreadytargeted and target.possibledamage(group.effective(), group.attacktype) > 0:
                    alreadytargeted.append(target)
                    targetpairs.append((group, target))
                    break
        
        anyunitslost = False
        targetpairs = sorted(targetpairs, key=lambda pair: pair[0].initiative, reverse=True)
        for pair in targetpairs:
            attacker = pair[0]
            target = pair[1]
            if attacker.units > 0:
                unitslost = target.takedamage(attacker.effective(), attacker.attacktype)
                anyunitslost |= unitslost > 0
                if target.units <= 0:
                    if target.isimmune:
                        immune.remove(target)
                    elif target.isinfection:
                        infection.remove(target)
                    allgroups.remove(target)
        if not anyunitslost:
            print('stalemate', boost)
            break
    
    if not anyunitslost:
        print('stalemate outside loop', boost)
        boost += 1
        print('Try again with boost', boost)
    elif allgroups[0].isinfection:
        print('The infection won!')
        boost += 1
        print('Try again with boost', boost)
    else:
        break

totalunits = 0
for group in allgroups:
    totalunits += group.units
print('Answer', totalunits)