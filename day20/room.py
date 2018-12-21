class Room ():

    def __init__(self, east, north):
        self.east = east
        self.north = north
    
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

class RoomInfo ():

    def __init__(self, cost, prev):
        self.cost = cost
        self.prev = prev

    def __str__(self):
        return ' cost: ' + str(self.cost) + ' prev: ' + str(self.prev)