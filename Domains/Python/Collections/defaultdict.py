from collections import defaultdict

n, m = tuple(map(int, input().split(' ')))
a = defaultdict(list)
b = []

for i in range(n):
    a[input()].append(str(i+1))
    
for i in range(m):
    b.append(input())
    
for let in b:
    if let in a:
        print(' '.join(a[let]))
    else:
        print('-1')

