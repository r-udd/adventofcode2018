from unit import *
#from manhattan import *
from mapmethods import *


area, units, elves, goblins = readmap()
printmap(area, units)
gameover = False
while not gameover:
    units.sort()
    #elves.sort()
    #goblins.sort()
    for unit in units:
        unit = unit.attackifpossible(goblins,elves)
        
        gameover = True
