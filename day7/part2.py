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
#print (requirements)
#print(allletters)

inprogress = []
donesecond = []
result = ""
currentsecond = 0
while True:
    for index, char in enumerate(allletters):
        if len(requirements[index]) == 0 and char not in result and char not in inprogress: #Nothing left blocking this letter
            if len(inprogress) < 5:
                inprogress.append(char)
                donesecond.append(currentsecond+61 + ord(char)-ord('A'))
                #print(inprogress, currentsecond, donesecond)
            #result += char
            #break
    currentsecond = min(donesecond)
    i = donesecond.index(currentsecond)
    #print(currentsecond, inprogress[i])
    toremove = inprogress.pop(i)
    result += toremove
    donesecond.pop(i)
    removeletter(requirements, toremove)
    
    
    if len(result) == len(allletters):
        break
print(result)
print(currentsecond)