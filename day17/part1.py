from coord import *

def findhole (area, coord, dir):
    #side = Coord(coord+dir, coord.y)
    current = Coord(coord.x, coord.y)
    while True:
        below = Coord(current.x, current.y+1)
        side = Coord(current.x+dir, current.y)
        belowchar = area[below.y][below.x]
        sidechar = area[side.y][side.x]
        if belowchar == '.':
            return True, current
        elif sidechar == '#':
            return False, current
        current.x += dir

def createmap(clay, movingwater, minx, maxx, maxy):
    area = []
    for y in range(maxy+1):
        arealine = []
        for x in range(minx, maxx+2):
            if Coord(x,y) in clay:
                arealine.append('#')
            elif Coord(x,y) == movingwater:
                arealine.append('|')
            elif x == 500 and y == 0:
                arealine.append('+')
            else:
                arealine.append('.')
        area.append(arealine)
    return area

def findlowestmovingwater(area):
    for y in range(len(area)-1, -1, -1):
        for x in range(len(area[y])-1, -1, -1):
            if area[y][x] == '|':
                if y == len(area) - 1:
                    continue
                below = area[y+1][x]
                if below == '|':
                    continue
                elif below == '.':
                    return Coord(x,y)

                if x-1 >= 0:
                    left = area[y][x-1]
                else: 
                    left = '|'
                if x+1 < len(area[y]):
                    right = area[y][x+1]
                else:
                    right = '|'
                
                if below in ['#', '~']:
                    if left == '.' or right == '.':
                        return Coord(x,y)
                    elif left == '#' and right == '#':
                        return Coord(x,y)
                        

def countwater(area):
    res = 0
    for line in area:
        for char in line:
            if char in ['~', '|']:
                res += 1
    return res

def printmap(area):
    for line in area:
        for x in line:
            print(x, end='')
        print()
    print()

clay = set()
with open('day17/input') as f:
    for line in f:
        if line.startswith('x'):
            x = int(line[2:line.index(',')])
            dotindex = line.index('..')
            ystart = int(line[line.index('y')+2:dotindex])
            ystop = int(line[dotindex + 2:-1])
            for y in range (ystart, ystop+1):
                clay.add(Coord(x,y))
        elif line.startswith('y'):
            y = int(line[2:line.index(',')])
            dotindex = line.index('..')
            xstart = int(line[line.index('x')+2:dotindex])
            xstop = int(line[dotindex + 2:-1])
            for x in range (xstart, xstop+1):
                clay.add(Coord(x,y))

maxx = 0
minx = 100000
maxy = 0
for c in clay:
    if c.x > maxx:
        maxx = c.x
    if c.x < minx:
        minx = c.x
    if c.y > maxy:
        maxy = c.y

#movingwater = [Coord(500,1)]

#clay.sort()
stillwater = []
area = createmap(clay, Coord(500,1), minx, maxx, maxy)
#printmap(area)
while True:
    moving = findlowestmovingwater(area)
    if moving == None:
        break
    below = Coord(moving.x, moving.y+1)
    belowchar = area[below.y][below.x]
    if belowchar == '.':
        area[below.y][below.x] = '|'
    elif belowchar == '#' or belowchar == '~':
        foundleft, left = findhole(area, moving, -1) #look to the left
        foundright, right = findhole(area, moving, 1) #look to the right
        if not foundleft and not foundright:
            for i in range(left.x, right.x+1):
                area[moving.y][i] = '~'
        if foundleft or foundright:
            for i in range(left.x, right.x+1):
                area[moving.y][i] = '|'
    #printmap(area)

print('Water amount', countwater(area))
'''for water in movingwater:
    below = Coord(water.x, water.y+1)
    if below in movingwater:
        continue
    if below not in clay and below not in movingwater:
        movingwater.append(below)
    elif below in clay:
        stillwater.append(water)
'''
