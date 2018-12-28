import manhattan as m
import coord as c
import heapq

tools = {'torch': '=', 'climb': '|', 'neither': '.'}
#toolsallowed = {'=': {'climb', 'neither'}, '|': {'torch', 'neither'}, '.': {'climb', 'torch'}}

def printmap (area, xrange, yrange, current, target, highlight):
    for y in yrange:
        for x in xrange:
            if x == current.x and y == current.y:
                print('@', end='')
            elif x == target.x and y == target.y:
                print('T', end='')
            elif c.Coord(x,y) in highlight:
                print('X', end='')
            else:
                print(area[y][x], end='')
        print()
    print()

def astar(area, start, target, tool):
    closedset = dict()
    #open = getemptyadjecents(area, start)
    opennodes = []
    heapq.heappush(opennodes, c.Node(start, 0, 0, 0, tool))
    smallestmanhattan = 1000000
    while len(opennodes) != 0:
        current = heapq.heappop(opennodes)
        #print('f', current.f)
        key = (current.coord.x, current.coord.y, current.tool)
        closedset[key] = (current.f, current.g, current.h)
        adjacents = current.getadjecents(area)
        for adjacent in adjacents:

            if adjacent == current.coord:
                g = current.g + 7
                tool = current.getnexttool(area)
            else:
                g = current.g + 1
                tool = current.tool
                            
            h = m.manhattan(adjacent, target.coord)
            if h < smallestmanhattan:
                #print('manhattan dist to target', h)
                smallestmanhattan = h
            f = g + h
            successor = c.Node(adjacent, f, g, h, tool)

            if successor == target:
                return successor
            key = (adjacent.x, adjacent.y, tool)
            if key in closedset:
                if g < closedset[key][1]:
                    #print("This shouldn't happen")
                    closedset[key] = (f, g, h)
                continue

            try:
                index = opennodes.index(successor)
                if successor.g < opennodes[index].g:
                    #print('Will it happen?')
                    opennodes[index].g = g
                    opennodes[index].f = f
                continue
            except ValueError:
                pass
            """if successor in opennodes:
                index = opennodes.index(successor)
                if successor.g > opennodes[index].g:
                    continue
                else:
                    opennodes[index].g = g
                    opennodes[index].f = f
                    #print('replacing')"""
            if successor not in opennodes:
                heapq.heappush(opennodes, successor)

def geologic (erosions, x, y, target):
    if x == 0 and y == 0:
        return 0
    elif x == target.coord.x and y == target.coord.y:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosions[x-1] * erosions[x]

def erosion(x, y, erosions, depth, mod, target):
    return (geologic(erosions, x, y, target) + depth) % mod

target = c.Node(c.Coord(14,778), -1, -1, -1, 'torch')#c.Coord(9,796)#c.Coord(14,778)#c.Coord(10, 10)#
xsize = target.coord.x + 200
ysize = target.coord.y + 200
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
        if x == target.coord.x and y == target.coord.y:
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


currenttool = 'torch'
start = c.Coord(0,0)

printmap(area, range(target.coord.x - 10, target.coord.x + 10), range(target.coord.y - 10, target.coord.y + 10), start, target.coord, [])
#printmap(area, start, target, [])
#while True:
print('Search commencing!' + target.coord.getregiontype(area))

endnode = astar(area, start, target, currenttool)
print('answer', endnode.g)
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
        