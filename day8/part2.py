def summetadata (input):
    #if not input:
    #    return 0
    res = 0
    nodes = int(input.pop())
    metadata = int(input.pop())
    if nodes == 0:
        for i in range(metadata):
            res+= int(input.pop())
        return res 
    #print('nodes', nodes)
    sumlist = []
    for i in range(nodes):
        sumlist.append(summetadata(input))
    for i in range(metadata):
        index = int(input.pop())
        if index != 0 and index <=len(sumlist):
            res+=sumlist[index-1]
    return res



with open('input') as f:
    input = f.readline().split()
input.reverse()
print(summetadata(input))
