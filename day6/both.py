def manhattan (pointa, x, y):
    return abs (pointa['x'] - x) + abs(pointa['y'] - y)

counter = 0
coordinates = []
maxX = 0
maxY = 0
with open('input') as f:
    for line in f:
        x = int(line[:line.index(',')])
        y = int(line[line.index(',') + 1:])
        #print(x, y, counter)
        coordinates.append({'id': counter, 'x': x, 'y': y})
        counter += 1
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

edgeX = maxX + 50
edgeY = maxY + 50

print('edgeX', edgeX)
print('edgeY', edgeY)

defaultid = 1000
area = [[{'id': defaultid, 'dist': 100000}] * (edgeY) for i in range(edgeX)]
print('len X', len(area))
print('len Y', len(area[0]))
#print('area', area)
sum = 0
areacounter = [0] * len(coordinates)
for x in range(edgeX):
    for y in range(edgeY):
        for coordinate in coordinates:
            dist = manhattan(coordinate, x,y)
            #print('Man', dist, coordinate, x, y)
            if dist < area[x][y]['dist']:
                previd = area[x][y]['id']
                newid = coordinate['id']
                if (previd !=  defaultid):
                    areacounter[previd] -= 1
                areacounter[newid] += 1
                area[x][y] = {'dist': dist, 'id': newid}
            elif dist == area[x][y]['dist']:
                previd = area[x][y]['id']
                newid = coordinate['id']
                if (previd !=  defaultid):
                    areacounter[previd] -= 1
                #print(dist, area[x][y]['dist'])
                area[x][y]['dist'] = dist
                area[x][y]['id'] = defaultid

#print('area', area)
'''
print('maxX', maxX, 'maxY', maxY)
for x in range(edgeX):
    for y in range(edgeY):
        #if area[x][y]['id'] != 1000:
        print(area[x][y]['id'],end=',')#, area[x][y]['dist'], '')
    print()
'''
#Go through edges and tag those ids as invalid
invalids = set()
for x in range(edgeX):
    id = area[x][0]['id']
    invalids.add(id)
    id = area[x][edgeY-1]['id']
    invalids.add(id)

for y in range(edgeY):
    id = area[0][y]['id']
    invalids.add(id)
    id = area[edgeX-1][y]['id']
    invalids.add(id)

#print(areacounter)
print('invalids', invalids)
currentMax = 0
for index, value in enumerate(areacounter):
    #print(index, value)
    if value > currentMax and index not in invalids:
        currentMax = value

#print('areacounter', areacounter)
print('Maximal area', currentMax)
