from room import *    

def step(rooms, currentroom, nextroom, nextroominfo):
    if nextroom not in rooms:
        rooms[nextroom] = nextroominfo

def followpath (rooms, currentroom, text):
    roomstack = []
    index = 0
    while True:
        char = text[index]
        if char == '$':
            return
        if char == '(':
            roomstack.append(currentroom)
            index += 1
            continue
        elif char == '|':
            currentroom = roomstack[-1]
            index += 1
            continue
        elif char == ')':
            currentroom = roomstack.pop()
            index += 1
            continue
        elif char == 'N':
            nextroom = Room(currentroom.east, currentroom.north + 1) 
        elif char == 'S':
            nextroom = Room(currentroom.east, currentroom.north - 1)
        elif char == 'W':
            nextroom = Room(currentroom.east - 1, currentroom.north)
        elif char == 'E':
            nextroom = Room(currentroom.east + 1, currentroom.north)
        nextroominfo = RoomInfo(rooms[currentroom].cost + 1, currentroom)
        step(rooms, currentroom, nextroom, nextroominfo)
        currentroom = nextroom
        index += 1

start = 0
expected = [0, 0, 0, 0, 0, 0, -1]

for test in range(len(expected)):

    currentroom = Room(0, 0)
    rooms = {currentroom: RoomInfo(0, None)}
    with open('day20/test' + str(start + test)) as f:
        line = f.readline()
    followpath(rooms, currentroom, line[1:])

    over1000 = 0
    for room, info in rooms.items():
        if 1000 <= info.cost:
            over1000 += 1

    print('test no ' + str(test))
    if test < 6:
        assert expected[test]==over1000, 'expected: ' + str(expected[test]) + ' found: ' + str(currentmax)
        
print('Answer', over1000)