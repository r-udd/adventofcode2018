import coord as c
import manhattan as m

area = ['...', '...','...']
coord = c.Coord(1,1)
assert len(coord.getadjecents(area, 'torch'))== 4
length = coord.getadjecents(area, 'neither')
assert len(length)== 0

area = ['...', '|||','===']
assert len(coord.getadjecents(area, 'torch'))== 3
assert len(coord.getadjecents(area, 'neither'))== 3
assert len(coord.getadjecents(area, 'climb'))== 2


area = ['...', '...','...']
coord = c.Coord(0,0)
res = coord.getadjecents(area, 'torch')
assert len(res) == 2
length = coord.getadjecents(area, 'neither')
assert len(length)== 0

coord = c.Coord(0,0)
coord2 = c.Coord(4,3)
res = m.diagonal(coord, coord2)
assert res == 5

coord = c.Coord(0,0)
coord2 = c.Coord(10, 10)
res = m.diagonal(coord, coord2)
print(res)