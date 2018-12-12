def patterntolist(pattern):
    res = [0]*5
    for index in range(len(pattern)):
        res[index] = pattern[index] == '#'
    return res

def summera(pots, offset):
    sum = 0
    for index, pot in enumerate(pots):
        if pot:
            sum += index-offset
    return sum

generations = 50000000000
patterns = []
with open('input') as f:
    initial = f.readline()[len('initial state: '):]
    f.readline() #empty
    for line in f.readlines():
        if line[-2] == '#':
            patterns.append(patterntolist(line[:5]))

offset = 200
noofpots = (offset * 2 + len(initial))
prevpots = [False] * noofpots
for index, pot in enumerate(initial):
    prevpots[offset + index] = pot == '#'

sum = 0
prevsum = 0
#The diff gets constant after ~100 generations.
for generation in range(1,110):
    pots = [False] * noofpots
    for index in range(2,len(pots)-2):
        pots[index] = prevpots[index-2:index+3] in patterns
    if pots[0] or pots[1] or pots[2] or pots[-3] or pots[-1] or pots[-2]:
        print("This shouldn't happen! (hopefully)")

    sum = summera(pots,offset)
    diff = sum-prevsum
    prevsum = sum
    prevpots = pots


print('generations', generations, 'gen', generation, 'diff', diff, 'sum', sum)
print('answer', (generations-generation)*diff + sum)
