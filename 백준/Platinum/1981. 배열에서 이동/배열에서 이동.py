from collections import deque
import sys

input = sys.stdin.readline
dij = [(1,0),(0,1),(-1,0),(0,-1)]
isin = lambda i,j : 0 <= i < n and 0 <= j < n

n = int(input())
l = [[int(x) for x in input().split()] for _ in range(n)]

MIN = sys.maxsize
MAX = -1

for i in range(n):
    for j in range(n):
        MAX = max(l[i][j], MAX)
        MIN = min(l[i][j], MIN)

def bfs(x):
    for m in range(MIN, MAX-x+1):
        if not m <= l[0][0] <= m+x: continue
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        queue = deque([(0,0)])
        while queue:
            ui, uj = queue.popleft()
            
            if ui == n-1 and uj == n-1:
                return True

            for di, dj in dij:
                vi, vj = ui+di, uj+dj

                if not isin(vi,vj) or visited[vi][vj]: continue
                if m <= l[vi][vj] <= m+x:
                    visited[vi][vj] = True
                    queue.append((vi,vj))

    return False

start, end = 0, MAX-MIN

while end - start > 0:
    mid = (end+start)//2
    if bfs(mid):
        end = mid
    else:
        start = mid+1

print(end)