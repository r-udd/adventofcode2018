import coord as c
import manhattan as m

def geologic (erosions, x, y, target):
    if x == 0 and y == 0:
        return 0
    elif x == target.x and y == target.y:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosions[x-1] * erosions[x]

def erosion(x, y, erosions, depth, mod, target):
    return (geologic(erosions, x, y, target) + depth) % mod

target = c.Coord(14,778)
xsize = target.x + 1
ysize = target.y + 1
erosions = [0] * xsize
#erosions = [[0] * xsize for x in range(10)]
#geologic = [[0] * xsize for x in range(10)]
depth = 11541
mod = 20183

totalrisk = 0
for y in range (ysize):
    for x in range (xsize):
        erosions[x] = erosion(x, y, erosions, depth, mod, target)        
        risk = erosions[x] % 3
        totalrisk += risk
        if x == target.x and y == target.y:
            print('T', end='')
        elif x == 0 and y == 0:
            print('M', end='')
        elif risk == 0:
            print('.', end='')
        elif risk == 1:
            print('=', end='')
        elif risk == 2:
            print('|', end='')
    print()
print('answer', totalrisk)