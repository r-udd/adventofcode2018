import marble as m

inputs = [(9,25,32), (10,1618,8317), (13,7999,146373), (17,1104,2764), (21,6111, 54718), (30,5807,37305),(404,100*71852,-1)]
for input in inputs:
    points = [0] * input[0]
    marble0 = m.Marble(None, 0, None)
    marble1 = m.Marble(marble0, 1, marble0)
    marble0.prev = marble1
    marble0.next = marble1
    current = marble1
    player = 1
    for next in range(2, input[1] + 1):
        if next % 100000 == 0:
            print(next)
        if next % 23 == 0:
            for i in range (7):
                current = current.prev
            before = current.prev
            after = current.next
            points[player] += current.value + next
            before.next = after
            after.prev = before
            del current
            current = after
        else:
            current = current.next
            after = current.next
            new = m.Marble(current, next, after)
            current.next = new
            after.prev = new
            current = new
        player = (player + 1) %input[0]
    if max(points) != input[2]:
        print('actual', max(points), 'desired', input[2])