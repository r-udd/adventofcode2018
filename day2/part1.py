exactlyTwo = 0
exactlyThree = 0
with open('input') as file:
	for line in file:
		noOfChar = {}
		for char in line:
			noOfChar[char] = noOfChar.get(char,0) + 1
		if any(v == 2 for k,v in noOfChar.items()):
			exactlyTwo += 1
		if any(v == 3 for k,v in noOfChar.items()):
			exactlyThree += 1
print ('exactlyTwo', exactlyTwo)
print ('exactlyThree', exactlyThree)
print ('Checksum', exactlyTwo * exactlyThree)
