from collections import deque
import sys

input = sys.stdin.readline

WALL = 0

isin = lambda i,j : 0 <= i < N and 0 <= j < M
iswall = lambda i,j : board[i][j] == WALL
canmove = lambda i,j : isin(i,j) and not iswall(i,j)

dij = [
    (-1, 0),
    ( 1, 0),
    ( 0,-1),
    ( 0, 1)
]

N, M = map(int, input().split())

board = [[int(x) for x in input().strip()] for _ in range(N)]

queue = deque()
visited = [[False] * M for _ in range(N)]

queue.append((0, 0, 1))
visited[0][0] = True

while queue:
    ui, uj, uw = queue.popleft()

    if ui == N-1 and uj == M-1:
        print(uw)
        exit()

    for di, dj in dij:

        vi, vj, vw = ui+di, uj+dj, uw+1

        if not canmove(vi,vj) or visited[vi][vj]: continue

        queue.append((vi, vj, vw))
        visited[vi][vj] = True