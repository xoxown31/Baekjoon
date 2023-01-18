from collections import deque
import sys

input = sys.stdin.readline
dij = [(0,1),(1,0),(0,-1),(-1,0)]
isin = lambda i,j : 0 <= i < N and 0 <= j < N

def bfs():
    visited = [[False] * N for _ in range(N)]
    res = 0
    
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            
            res += 1
            
            queue = deque([(i,j)])
            visited[i][j] = True
            
            while queue:
                ui, uj = queue.popleft()
                
                for di, dj in dij:
                    vi, vj = ui+di, uj+dj
                    
                    if not isin(vi,vj) or board[i][j] != board[vi][vj] or visited[vi][vj]: continue
                    
                    visited[vi][vj] = True
                    queue.append((vi,vj))
                    
    return res

N = int(input())

board = [[x for x in input().strip()] for _ in range(N)]

res = [bfs(), 0]
                
for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            board[i][j] = 'R'
            
res[1] = bfs()
        
print(*res)