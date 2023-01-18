import sys

input = sys.stdin.readline

N, M = map(int, input().split())

link = []

dxy = [(1,0), (0,1), (-1,0), (0,-1)]

for i in range(N):
    line = input().strip()

    link.append([])

    for j in range(M):
        link[i].append(dxy["DRUL".find(line[j])])

count = 0
visited = [[0] * M for _ in range(N)]

def dfs(i, j):
    global count

    if visited[i][j] != 0:
        return

    count += 1

    stack = [(i,j)]
    visited[i][j] = count

    while stack:
        ui, uj = stack.pop()

        for di, dj in dxy:

            vi, vj = ui + di, uj + dj

            if (vi < 0 or vi >= N or vj < 0 or vj >= M) or visited[vi][vj] != 0:
                continue

            if link[vi][vj] == (-di,-dj) or link[ui][uj] == (di,dj):
                stack.append((vi, vj))
                visited[vi][vj] = count

for i in range(N):
    for j in range(M):
        dfs(i, j)

print(count)
