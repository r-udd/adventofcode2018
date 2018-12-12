import pprint as p

def patterntolist(pattern):
    res = [0]*5
    for index in range(len(pattern)):
        res[index] = pattern[index] == '#'
    return res
pp = p.PrettyPrinter(indent=2)
generations = 20
patterns = []
with open('input') as f:
    initial = f.readline()[len('initial state: '):]
    #print(initial)

    f.readline() #empty
    for line in f.readlines():
        if line[-2] == '#':
            patterns.append(patterntolist(line[:5]))

#print(patterns)

prevpots = [False] * (generations * 4 + len(initial))
#print(len(pots))
for index, pot in enumerate(initial):
    prevpots[generations*2 + index] = pot == '#'

for generation in range(generations):
    pots = [False] * (generations * 4 + len(initial))
    for index in range(2,len(pots)-2):
        pots[index] = prevpots[index-2:index+3] in patterns
    prevpots = pots

#pp.pprint(pots)
sum = 0
for index, pot in enumerate(pots):
    if pot:
        sum += index-generations*2
print(sum)
