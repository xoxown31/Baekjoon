from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline
dij = [(0,1),(1,0),(0,-1),(-1,0)]

isin = lambda i,j : 0 <= i < h and 0 <= j < w
iswall = lambda i,j : board[i][j] == 'x'
canmove = lambda i,j : isin(i,j) and not iswall(i,j)

def bfs(i, j):
    visited = [[0] * w for _ in range(h)]
    visited[i][j] = 1
    queue = deque([(i,j)])
    while queue:
        ui, uj = queue.popleft()

        for di, dj in dij:
            vi, vj = ui+di, uj+dj

            if canmove(vi,vj) and not visited[vi][vj]:
                queue.append((vi,vj))
                visited[vi][vj] = visited[ui][uj] + 1

    return visited

while True:
    w, h = map(int, input().split())

    if not w+h: break

    board = [list(input().strip()) for _ in range(h)]

    dusts = []

    for i in range(h):
        for j in range(w):
            if board[i][j] == 'o': dusts.insert(0, (i,j))
            elif board[i][j] == '*': dusts.append((i,j))
    
    dist = [[0] * len(dusts) for _ in range(len(dusts))]
    visited = bfs(dusts[0][0], dusts[0][1])
    ispossible = True

    for i in range(1, len(dusts)):
        t = visited[dusts[i][0]][dusts[i][1]]
        if not t:
            print(-1)
            ispossible = False
            break
        dist[0][i] = t-1
    
    if not ispossible: continue

    for i in range(len(dusts)-1):
        visited = bfs(dusts[i][0], dusts[i][1])
        for j in range(i+1, len(dusts)):
            dist[i][j] = visited[dusts[j][0]][dusts[j][1]] - 1
            dist[j][i] = dist[i][j]

    res = sys.maxsize
    for l in permutations(range(1, len(dist))):
        t = dist[0][l[0]]
        for i in range(len(l)-1):
            t += dist[l[i]][l[i+1]]
        res = min(res, t)
    print(res)