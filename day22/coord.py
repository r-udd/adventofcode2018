tools = {'torch': '=', 'climb': '|', 'neither': '.'}
dirs = ((-1, 0), (0, -1), (0, 0), (0, 1), (1, 0))

def ispassable(area, x, y, tool):
    return x >= 0 and y >= 0 and tools[tool] != area[y][x]

class Coord ():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''   
    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            return self.x < other.x
    '''
    def __eq__(self, other):
        if other != None:
            return self.x == other.x and self.y == other.y
        return False

    def getregiontype(self, area):
        return area[self.y][self.x]

    def __hash__(self):
        return (self.x, self.y).__hash__()

    """ def ispassable(self, area, tool):
        if self.x < 0 or self.y < 0:
            return False
        return area[self.y][self.x] != tools[tool] 
        
        def getadjecents(self, area, tool):
        possibles = [Coord(self.x, self.y-1), Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y+1)]
        return [c for c in possibles if c.ispassable(area, tool)]"""

    def getadjecents(self, area, tool):
        #possibles = (Coord(self.x, self.y-1), Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y+1))
        return (Coord(self.x + d[0], self.y + d[1]) for d in dirs if ispassable(area, self.x + d[0], self.y + d[1], tool))

    def __str__(self):
        return ' x: ' + str(self.x) + ' y: ' + str(self.y)


class Node():
    
    def __init__(self, coord, f, g, h, tool):
        self.coord = coord
        self.tool = tool
        self.f = f
        self.g = g
        self.h = h
    
    def __hash__(self):
        return (self.coord.__str__() + self.tool).__hash__()

    def getregiontype(self, area):
        return self.coord.getregiontype(area)

    def getadjecents(self, area):
        return self.coord.getadjecents(area, self.tool)

    def __eq__(self, other):
        return self.coord == other.coord and self.tool == other.tool

    def __lt__(self, other):
        if self.f < other.f:
            return True

    def getnexttool(self, area):
        for t, weaktype in tools.items():
            if t != self.tool and self.coord.getregiontype(area) != weaktype:
                return t
        """ 
        elif self.f == other.f:
            selftool = self.coord.getnexttool()
            othertool = other.coord.getnexttool()
            return len(self.getadjecents) """

