#import manhattan as m
import heapq

tools = {'torch': '=', 'climb': '|', 'neither': '.'}

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def ispassable(area, x, y, tool):
    return x >= 0 and y >= 0 and tools[tool] != area[y][x]

def getadjecents(area, x, y, tool):
    return ((x + d[0], y + d[1]) for d in dirs if ispassable(area, x + d[0], y + d[1], tool))

def getregiontype(area, x, y):
    return area[y][x]

def getnexttool(area, x, y, tool):
    for t, weaktype in tools.items():
        if t != tool and getregiontype(area, x, y) != weaktype:
            return t

def printmap (area, xrange, yrange, current, target):
    for y in yrange:
        for x in xrange:
            if x == current[0] and y == current[1]:
                print('@', end='')
            elif x == target[0] and y == target[1]:
                print('T', end='')
            else:
                print(area[y][x], end='')
        print()
    print()

def astar(area, start, target):
    closedset = dict()
    opennodes = []
    heapq.heappush(opennodes, (0, start[0], start[1], start[2]))
    #smallestmanhattan = 1000000
    while opennodes:
        minutes, x, y, tool = heapq.heappop(opennodes)
        key = (x, y, tool)
    
        if key in closedset and closedset[key] <= minutes:
            continue
        closedset[key] = minutes
        if key == target:
            return minutes

        heapq.heappush(opennodes, (minutes+7, x, y, getnexttool(area, x, y, tool)))
        adjacents = getadjecents(area, x, y, tool)
        for adjacent in adjacents:
            
            adjacentminutes = minutes + 1
            #h = m.manhattan(adjacent[0], adjacent[1], target)
            #if h < smallestmanhattan:
                #print('manhattan dist to target', h)
                #smallestmanhattan = h

            heapq.heappush(opennodes, (adjacentminutes, adjacent[0], adjacent[1], tool))

def geologic (erosions, x, y, targetx, targety):
    if x == 0 and y == 0:
        return 0
    elif x == targetx and y == targety:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosions[x-1] * erosions[x]

def erosion(x, y, erosions, depth, mod, targetx, targety):
    return (geologic(erosions, x, y, targetx, targety) + depth) % mod

targetx = 14
targety = 778
target = (targetx, targety, 'torch')
xsize = targetx + 1000
ysize = targety + 1000
erosions = [0] * xsize
area = [[0] * xsize for x in range(ysize)]
depth = 11541
mod = 20183

totalrisk = 0
for y in range (ysize):
    for x in range (xsize):
        erosions[x] = erosion(x, y, erosions, depth, mod, targetx, targety)        
        risk = erosions[x] % 3
        totalrisk += risk
        if x == targetx and y == targety:
            char = '.'
            #print('T', end='')
        elif x == 0 and y == 0:
            char = '.'
            #print('M', end='')
        elif risk == 0:
            char = '.' #Rocky
            #print(char, end='')
        elif risk == 1:
            char = '=' #Wet
            #print(char, end='')
        elif risk == 2:
            char = '|' #Narrow
            #print(char, end='')
        area[y][x] = char
    #print()


start = (0, 0, 'torch')

printmap(area, range(targetx - 10, targetx + 10), range(targety - 10, targety + 10), start, target)
#printmap(area, start, target, [])
print('Search commencing!')

endnode = astar(area, start, target)
print('answer', endnode)

#printmap(area, range(target.coord.x - 10, target.coord.x + 10), range(target.coord.y - 10, target.coord.y + 10), start, target, highlight)
