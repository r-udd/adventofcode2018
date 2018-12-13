from cart import *

def printmap (area,carts):
    for y, row in enumerate(area):
        for x,tile in enumerate(row):
            for cart in carts:
                if cart.x == x and cart.y == y:
                    print('X', end='')
                    break
            else:
                print(tile, end='')
        print()
    print('\n')

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

nocrash = True
tick = 0
while nocrash:
    for cart in carts:
        cart.move(area)
    tick+=1
    printmap(area,carts)
    input()

for cart in carts:
    print(cart)
