from coord import *

def getchar(coord, moving, still, clay):
    if coord in moving:
        return '|'
    elif coord in still:
        return '~'
    elif coord in clay:
        return '#'
    else:
        return '.'

def findhole (coord, dir, moving, still, clay):
    #side = Coord(coord+dir, coord.y)
    current = Coord(coord.x, coord.y)
    while True:
        below = Coord(current.x, current.y+1)
        side = Coord(current.x+dir, current.y)
        belowchar = getchar(below, moving, still,clay)
        sidechar = getchar(side, moving, still,clay)
        if belowchar == '.':
            return True, current
        elif sidechar == '#':
            return False, current
        current.x += dir

def createmap(clay, movingwater, minx, maxx, maxy):
    area = []
    for y in range(maxy+1):
        arealine = []
        for x in range(minx-1, maxx+2):
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

def findlowestmovingwater(maxy, movingwater, still, clay):
    for moving in movingwater:
        x = moving.x
        y = moving.y
        if y == maxy:
            continue
        bc = Coord(x, y+1)
        below = getchar(bc, movingwater, still, clay)
        if below == '|':
            continue
        elif below == '.':
            return Coord(x,y)

        lc = Coord(x-1, y)
        #if x-1 > minx:
        left = getchar(lc, movingwater, still, clay)
        #else: 
        #    left = '|'

        rc = Coord(x+1, y)
        #if x+1 < maxx):
        right = getchar(rc, movingwater, still, clay)
        #else:
        #    right = '|'
        
        if below in ['#', '~']:
            if left == '.' or right == '.':
                return Coord(x,y)
            elif left == '#' and right == '#':
                return Coord(x,y)
                        

def printmap(minx, maxx, maxy, movingwater, stillwater, clay):
    for y in range(maxy+1):
        for x in range(minx-1, maxx+2):
            c = Coord(x,y)
            char = getchar(c, movingwater, stillwater, clay)
            print(char, end='')
        print()
    print()

clay = set()
with open('input') as f:
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
miny = 100000
for c in clay:
    if c.x > maxx:
        maxx = c.x
    if c.x < minx:
        minx = c.x
    if c.y > maxy:
        maxy = c.y
    if c.y < miny:
        miny = c.y

movingwater = {Coord(500,1)}

#clay.sort()
stillwater = set()
#area = createmap(clay, Coord(500,1), minx, maxx, maxy)
#printmap(area)
counter = 1
while True:
    moving = findlowestmovingwater(maxy, movingwater, stillwater, clay)
    if moving == None:
        break
    below = Coord(moving.x, moving.y+1)
    belowchar = getchar(below, movingwater, stillwater, clay)
    if belowchar == '.':
        movingwater.add(below)
    elif belowchar == '#' or belowchar == '~':
        foundleft, left = findhole(moving, -1, movingwater, stillwater, clay) #look to the left
        foundright, right = findhole(moving, 1, movingwater, stillwater, clay) #look to the right
        if not foundleft and not foundright:
            for i in range(left.x, right.x+1):
                c = Coord(i, moving.y)
                stillwater.add(c)
                if c in movingwater:
                    movingwater.remove(c)
        if foundleft or foundright:
            for i in range(left.x, right.x+1):
                c = Coord(i, moving.y)
                movingwater.add(c)
    #if counter == 1000:
     #   printmap(minx, maxx, maxy, movingwater, stillwater, clay)
      #  break
    counter += 1
#printmap(minx, maxx, maxy, movingwater, stillwater, clay)
print('maxy', maxy)
movingcount = len([s for s in movingwater if s.y >=miny and s.y<=maxy])
stillcount = len([s for s in stillwater if s.y >=miny and s.y<=maxy])
print('part1', movingcount + stillcount)
print('part2', stillcount)
'''for water in movingwater:
    below = Coord(water.x, water.y+1)
    if below in movingwater:
        continue
    if below not in clay and below not in movingwater:
        movingwater.append(below)
    elif below in clay:
        stillwater.append(water)
'''
