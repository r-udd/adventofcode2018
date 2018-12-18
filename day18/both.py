from coord import * 

def readmap (filename, size):
    area = area = [[0 for j in range(size)] for i in range(size)]
    with open(filename) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == '\n':
                    continue
                area[y][x] = char
    return area

def printmap (area):
    for y, row in enumerate(area):
        for x, tile in enumerate(row):
            print(tile, end='')
        print()
    print('\n')

def countno(area, char):
    count = 0
    for y in range(size):
        for x in range(size):
            if area[y][x] == char:
                count += 1
    return count

def count(area, adjecents, char, atleast):
    count = 0
    for pos in adjecents:
        if area[pos.y][pos.x] == char:
            count += 1
    return count >= atleast

size = 50
area = readmap('day18/input',size)
new = [['.' for j in range(size)] for i in range(size)]
minutecount = 10
maxresource = 0
lastmaxminute = 0
minute = 0
while minute < minutecount:
    for y in range(size):
        for x in range(size):
            current = Coord(x,y)
            char = area[current.y][current.x]
            adjecents = current.getadjecents(size, size)
            if char == '.' and count(area, adjecents, '|', 3):
                new[current.y][current.x] = '|'
            elif char == '|' and count(area, adjecents, '#', 3):
                new[current.y][current.x] = '#'
            elif char == '#' and count(area, adjecents, '#', 1) and count(area, adjecents, '|', 1):
                new[current.y][current.x] = '#'
            elif char == '#':
                new[current.y][current.x] = '.'
            else:
                new[current.y][current.x] = area[current.y][current.x]

    for y in range(size):
        for x in range(size):
            area[y][x] = new[y][x]
    
    if minute >= 500:
        treecount = countno(area,'|')
        millcount = countno(area,'#')
        resource = treecount * millcount
        if resource > maxresource:
            print(minute, resource)
            maxresource = resource
            lastmaxminute = minute
        elif resource == maxresource:
            print(minute, resource)
            minutecount = minute + ((minutecount-minute) % (minute - lastmaxminute))
            lastmaxminute = minute
    minute+= 1

print('minute', minutecount, 'resource value', countno(area,'|') * countno(area, '#'))