def almostEqual (line1, line2):
	count = 0
	result = ""
	for char1,char2 in zip(line1, line2):
		if (char1 != char2):
			count += 1
		else:
			result += char1
	if count == 1:
		return result
	return ""


with open('input') as file:
	allLines=file.readlines()
	for line1 in allLines:
		for line2 in allLines:
			res = almostEqual(line1, line2)
			if (res != ""):
				print (res)

