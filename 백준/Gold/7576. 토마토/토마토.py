import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())

l = []

q = deque()

for i in range(N):
    line = [int(x) for x in input().split()]
    l.append([])
    for j in range(M):
        l[i].append(line[j])
        if line[j] == 1:
            q.append((j, i))

while q:
    v = q.popleft()
    vx, vy = v[0], v[1]

    for i in range(4):
        nx, ny = vx+dx[i], vy+dy[i]

        if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
            continue

        if l[ny][nx] == 0:
            q.append((nx, ny))
            l[ny][nx] = l[vy][vx] + 1

m = 0
for i in range(N):
    for j in range(M):
        if l[i][j] == 0:
            print(-1)
            exit()
        if m < l[i][j]:
            m = l[i][j]

print(m-1)
