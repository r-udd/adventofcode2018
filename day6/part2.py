def manhattan (pointa, x, y):
    return abs (pointa['x'] - x) + abs(pointa['y'] - y)

counter = 0
coordinates = []
maxX = 0
maxY = 0
offsetX = 110
offsetY = 100
with open('input') as f:
    for line in f:
        x = int(line[:line.index(',')]) +offsetX
        y = int(line[line.index(',') + 1:])+offsetY
        #print(x, y, counter)
        coordinates.append({'id': counter, 'x': x, 'y': y})
        counter += 1
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

edgeX = offsetX + maxX + 200
edgeY = offsetY + maxY + 200

print('edgeX', edgeX)
print('edgeY', edgeY)

#defaultid = 1000
#area = [[{'id': defaultid, 'dist': 100000}] * (edgeY) for i in range(edgeX)]
#print('len X', len(area))
#print('len Y', len(area[0]))
#print('area', area)
areacounter = 0
for x in range(offsetX + edgeX):
    for y in range(offsetY + edgeY):
        distances = 0
        for coordinate in coordinates:
            distances += manhattan(coordinate, x,y)
        if distances < 10000:
            areacounter += 1 
print(areacounter)
