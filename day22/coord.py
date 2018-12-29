tools = {'torch': '=', 'climb': '|', 'neither': '.'}
dirs = ((-1, 0), (0, 1), (0, -1), (1, 0))

def ispassable(area, x, y, tool):
    return x >= 0 and y >= 0 and tools[tool] != area[y][x]

class Node():
    
    def __init__(self, x, y, tool, minutes = 1000000):
        self.minutes = minutes
        self.x = x
        self.y = y
        self.tool = tool
    
    #def __hash__(self):
    #    return (self.x, self.y, self.tool).__hash__()

    def __lt__(self, other):
        '''if self.minutes < other.minutes:
            return True
        if self.minutes == other.minutes:
            if self.x < other.x:
                return True
            elif self.x == other.x:
                if self.y == other.y:
                    return True
        return False'''
        res = (self.minutes, self.x, self.y, self.tool) < (other.minutes, other.x, other.y, other.tool) 
        return res

    def getregiontype(self, area):
        return area[self.y][self.x]

    def getadjecents(self, area, tool):
        #possibles = (Coord(self.x, self.y-1), Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y+1))
        return (Node(self.x + d[0], self.y + d[1], tool) for d in dirs if ispassable(area, self.x + d[0], self.y + d[1], tool))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.tool == other.tool

    def getnexttool(self, area):
        for t, weaktype in tools.items():
            if t != self.tool and self.getregiontype(area) != weaktype:
                return t

    #def __str__(self):
    #    return ' x: ' + str(self.x) + ' y: ' + str(self.y)
