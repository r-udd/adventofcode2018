
class Bot ():

    def __init__(self, x, y, z, radius):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
    
    def manhattan(self, bot):
        return abs (self.x - bot.x) + abs(self.y - bot.y) + abs(self.z - bot.z)