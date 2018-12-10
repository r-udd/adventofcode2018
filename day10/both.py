points = []
with open('input') as f:
    for line in f:
        x = int(line[line.index('<')+1:line.index(',')])
        y = int(line[line.index(',')+1:line.index('>')])
        velocity = line.split('<')[2]
        velx = int(velocity[0:velocity.index(',')])
        vely = int(velocity[velocity.index(',')+1:-2])
        points.append({'x': x, 'y': y, 'velx': velx, 'vely': vely})

counter = 0
prevarea = 100000000000
while True:
    minx = 1000000
    miny = 1000000
    maxx = -1000000
    maxy = -1000000
    for point in points:
        point['x'] += point['velx']
        point['y'] += point['vely']
        if point['x'] > maxx:
            maxx  = point['x']
        if point['y'] > maxy:
            maxy  = point['y']
        if point['x'] < minx:
            minx = point['x']
        if point['y'] < miny:
            miny = point['y']
    counter += 1
    area = (maxx - minx) * (maxy - miny)
    if area > prevarea:
        break
    
    prevarea = (maxx - minx) * (maxy - miny)

for y in range(miny, maxy+1):
    for x in range(minx, maxx+1):
        found = False
        for point in points:
            if point['x'] - point['velx'] == x and point['y'] - point['vely'] == y:
                found = True
        if found:
            print('#', end='')
        else:
            print('.', end='')
    print()
print('Part2', counter-1)