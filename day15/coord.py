
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

    def __str__(self):
        return ' x: ' + str(self.x) + ' y: ' + str(self.y)