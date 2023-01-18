from collections import deque
import sys

input = sys.stdin.readline

dij = [(0,1),(1,0),(0,-1),(-1,0)]
isin = lambda i,j : 0 <= i < h+2 and 0 <= j < w+2

def bfs(i,j):
    dq = deque([(i,j)])
    visited = [[-1] * (w+2) for _ in range(h+2)]
    visited[i][j] = 0
    while dq:
        ui, uj = dq.popleft()

        for di, dj in dij:
            vi, vj = ui+di, uj+dj

            if isin(vi,vj) and visited[vi][vj] == -1:
                if board[vi][vj] in '.$':
                    visited[vi][vj] = visited[ui][uj]
                    dq.appendleft((vi,vj))
                elif board[vi][vj] == '#':
                    visited[vi][vj] = visited[ui][uj] + 1
                    dq.append((vi,vj))
    return visited


T = int(input())

for _ in range(T):
    
    h, w = map(int, input().split())

    board = ['.'*(w+2)]+['.'+input().strip()+'.' for _ in range(h)]+['.'*(w+2)]

    l = []

    for i in range(1, h+1):
        for j in range(1, w+1):
            if board[i][j] == '$':
                l.append((i,j))
    
    a = bfs(l[0][0], l[0][1])
    b = bfs(l[1][0], l[1][1])
    c = bfs(0, 0)

    ans = sys.maxsize

    for i in range(h+2):
        for j in range(w+2):
            if a[i][j] != -1 and b[i][j] != -1 and c[i][j] != -1:
                t = a[i][j] + b[i][j] + c[i][j]
                if board[i][j] == '*': continue
                if board[i][j] == '#': t -= 2
                ans = min(ans, t)
    
    print(ans)          