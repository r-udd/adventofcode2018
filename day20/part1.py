from room import *

def removediff():
    0

def step(rooms, currentroom, nextroom):
    if nextroom not in rooms:
        rooms.add(nextroom)
    elif currentroom.cost < rooms[currentroom].cost:
        print('FOUND CLOSER PATH TO ROOM', currentroom.east, currentroom.north)
        # Go through all subsequent nodes and remove diff
        removediff()

def branch(rooms, currentroom, rest)
    0
        
def handleletter(rooms, currentroom, branchpoint, rest):
    #nextroom = None
    if len(rest) == 0:
        return currentroom
    char = rest[0]
    if char == 'N':
        nextroom = Room(currentroom.east, currentroom.north + 1, currentroom)
    elif char == 'S':
        nextroom = Room(currentroom.east, currentroom.north - 1, currentroom)
    elif char == 'W':
        nextroom = Room(currentroom.east - 1, currentroom.north, currentroom)
    elif char == 'E':
        nextroom = Room(currentroom.east + 1, currentroom.north, currentroom)
    elif char == ')':
        return [currentroom]
    elif char == '(':
        rooms = handleletter(rooms, currentroom, currentroom, rest[rest1:])
        rest.index(')')
        for room in rooms:
            handleletter(rooms, )
    elif char == '|':
        #if rest[1] == ')'
        #    return branchpoint
        return [currentroom] + handleletter(rooms, branchpoint, branchpoint, rest [:1])
        #nextroom = Room(currentroom.east + 1, currentroom.north, currentroom)
    else: 
        print('ERROR handleletter')
        step(rooms, currentroom, nextroom)
    handleletter(rooms, nextroom, rest[1:])



currentroom = Room(0, 0, None)
rooms = {currentroom}
with open('day20/test1') as f:
    line = f.readline()
    
for char in line:
    handleletters(rooms, currentroom, line[1:-1])

currentmax = 0
for room in rooms:
    if currentmax < room.cost:
        currentmax = room.cost
print('Answer', currentmax)