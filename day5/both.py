def shouldBeRemoved(char1, char2):
    return char1.lower() == char2.lower() and char1 != char2

def removePolymers (charList):
    index = len(charList) - 1
    while (True):
        if index <= 0:
            break
        if shouldBeRemoved(charList[index], charList[index-1]):
            del charList[index-1: index + 1]
            index = min(index - 1, len(charList) - 1)
        else:
            index -= 1
    return len(charList)

with open('input') as f:
	line = f.readline().rstrip()
charList = list(line)
result1 = removePolymers(charList)
print('part1:', result1)

minvalue = result1
for char in 'abcdefghijklmnopqrstuvwxyz':
    charList = list(line.replace(char,'').replace(char.upper(),''))
    length = removePolymers(charList)
    if length < minvalue:
        minvalue = length

print('part2:', minvalue)