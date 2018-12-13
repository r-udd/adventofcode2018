from cart import *

def printmap (area):
    for row in area:
        for tile in row:
            print(tile, end='')
        print()
    print('\n')

dirs = {}
dirs['left'] = {'x': -1, 'y': 0}
dirs['up'] = {'x': 0, 'y': -1}
dirs['right'] = {'x': 1, 'y': 0}
dirs['down'] = {'x': 0, 'y': 1}
carts = []
area = []
with open('day13/test') as f:
    for y, line in enumerate(f):
        arealine = []
        for x, char in enumerate(line):
            if char == '\n':
                continue
            if char == '>':
                carts.append(Cart(x,y,'right'))
                arealine.append('-')
            elif char == '^':
                carts.append(Cart(x,y,'up'))
                arealine.append('|')
            elif char == '<':
                carts.append(Cart(x,y,'left'))
                arealine.append('-')
            elif char == 'v':
                carts.append(Cart(x,y,'down'))
                arealine.append('|')
            else:
                arealine.append(char)
            #print(char, end='')
        area.append(arealine)

carts.sort()

printmap(area)
for cart in carts:
    print(cart)
