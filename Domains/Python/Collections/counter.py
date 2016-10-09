from collections import Counter

X = int(input())
sizes = Counter(map(int, input().split(' ')))
N = int(input())

earnings = 0

for _ in range(N):
    size, price = map(int, input().split(' '))
    if sizes[size] > 0:
        earnings += price
        sizes[size] -= 1
        
print(earnings)