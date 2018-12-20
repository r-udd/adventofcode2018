class Room ():

    def __init__(self, east, north, prev):
        self.east = east
        self.north = north
        self.prev = prev
        if prev != None:
            self.cost = prev.cost + 1
        else:
            self.cost = 0
    
    def __lt__(self, other):
        if self.north < other.north:
            return True
        elif self.north == other.north:
            return self.east < other.east

    def __eq__(self, other):
        if other != None:
            return self.east == other.east and self.north == other.north
        return False

    def __hash__(self):
        return (self.east, self.north).__hash__()

    def __str__(self):
        return ' east: ' + str(self.east) + ' north: ' + str(self.north)