class Point ():

    def __init__(self, a, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
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

    def __hash__(self):
        return (self.x, self.y).__hash__()

    """ def ispassable(self, area, tool):
        if self.x < 0 or self.y < 0:
            return False
        return area[self.y][self.x] != tools[tool] 
        
        def getadjecents(self, area, tool):
        possibles = [Coord(self.x, self.y-1), Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y+1)]
        return [c for c in possibles if c.ispassable(area, tool)]"""
    
    def manhattan(self, other):
        return abs (self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z) + abs(self.a - other.a)

    def __str__(self):
        return ' a: ' + str(self.a) + ' x: ' + str(self.x) + ' y: ' + str(self.y) + ' z: ' + str(self.z)
"""

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
        
        elif self.f == other.f:
            selftool = self.coord.getnexttool()
            othertool = other.coord.getnexttool()
            return len(self.getadjecents) """

