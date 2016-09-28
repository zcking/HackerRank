def array_left_rotation(a, n, k):
    a = list(a)
    return a[k:] + a[:k]
    

n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
