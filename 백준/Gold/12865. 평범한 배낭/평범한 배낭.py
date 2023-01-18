import sys

input = sys.stdin.readline

N, K = map(int, input().split())

l = [[0, 0]]

for _ in range(N):
    W, V = map(int, input().split())
    l.append([W, V])

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for number in range(1, N+1):
    for weight in range(K+1):
        if weight >= l[number][0]:
            dp[number][weight] = max(dp[number-1][weight], dp[number-1][weight-l[number][0]] + l[number][1])
        else:
            dp[number][weight] = dp[number-1][weight]

print(dp[-1][-1])
