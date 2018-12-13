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

carts.sort()

nocrash = True
tick = 0
#printmap(area,carts)
while nocrash:
    crashing = []
    carts.sort()
    for movingcart in carts:
        movingcart.move(area)
        for othercart in carts:
            if movingcart.iscolliding(othercart):
                carts = [x for x in carts if x != movingcart and x != othercart]
                print('BOOM tick, x, y', tick, movingcart.x, movingcart.y, ' remaining ', len(carts))
                #print(carts)
                #break
    if len(carts) <= 1:
        print('Last wagon standing', carts[0].x, carts[0].y)
        nocrash = False        
    tick+=1
    #printmap(area,carts)
    #input()

for cart in carts:
    print(cart)
