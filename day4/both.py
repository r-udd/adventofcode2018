def saveSleepingTime (guards, id, date, startSleepTime, endSleepTime):
	if id not in guards:
		guards[id] = {}
	if date not in guards[id]:
		guards[id][date] = []
	startminute = int(startSleepTime[-3:-1])
	endminute = int(endSleepTime[-3:-1])
	for minute in range(startminute, endminute):
		guards[id][date].append(minute)

def findminute (datesandtimes):
	minutetotal = [0] * 60
	for date, minutes in datesandtimes.items():
		for minute in minutes:
			minutetotal[minute] += 1
	maxcount = max(minutetotal)
	maxminute = minutetotal.index(maxcount)
	return maxcount, maxminute

guards = {}
isSleeping = False
with open('input') as f:
	sortedLines = f.readlines()
	sortedLines.sort()
	for line in sortedLines:
		date = line.split()[0][1:]
		time = line.split()[1]
		if '#' in line:
			id = line.split()[3][1:]
			isSleeping = False
		if 'wakes' in line and isSleeping:
			isSleeping = False
			endSleepTime = time
			saveSleepingTime(guards, id, date, startSleepTime, endSleepTime)
		if 'falls' in line:
			isSleeping = True
			startSleepTime = time

highesttotal = 0
highestid = -1
for guardid, dates in guards.items():
	totalminutes = 0
	for date, timelist in dates.items():
		totalminutes += len(timelist)
	if totalminutes > highesttotal:
		highesttotal = totalminutes
		highestid = guardid

maxcount, maxminute = findminute(guards[highestid])

#print ("minutes total", totalminutes, "guardid", guardid)
#print ('count', maxcount, 'maxminute', maxminute)
print('Part1:', int(highestid) * maxminute)

maxid = 0
totalmaxcount = 0
totalmaxminute = 0
for id, datelist in guards.items():
	maxcount, guardmaxminute = findminute(datelist)
	if (totalmaxcount < maxcount):
		maxid = id
		totalmaxminute = guardmaxminute
		totalmaxcount = maxcount

print ('Part2:', int(maxid)*totalmaxminute)