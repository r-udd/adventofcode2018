area = [[0 for j in range(301)] for i in range(301)]

def calcpower (x, y, serial):
    rackid = x + 10
    power = rackid * y
    power += serial
    power = power * rackid
    power = int(str(power)[-3])
    return power - 5

def calcpowergrid(area, x, y, serial):
    maxpower = -100000
    maxsize = 0
    biggestarea=max(x,y)
    sum = 0
    for size in range(1, 301-biggestarea):
        for i in range (0,size):
            sum += area[x+i][y+size-1]
        for i in range (0,size):
            sum += area[x+size-1][y+i]
        sum -= area[x+size-1][y+size-1] #Gets counted twice
        if sum > maxpower:
            maxpower = sum
            maxsize = size
    return maxsize, maxpower

maxpower = -100000
serial = 5235
#print(calcpower(34, 463, 18))
#print(calcpowergrid(33,45,serial))
for x in range(1,301):
    for y in range(1,301):
        area[x][y] = calcpower(x,y,serial)


for x in range(1,301):
    for y in range(1,301):
        size, power = calcpowergrid(area, x, y, serial)
        if power > maxpower:
            maxpower = power
            maxx = x
            maxy = y
            maxsize = size
    if x % 10 == 0:
        print(x,maxpower, maxx, maxy, maxsize)
print(maxpower, maxx, maxy, maxsize)
print(calcpowergrid(area, 90,269,serial))
