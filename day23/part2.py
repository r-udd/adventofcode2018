import bot as b
import z3
strongest = None
bots = []

def z3abs (value):
    return z3.If(value >= 0, value, -value)

opt = z3.Optimize()
x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')
with open('day23/input') as f:
    for line in f:
        splitted = line.split(',')
        xbot = int(splitted[0][5:])
        ybot = int(splitted[1])
        zbot = int(splitted[2][:-1])
        radius = int(splitted[3][3:-1])
        newbot = b.Bot(xbot, ybot, zbot, radius)
        opt.add_soft(z3abs (xbot-x) + z3abs (ybot-y) + z3abs (zbot-z) <= radius)
        bots.append(newbot)
        if strongest == None or newbot.radius > strongest.radius:
            strongest = newbot

dist = z3.Int('dist')
opt.add(dist == z3abs(x) + z3abs(y) + z3abs(z))
l = opt.minimize(dist)
opt.check()

print(opt.lower(l))
print(opt.model())