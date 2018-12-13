class Cart:

    nextturn = 'left'
    dirs = {'left': {'x': -1, 'y': 0},
        'up': {'x': 0, 'y': -1},
        'right': {'x': 1, 'y': 0},
        'down': {'x': 0, 'y': 1}}

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

    def move(self, area):
        nextx = self.x+self.dirs[self.dir]['x']
        nexty = self.y+self.dirs[self.dir]['y']
        nextchar = area[nexty][nextx]
        if nextchar == '\\' and self.dir == 'left':
            if self.dir == 'left':
                self.dir = 'up'
            elif self.dir == 'up':
                self.dir = 'left'
            elif self.dir == 'right':
                self.dir = 'down'
            elif self.dir == 'down':
                self.dir = 'right'
        elif nextchar == '/':
            if self.dir == 'left':
                self.dir = 'down'
            elif self.dir == 'up':
                self.dir = 'right'
            elif self.dir == 'right':
                self.dir = 'up'
            elif self.dir == 'down':
                self.dir = 'left'
        elif nextchar == '+':
            if nextturn = 'left':
                
        else:
            print('ERROR')
        self.x = nextx
        self.y = nexty
