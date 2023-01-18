import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = []

for i in range(N):
    l.append([int(x) for x in input().split()])

for i in range(N):
    for j in range(1, N):
        l[i][j] += l[i][j-1]

for i in range(1, N):
    for j in range(N):
        l[i][j] += l[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x:int(x)-1, input().split())
    s = l[x2][y2]
    for p in [(x2, y1-1, 1), (x1-1, y2, 1), (x1-1, y1-1, -1)]:
        if p[0] < 0 or p[1] < 0:
            continue
        s -= l[p[0]][p[1]] * p[2]

    print(s)
