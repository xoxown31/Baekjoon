from collections import deque

N = int(input())

board = [[int(x) for x in input().split()] for _ in range(N)]

dij = [(-1,0),(0,-1),(0,1),(1,0)]
isin = lambda i,j : 0 <= i < N and 0 <= j < N

def find(i, j, size):
    queue = deque([(i,j,0)])
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True

    res = []

    while queue:
        ui, uj, uw = queue.popleft()

        if 0 < board[ui][uj] < size:
            res.append((ui,uj,uw))
        
        for di, dj in dij:
            vi, vj, vw = ui+di, uj+dj, uw+1

            if not isin(vi, vj) or visited[vi][vj]: continue
            if board[vi][vj] > size: continue

            visited[vi][vj] = True
            queue.append((vi,vj,vw))

    return sorted(res, key = lambda x : (x[2], x[0], x[1]))

size = 2
eat = 0
time = 0

start = False
ui, uj = -1, -1
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            start = True
            ui, uj = i, j
            board[i][j] = 0
            break
    if start:
        break

while find(ui, uj, size):

    vi, vj, vw = find(ui, uj, size)[0]

    time += vw
    eat += 1

    if eat == size:
        size += 1
        eat = 0
    
    ui, uj = vi, vj
    board[vi][vj] = 0

print(time)