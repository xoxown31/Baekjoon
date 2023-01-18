import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    K = int(input())

    l = [int(x) for x in input().split()]

    dp = [[0] * K for _ in range(K)]

    for i in range(K-1):
        dp[i][i+1] = l[i] + l[i+1]

    for i in range(K-3,-1,-1):
        for j in range(i+2, K):
            dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i,j)]) + sum(l[i:j+1])
    
    print(dp[0][K-1])