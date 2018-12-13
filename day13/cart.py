class Cart:

    nextturn = 'left'
    dirs = {'left': {'x': -1, 'y': 0},
        'up': {'x': 0, 'y': -1},
        'right': {'x': 1, 'y': 0},
        'down': {'x': 0, 'y': 1}}
    ordereddirs = ['left', 'up', 'right', 'down']

    def __init__(self, x, y, dir, id):
        self.x = x
        self.y = y
        self.dir = dir
        self.id = id

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y < other.y
    
    def iscolliding(self, other):
        '''Used for collision calculation, cant collide with itself'''
        return self.id != other.id and self.x == other.x and self.y == other.y

    def __str__(self):
        return 'id: ' + str(self.id) + ' x: ' + str(self.x) + ' y: ' + str(self.y) + ' dir: ' + self.dir

    def move(self, area):
        nextx = self.x+self.dirs[self.dir]['x']
        nexty = self.y+self.dirs[self.dir]['y']
        self.x = nextx
        self.y = nexty
        nextchar = area[nexty][nextx]
        if nextchar == '\\':
            if self.dir == 'left':
                self.dir = 'up'
            elif self.dir == 'up':
                self.dir = 'left'
            elif self.dir == 'right':
                self.dir = 'down'
            elif self.dir == 'down':
                self.dir = 'right'
            else:
                print('ERROR 1')
        elif nextchar == '/':
            if self.dir == 'left':
                self.dir = 'down'
            elif self.dir == 'up':
                self.dir = 'right'
            elif self.dir == 'right':
                self.dir = 'up'
            elif self.dir == 'down':
                self.dir = 'left'
            else:
                print('ERROR 2')
        elif nextchar == '+':
            index = self.ordereddirs.index(self.dir)
            if self.nextturn == 'left':
                self.dir = self.ordereddirs[(index - 1) % 4]
                self.nextturn = 'straight'
            elif self.nextturn == 'straight':
                self.nextturn = 'right'
            elif self.nextturn == 'right':
                self.dir = self.ordereddirs[(index + 1) % 4]
                self.nextturn = 'left'
            else:
                print('ERROR 3')
