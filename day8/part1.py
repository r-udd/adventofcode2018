def summetadata (input):
    #if not input:
    #    return 0
    nodes = int(input.pop())
    #print('nodes', nodes)
    metadata = int(input.pop())
    res = 0
    for i in range(nodes):
        res+= summetadata(input)
    for i in range(metadata):
        res+= int(input.pop())
    return res



with open('input') as f:
    input = f.readline().split()
input.reverse()
print(summetadata(input))
