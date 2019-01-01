class Point ():

    def __init__(self, a, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.a = a

    def __eq__(self, other):
        if other != None:
            return self.x == other.x and self.y == other.y
        return False
 
    def manhattan(self, other):
        return abs (self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z) + abs(self.a - other.a)

    def __str__(self):
        return ' a: ' + str(self.a) + ' x: ' + str(self.x) + ' y: ' + str(self.y) + ' z: ' + str(self.z)
