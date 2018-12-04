cloth = [[0] * 1000 for i in range(1000)]
with open('input') as f:
	file = f.readlines()

for line in file:
	linelist = line.split()
	startX = int(linelist[2].split(',')[0])
	startY = int(linelist[2].split(',')[1][:-1])
	width, height = linelist[3].split('x')
	for x in range(int(width)):
		for y in range(int(height)):
			if (cloth[startX+x][startY+y] == 0):
				cloth[startX+x][startY+y] = 1
			else:
				cloth[startX+x][startY+y] = 2

for line in file:
	linelist = line.split()
	id = linelist[0][1:]
	startX = int(linelist[2].split(',')[0])
	startY = int(linelist[2].split(',')[1][:-1])
	width, height = linelist[3].split('x')
	isintact = True
	for x in range(int(width)):
		for y in range(int(height)):
			if (cloth[startX+x][startY+y] == 2):
				isintact = False
	if isintact:
		print(id)

