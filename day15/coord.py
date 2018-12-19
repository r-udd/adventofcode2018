from manhattan import *

class Coord ():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            return self.x < other.x

    def __eq__(self, other):
        if other != None:
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return (self.x, self.y).__hash__()

    def getadjecents(self):
        'Returns in reading order'
        return [Coord(self.x, self.y-1), Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y+1)]
        
    
    def getclosecoordadjecents(self, target): 
        'Returns in reading order'
        return [Closecoord(self.x, self.y-1, target), Closecoord(self.x-1, self.y, target), Closecoord(self.x+1, self.y, target), Closecoord(self.x, self.y+1, target)]

    def __str__(self):
        return ' x: ' + str(self.x) + ' y: ' + str(self.y)

class Closecoord(Coord):
    'Will be ordered according to the manhattan distance of the target'
    def __init__(self, x, y, target):
        super().__init__(x,y)
        self.target = target
        self.dist = manhattancc(self, target)

    def __lt__(self, other):
        return self.dist < other.dist or (self.dist == other.dist and super().__lt__(other))