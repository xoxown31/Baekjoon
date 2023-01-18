import sys

input = sys.stdin.readline

n = int(input())

l = [0] * 3 + [0] * n

for i in range(3, n+3):
    l[i] = int(input())

dp = [0] * 3 + [0] * n

for i in range(3, n+3):
    dp[i] = l[i] + max(l[i-1] + dp[i-3], dp[i-2])
    dp[i] = max(dp[i], dp[i-1])

print(max(dp))
