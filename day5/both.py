def shouldBeRemoved(char1, char2):
    return char1.lower() == char2.lower() and char1 != char2

def removePolymers (charList):
    index = 0
    removedAny = False
    while (True):
        if index + 1 >= len(charList):
            index = 0
            if not removedAny:
                break
            removedAny = False

        if shouldBeRemoved(charList[index], charList[index+1]):
            charList = charList[:index] + charList[index+2:]
            removedAny = True
        else:
            index += 1
    return len(charList)

with open('input') as f:
	line = f.readline()
charList = [c for c in line[:-1]] #remove linebreak

print('part1:', removePolymers(charList))
results = []
for char in 'abcdefghijklmnopqrstuvwxyz':
    charList = [c for c in line[:-1] if c.lower() != char]
    length = removePolymers(charList)
    results.append(length)

print('part2' ,min(results))