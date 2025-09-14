import sys
from collections import deque

input = sys.stdin.readline
MAX = sys.maxsize

isin = lambda i,j : 0 <= i < l and 0 <= j < l
canmove = lambda i,j : isin(i,j)

dij = [
    ( 2, 1), ( 2, -1),
    (-2, 1), (-2, -1),
    (1,  2), (-1,  2),
    (1, -2), (-1, -2)
]

T = int(input())

for _ in range(T):
    l = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    visited = [[False] * l for _ in range(l)]
    queue = deque()

    visited[si][sj] = True
    queue.append((si,sj,0))

    res = MAX

    while queue:
        ui, uj, uw = queue.popleft()
        
        if ui == ei and uj == ej:
            res = min(uw, res)

        for di, dj in dij:
            vi, vj, vw = ui+di, uj+dj, uw+1

            if not canmove(vi, vj) or visited[vi][vj]: continue

            visited[vi][vj] = True
            queue.append((vi,vj,vw))

    print(res)