import manhattan as m
import coord as c

tools = {'torch': '=', 'climb': '|', 'neither': '.'}
toolsallowed = {'=': {'climb', 'neither'}, '|': {'torch', 'neither'}, '.': {'climb', 'torch'}}

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
    closedset = set()
    #open = getemptyadjecents(area, start)
    startf = m.manhattan(start, target)
    openset = [c.Node(start, startf, 0, 0, tool, None)]

    smallestmanhattan = 1000000
    while len(openset) != 0:
        openset.sort()
        current = openset.pop(0)
        
        if current.coord == target:
            #debug = [s for s in closedset if s.coord.x <3 and s.coord.y < 2]
            return current
        closedset.add(current)
        adjacents = current.getadjecents(area)
        for adjacent in adjacents:
            adjregiontype = adjacent.getregiontype(area)

            if adjregiontype != tools[current.tool]:
                g = current.g + 1
                tool = current.tool
            else:
                g = current.g + 8
                tool = current.getnexttool(area) #tool = toolsallowed[currregiontype].intersection(toolsallowed[adjregiontype]) #current.getnexttool(area)

            if adjacent == target and tool != 'torch':
                g = g + 7
                print('EDGY')
                            
            h = m.manhattan(adjacent, target)
            if h < smallestmanhattan:
                print('manhattan dist to target', h)
                smallestmanhattan = h
            f = g + h
            successor = c.Node(adjacent, f, g, h, tool, current)
            if successor in closedset:
                continue

            if successor not in openset:
                openset.append(successor)

    #closedset.sort()
    #return closedset[0]

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

target = c.Coord(9,796)#c.Coord(14,778)#c.Coord(10, 10)#
xsize = target.x + 500
ysize = target.y + 500
erosions = [0] * xsize
area = [[0] * xsize for x in range(ysize)]
#erosions = [[0] * xsize for x in range(10)]
#geologic = [[0] * xsize for x in range(10)]
depth = 6969#11541#510# #11541
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


currenttool = 'torch'
start = c.Coord(0,0)

printmap(area, range(target.x - 10, target.x + 10), range(target.y - 10, target.y + 10), start, target, [])
#printmap(area, start, target, [])
#while True:
print('Search commencing!' + target.getregiontype(area))

endnode = astar(area, start, target, currenttool)
totalcost = endnode.g
#if endnode.tool != 'torch':
#    totalcost += 7
n = endnode
highlight = []
while n.coord != start:
    highlight.append(n.coord)
    n = n.prev


printmap(area, range(target.x - 10, target.x + 10), range(target.y - 10, target.y + 10), start, target, highlight)
#printmap(area, endnode.coord, target, highlight)
print('current tool ' + currenttool + ' cost: ' + str(totalcost))



    #if nextcoord != target:
        
print('answer', totalcost)