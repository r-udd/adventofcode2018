import sys

l = [int (i) for i in open ('input').readlines()]
found = set()
freq = 0
while True:
	for i in l:
		freq += i
		if (freq in found):
			print(freq)
			sys.exit()
		found.add(freq)