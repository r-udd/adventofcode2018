recipes = [3,7]
first = 0
second = 1
#inputlist = [5,1,5,8,9]
#inputlist = [0,1,2,4,5]
#inputlist = [9,2,5,1,0]
#inputlist = [5,9,4,1,4]
inputlist = [3,6,0,7,8,1]
notfound = True
while notfound:
    #print(recipes)
    sum = recipes[first] + recipes[second]
    sumstr = str(sum)
    for c in sumstr:
        recipes.append(int(c))
        #print('seq', recipes[-len(inputlist):], end='')
        if recipes[-len(inputlist):] == inputlist:
            notfound = False
            break
    first = (first + recipes[first] + 1) % len(recipes)
    second = (second + recipes[second] + 1) % len(recipes)
    #input()

print(len(recipes)- len(inputlist))