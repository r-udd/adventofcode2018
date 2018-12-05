def shouldBeRemoved(char1, char2):
    return char1.lower() == char2.lower() and char1 != char2

def removePolymers (charList):
    index = 0
    while (True):
        if index + 1 >= len(charList):
            break

        if shouldBeRemoved(charList[index], charList[index+1]):
            del charList[index: index + 2]
            index = max(index - 1, 0)
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

print('part2:', min(results))