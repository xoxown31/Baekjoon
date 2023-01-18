import sys

input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    l.append([int(i) for i in input().split()])

dp = [[0 for j in range(i+1)] for i in range(n)]

dp[0][0] = l[0][0]

for i in range(1, n):
    dp[i][0] = l[i][0] + dp[i-1][0]
    dp[i][i] = l[i][i] + dp[i-1][i-1]
    for j in range(1, i):
        dp[i][j] = l[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[i]))