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
	line = f.readline().rstrip()
charList = list(line)
result1 = removePolymers(charList)
print('part1:', result1)

minvalue = result1
for char in 'abcdefghijklmnopqrstuvwxyz':
    #currentline = line.replace(char,'').replace(char.upper(),'')
    charList = list(line.replace(char,'').replace(char.upper(),''))
    length = removePolymers(charList)
    if length < minvalue:
        minvalue = length

print('part2:', minvalue)