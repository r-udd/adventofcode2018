def manhattan(unit, position):
    return abs (unit.x - position['x']) + abs(unit.y - position['y'])

def manhattan(unit, unit2):
    return abs (unit.x - unit2.x) + abs(unit.y - unit2.y)