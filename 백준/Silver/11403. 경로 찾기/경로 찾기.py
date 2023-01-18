import sys

input = sys.stdin.readline

N = int(input())
dp = [[int(x) for x in input().split()] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = (dp[i][k] and dp[k][j]) or dp[i][j]

for i in range(N):
    print(*dp[i])