from collections import deque
import sys

input = sys.stdin.readline
MAX = sys.maxsize

dijk = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
isin = lambda i,j,k : 0 <= i < H and 0 <= j < N and 0 <= k < M
iswall = lambda i,j,k : board[i][j][k] == -1
canmove = lambda i,j,k : isin(i,j,k) and not iswall(i,j,k)

M, N, H = map(int, input().split())

board = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(H)]
visited = [[[MAX] * M for _ in range(N)] for _ in range(H)]

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                queue.append((i,j,k,0))
                visited[i][j][k] = 0

while queue:
    ui, uj, uk, uw = queue.popleft()
    
    for di, dj, dk in dijk:
        vi, vj, vk, vw = ui+di, uj+dj, uk+dk, uw+1
        
        if not canmove(vi,vj,vk): continue
        
        if vw < visited[vi][vj][vk]:
            visited[vi][vj][vk] = vw
            queue.append((vi,vj,vk,vw))

cansolve = True
day = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if not iswall(i,j,k):
                if visited[i][j][k] == MAX:
                    cansolve = False
                    day = -1
                    break
                day = max(day, visited[i][j][k])
        if not cansolve: break
    if not cansolve: break

print(day)