cloth = [[0 for j in range(1001)] for i in range(1001)]
with open('input') as f:
	file = f.readlines()

for line in file:
	linelist = line.split()
	startX = int(linelist[2].split(',')[0])
	startY = int(linelist[2].split(',')[1][:-1])
	width = int(linelist[3].split('x')[0])
	height = int(linelist[3].split('x')[1])
	for x in range(1, width+1):
		for y in range(1, height+1):
			if (cloth[startX+x][startY+y] == 0):
				cloth[startX+x][startY+y] = 1
			else:
				cloth[startX+x][startY+y] = 2

for line in file:
	linelist = line.split()
	id = linelist[0][1:]
	startX = int(linelist[2].split(',')[0])
	startY = int(linelist[2].split(',')[1][:-1])
	width = int(linelist[3].split('x')[0])
	height = int(linelist[3].split('x')[1])
	isintact = True
	for x in range(1, width+1):
		for y in range(1, height+1):
			if (cloth[startX+x][startY+y] == 2):
				isintact = False
	if isintact:
		print(id)

