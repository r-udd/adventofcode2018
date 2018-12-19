def manhattanuc(unit, coord):
    return abs (unit.coord.x - coord.x) + abs(unit.coord.y - coord.y)

def manhattanuu(unit, unit2):
    return abs (unit.coord.x - unit2.coord.x) + abs(unit.coord.y - unit2.coord.y)

def manhattancc(coord, coord2):
    return abs (coord.x - coord2.x) + abs(coord.y - coord2.y)