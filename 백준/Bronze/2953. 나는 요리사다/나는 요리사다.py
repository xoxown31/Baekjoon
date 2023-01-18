M = 0
for i in range(5):
    l = list(map(int, input().split()))

    s = l[0] + l[1] + l[2] + l[3]

    if s > M:
        M = s
        n = i

print(n+1, M)