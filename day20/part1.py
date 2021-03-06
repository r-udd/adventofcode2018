from room import *

def findbackwardmatchingparenthesis(text, index):
    count = 0
    for i in range(index, -1, -1):
        if text[i] == ')':
            count += 1
        elif text[i] == '(':
            count -= 1
            if count == 0:
                return i

def removeparenthesis(text):
    right = text.rfind('|)')
    while right != -1:
        match = findbackwardmatchingparenthesis(text, right + 1)
        text = text[:match] + text[right+2:]

        right = text.rfind('|)')
    return text

    

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
expected = [3, 2, 10, 18, 23, 31, -1]

for test in range(len(expected)):

    currentroom = Room(0, 0)
    rooms = {currentroom: RoomInfo(0, None)}
    with open('day20/test' + str(start + test)) as f:
        line = f.readline()
    text = removeparenthesis(line)
    followpath(rooms, currentroom, text[1:])

    currentmax = 0
    roommax = None
    for room, info in rooms.items():
        if currentmax < info.cost:
            currentmax = info.cost
            roommax = room

    room = roommax
    print('test no ' + str(test))
    if test < 6:
        assert expected[test]==currentmax, 'expected: ' + str(expected[test]) + ' found: ' + str(currentmax)
        
print('Answer', currentmax)