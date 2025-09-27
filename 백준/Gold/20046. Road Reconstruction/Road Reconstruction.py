import sys
import heapq

input = sys.stdin.readline

INF = 10**18

WALL = -1

isin = lambda i,j : 0 <= i < m and 0 <= j < n
iswall = lambda i,j : board[i][j] == WALL
canmove = lambda i,j : isin(i,j) and not iswall(i,j)

def dijkstra(start):
    
    dist= [[INF] * n for _ in range(m)]
    dist[start[0]][start[1]] = board[start[0]][start[1]]
    pq = [(board[start[0]][start[1]], start[0], start[1])]
    while pq:
        uw, ui, uj = heapq.heappop(pq)
        if uw > dist[ui][uj]: continue
        for di, dj in dij4:
            vi, vj = ui+di, uj+dj

            if not canmove(vi,vj):
                continue

            vw = uw+board[vi][vj]
            if dist[vi][vj] > vw:
                dist[vi][vj] = vw
                heapq.heappush(pq,(dist[vi][vj],vi, vj))
    return dist

m, n = map(int, input().split())

dij4 = [
    ( 1, 0),
    (-1, 0),
    (0,  1),
    (0, -1)
]

board = [[int(x) for x in input().split()] for _ in range(m)]

if board[0][0] == -1:
    print(-1)
    exit()

res = dijkstra((0,0))[-1][-1]

print(res if res < INF else -1)