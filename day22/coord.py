tools = {'torch': '=', 'climb': '|', 'neither': '.'}

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

    def ispassable(self, area):
        return self.x >= 0 and self.y >= 0

    def getadjecents(self, area):
        possibles = [Coord(self.x, self.y-1), Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y+1)]
        return [c for c in possibles if c.ispassable(area)]

    def __str__(self):
        return ' x: ' + str(self.x) + ' y: ' + str(self.y)


class Node():
    
    def __init__(self, coord, f, g, h, tool, prev):
        self.coord = coord
        self.tool = tool
        self.f = f
        self.g = g
        self.h = h
        self.prev = prev
    
    def __hash__(self):
        return self.coord.__hash__()

    def getregiontype(self, area):
        return self.coord.getregiontype(area)

    def getadjecents(self, area):
        return self.coord.getadjecents(area)

    def __eq__(self, other):
        return self.coord == other.coord

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

