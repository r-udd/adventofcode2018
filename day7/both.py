def removeletter (requirements, letter):
    for required in requirements:
        required.discard(letter)

allletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
requirements = [set() for char in allletters]
largestletter = 'A'
with open('input') as f:
    for line in f:
        splitted = line.split()
        required = splitted[1]
        target = splitted[-3]
        requirements[ord(target) - ord('A')].add(required)
        if target > largestletter:
            largestletter = target
        if required > largestletter:
            largestletter = required
requirements = requirements[:ord(largestletter) - ord('A') + 1]
allletters = allletters[:ord(largestletter) - ord('A') + 1]
print (requirements)
print(allletters)

result = ""
while True:
    for index, char in enumerate(allletters):
        if len(requirements[index]) == 0 and char not in result: #Nothing left blocking this letter
            removeletter(requirements, char)
            result += char
            break
    if len(result) == len(allletters):
        break
print(result)