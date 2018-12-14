recipes = [3,7]
first = 0
second = 1
input = 360781
while len (recipes) <= input+10:
    #print(recipes)
    sum = recipes[first] + recipes[second]
    sumstr = str(sum)
    for c in sumstr:
        recipes.append(int(c))
    first = (first + recipes[first] + 1) % len(recipes)
    second = (second + recipes[second] + 1) % len(recipes)

for i in range(10):
    print(recipes[input+i], end='')
print()