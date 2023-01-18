l = list(range(1, 21))

for i in range(10):
    a = tuple(map(int, input().strip().split()))
    l = l[:a[0]-1] + list(reversed(l[a[0]-1:a[1]])) + l[a[1]:]

for i in range(20):
    print(l[i], end = ' ')
