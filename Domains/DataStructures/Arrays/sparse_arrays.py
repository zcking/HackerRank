from collections import defaultdict

strings = defaultdict(int)

for _ in range(int(input())):
    strings[input()] += 1
    
for _ in range(int(input())):
    print(strings[input()])

