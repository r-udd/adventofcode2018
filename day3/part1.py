cloth = [[0 for j in range(1001)] for i in range(1001)]
with open('input') as f:
	for line in f:
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

sum = 0
for row in cloth:
	sum += row.count(2)
print(sum)
