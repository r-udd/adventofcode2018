class Cart:
    
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y < other.y

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y) + ' dir: ' + self.dir
