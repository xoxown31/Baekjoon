import sys

sys.setrecursionlimit(50000)

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

l = [[0 for j in range(50)] for i in range(50)]

def dfs(x, y):
    l[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
            continue
        if l[ny][nx] == 1:
            dfs(nx, ny)
    

T = int(input())

for _ in range(T):

    count = 0
    
    M, N, K = map(int, input().split())
    
    for i in range(N):
        for j in range(M):
            l[i][j] = 0

    for __ in range(K):
        X, Y = map(int, input().split())
        l[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if l[i][j] == 1:
                dfs(j, i)
                count += 1
                
    print(count)
