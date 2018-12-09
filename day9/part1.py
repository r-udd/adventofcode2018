inputs = [(9,25,32), (10,1618,8317), (13,7999,146373), (17,1104,2764), (21,6111, 54718), (30,5807,37305),(404,71852,-1)]
for input in inputs:
    #print(input)
    points = [0] * input[0]
    current = 1
    marbles = [0,1]
    player = 1
    for next in range(2, input[1] + 1):
        if next % 23 == 0:
            current = (current - 7) % len(marbles)
            points[player] += marbles[current] + next
            del marbles[current]
        else:
            current = (current + 2) % len(marbles)
            marbles.insert(current, next)
        #print(marbles, next, 'player', player,'curr', current)
        player = (player + 1) %input[0]
    if max(points) != input[2]:
        print('actual', max(points), 'desired', input[2])