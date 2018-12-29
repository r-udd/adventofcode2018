import manhattan as m
import coord as c
import heapq

tools = {'torch': '=', 'climb': '|', 'neither': '.'}
#toolsallowed = {'=': {'climb', 'neither'}, '|': {'torch', 'neither'}, '.': {'climb', 'torch'}}

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def ispassable(area, x, y, tool):
    return x >= 0 and y >= 0 and tools[tool] != area[y][x]

def getadjecents(area, x, y, tool):
    #possibles = (Coord(self.x, self.y-1), Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y+1))
    return ((x + d[0], y + d[1]) for d in dirs if ispassable(area, x + d[0], y + d[1], tool))

def getregiontype(area, x, y):
    return area[y][x]

def getnexttool(area, x, y, tool):
    for t, weaktype in tools.items():
        if t != tool and getregiontype(area, x, y) != weaktype:
            return t

def printmap (area, xrange, yrange, current, target, highlight):
    for y in yrange:
        for x in xrange:
            if x == current.x and y == current.y:
                print('@', end='')
            elif x == target.x and y == target.y:
                print('T', end='')
            #elif c.Node(x,y,) in highlight:
            #    print('X', end='')
            else:
                print(area[y][x], end='')
        print()
    print()

def astar(area, start, target):
    closedset = dict()
    #open = getemptyadjecents(area, start)
    opennodes = []
    #heapq.heappush(opennodes, start)
    heapq.heappush(opennodes, (0, start.x, start.y, start.tool))
    smallestmanhattan = 1000000
    while opennodes:
        #current = heapq.heappop(opennodes)
        minutes, x, y, tool = heapq.heappop(opennodes)
        #print('f', current.f)
        key = (x, y, tool)
    
        if key in closedset and closedset[key] <= minutes:
            continue
        closedset[key] = minutes
        if x == target.x and y == target.y and tool == target.tool:
            return minutes

        heapq.heappush(opennodes, (minutes+7, x, y, getnexttool(area, x, y, tool)))
        #heapq.heappush(opennodes, c.Node(current.x, current.y, current.getnexttool(area), current.minutes+7))
        adjacents = getadjecents(area, x, y, tool)
        for adjacent in adjacents:
            
            adjacentminutes = minutes + 1
            h = m.manhattan(adjacent[0], adjacent[1], target)
            #if h < smallestmanhattan:
                #print('manhattan dist to target', h)
                #smallestmanhattan = h

            heapq.heappush(opennodes, (adjacentminutes, adjacent[0], adjacent[1], tool))

def geologic (erosions, x, y, target):
    if x == 0 and y == 0:
        return 0
    elif x == target.x and y == target.y:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosions[x-1] * erosions[x]

def erosion(x, y, erosions, depth, mod, target):
    return (geologic(erosions, x, y, target) + depth) % mod

target = c.Node(14, 778, 'torch')#c.Coord(9,796)#c.Coord(14,778)#c.Coord(10, 10)#
xsize = target.x + 1000
ysize = target.y + 1000
erosions = [0] * xsize
area = [[0] * xsize for x in range(ysize)]
#erosions = [[0] * xsize for x in range(10)]
#geologic = [[0] * xsize for x in range(10)]
depth = 11541#510# #11541
mod = 20183

totalrisk = 0
for y in range (ysize):
    for x in range (xsize):
        erosions[x] = erosion(x, y, erosions, depth, mod, target)        
        risk = erosions[x] % 3
        totalrisk += risk
        if x == target.x and y == target.y:
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


start = c.Node(0,0, 'torch', 0)

printmap(area, range(target.x - 10, target.x + 10), range(target.y - 10, target.y + 10), start, target, [])
#printmap(area, start, target, [])
#while True:
print('Search commencing!' + target.getregiontype(area))

endnode = astar(area, start, target)
print('answer', endnode)
#if endnode.tool != 'torch':
#    totalcost += 7
#highlight = []
#while n.coord != start:
#    highlight.append(n.coord)
#    n = n.prev


#printmap(area, range(target.coord.x - 10, target.coord.x + 10), range(target.coord.y - 10, target.coord.y + 10), start, target, highlight)
#printmap(area, endnode.coord, target, highlight)
#print('current tool ' + currenttool + ' cost: ' + str(totalcost))



    #if nextcoord != target:
        