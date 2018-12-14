from cart import *
import sys

def printmap (area,carts):
    dirchars = {'left': '<',
    'right': '>',
    'up': '^',
    'down': 'v'}
    for y, row in enumerate(area):
        for x,tile in enumerate(row):
            for cart in carts:
                if cart.x == x and cart.y == y:
                    print(dirchars[cart.dir], end='')
                    break
            else:
                print(tile, end='')
        print()
    print('\n')

carts = []
area = []
id = 0
with open('day13/input') as f:
    for y, line in enumerate(f):
        arealine = []
        for x, char in enumerate(line):
            if char == '\n':
                continue
            if char == '>':
                carts.append(Cart(x,y,'right', id))
                arealine.append('-')
                id += 1
            elif char == '^':
                carts.append(Cart(x,y,'up', id))
                arealine.append('|')
                id += 1
            elif char == '<':
                carts.append(Cart(x,y,'left', id))
                arealine.append('-')
                id += 1
            elif char == 'v':
                carts.append(Cart(x,y,'down', id))
                arealine.append('|')
                id += 1
            else:
                arealine.append(char)
            #print(char, end='')
        area.append(arealine)


nocrash = True
tick = 0
#printmap(area,carts)
while nocrash:
    carts.sort()
    for cart in carts:
        cart.move(area)
        
        for c in carts:
            if cart.iscolliding(c):
                print('BOOM x, y, tick', cart.x, cart.y, tick)
                nocrash = False
        
    tick+=1
    #printmap(area,carts)
    #input()
