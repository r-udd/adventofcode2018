from point import Point

def findmerges (constellations, start):
    for i in range(start, len(constellations)):
            for j in range(len(constellations)):
                if i == j:
                    continue
                for point in constellations[j]:
                    if any(point.manhattan(constpoint) <= 3 for constpoint in constellations[i]):
                        return i, j
    return -1, -1

res = [('test1', 2), ('test2', 4), ('test3', 3), ('test4', 8), ('input', -1)]
for trial in res:
    points = []
    with open('day25/' + trial[0]) as f:
        for line in f:
            s = line.split(',')
            points.append(Point(int(s[0]), int(s[1]), int(s[2]), int(s[3])))


    constellations = []
    for point in points:
        newconst = True
        for const in constellations:
            if any(point.manhattan(constpoint) <= 3 for constpoint in const):
                const.append(point)
                newconst = False
                break
        if newconst:
            constellations.append([point])

    index1 = 0
    while True:
        index1, index2 = findmerges(constellations, index1)
        if index1 == -1 and index2 == -1:
            break
        print('JOINING', index1, index2)
        constellations[index1] += constellations[index2]
        del constellations[index2]

    print(trial[0], len(constellations))

    #assert len(constellations) == trial[1]