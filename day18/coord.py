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
    
    def getadjecents(self,maxx, maxy):
        'Returns in reading order'
        diffs=((-1,-1), (0,-1), (1,-1), (-1, 0), (1,0), (-1, 1), (0, 1), (1, 1))
        return [Coord(self.x+diff[0], self.y+diff[1]) for diff in diffs if self.x+diff[0] >= 0 and self.x+diff[0] < maxx and self.y+diff[1] >= 0 and self.y+diff[1] < maxy]
        #return [[Coord(x, y) for x in range(self.x-1, self.x+2) if x >= 0 and y >= 0 and x < maxx and y < maxy and (self.x !=x or self.y!=y)] for y in range(self.y-1,self.y + 2)]

    def __str__(self):
        return ' x: ' + str(self.x) + ' y: ' + str(self.y)