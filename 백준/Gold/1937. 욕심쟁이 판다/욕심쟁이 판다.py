import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[1] * n for _ in range(n)]  # 최소 자기 자신은 방문 가능
dij = [(0,1),(0,-1),(1,0),(-1,0)]

l = []
for i in range(n):
    for j in range(n):
        l.append((board[i][j], i, j))

l.sort()  # 값 오름차순

res = 1
for val, i, j in l:
    for di, dj in dij:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] > val:
            dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)
            res = max(res, dp[ni][nj])

print(res)
