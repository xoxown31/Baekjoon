from heapq import heappush, heappop
from collections import deque
import sys

input = sys.stdin.readline

MAX = sys.maxsize
WALL = 0

isin = lambda i,j : 0 <= i < n and 0 <= j < n
iswall = lambda i,j : board[i][j] == WALL

dij = [
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1)
]

n = int(input())

board = [[int(x) for x in input().strip()] for _ in range(n)]

heap = []
dp = [[MAX] * n for _ in range(n)]

heappush(heap, (0,0,0))
dp[0][0] = True

while heap:

    uw, ui, uj = heappop(heap)

    if uw > dp[ui][uj]:
        continue

    for di, dj in dij:

        vi, vj = ui+di, uj+dj

        if not isin(vi,vj): continue

        vw = uw + (1 if iswall(vi,vj) else 0)

        if vw < dp[vi][vj]:
            dp[vi][vj] = vw
            heappush(heap, (vw, vi, vj))

print(dp[-1][-1])