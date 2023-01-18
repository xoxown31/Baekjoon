import sys

input = sys.stdin.readline
    
N = int(input())

l = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for i in range(N-1):
    dp[i][i+1] = l[i][0] * l[i][1] * l[i+1][1]

for i in range(N-3,-1,-1):
    for j in range(i+2, N):
        dp[i][j] = min([dp[i][k] + dp[k+1][j] + l[i][0] * l[k][1] * l[j][1] for k in range(i,j)])

print(dp[0][N-1])