
def calcpower (x, y, serial):
    rackid = x + 10
    power = rackid * y
    power += serial
    power = power * rackid
    power = int(str(power)[-3])
    return power - 5

def calcpowergrid(x, y, serial):
    sum = 0
    for i in range(y, y+3):
        for j in range(x, x+3):
            sum += calcpower(j, i, serial)
    return sum

maxpower = -100000
serial = 5235
#print(calcpower(34, 463, 18))
#print(calcpowergrid(33,45,serial))
for y in range(1,299):
    for x in range(2,299):
        power = calcpowergrid(x, y, serial)
        if power > maxpower:
            maxpower = power
            maxx = x
            maxy = y
print(maxpower, maxx, maxy)
