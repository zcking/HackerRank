from collections import defaultdict

N, Q = list(map(int, input().strip().split(' ')))

seq = defaultdict(list)
lastAns = 0

for s in range(Q):
    action, x, y = list(map(int, input().strip().split(' ')))
    index = (x ^ lastAns) % N
    
    if action == 1:
        seq[index].append(y)
    else:
        lastAns = seq[index][y % len(seq[index])]
        print(lastAns)