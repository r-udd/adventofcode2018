import bot as b
strongest = None
bots = []
with open('day23/input') as f:
    for line in f:
        splitted = line.split(',')
        x = int(splitted[0][5:])
        y = int(splitted[1])
        z = int(splitted[2][:-1])
        radius = int(splitted[3][3:-1])
        newbot = b.Bot(x, y, z, radius)
        bots.append(newbot)
        if strongest == None or newbot.radius > strongest.radius:
            strongest = newbot
count = 0
for bot in bots:
    if strongest.inrange(bot):
        count += 1

print(count)