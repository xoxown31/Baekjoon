import sys

input = sys.stdin.readline
MAX = sys.maxsize

n = int(input())
m = int(input())

dp = [[MAX] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    dp[a][b] = min(c, dp[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dp[i][j] if dp[i][j] != MAX and i!=j else 0,end = ' ')
    print()