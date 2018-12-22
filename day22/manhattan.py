def manhattan(coord, coord2):
    return abs (coord.x - coord2.x) + abs(coord.y - coord2.y)

def diagonal(coord, coord2):
    return (abs (coord.x - coord2.x)**2 + abs(coord.y - coord2.y) ** 2) ** 0.5