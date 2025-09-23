dp = [[1005] * 2005 for _ in range(1005)]

M = -1

for _ in range(int(input())):

    T, A, B = map(int, input().split())
    M = max(T, M)
    for x in range(A+1, B):
        dp[T][x] = -1

dp[0][0] = 0

for t in range(M):
    for x in range(-t, t+1):
        if dp[t][x] == -1: continue

        if x > -1000:
            dp[t+1][x-1] = min(dp[t][x]+1, dp[t+1][x-1])
        if x < 1000:
            dp[t+1][x+1] = min(dp[t][x]+1, dp[t+1][x+1])
        dp[t+1][x] = min(dp[t][x], dp[t+1][x])

res = min(x for x in dp[M] if x > -1)
print(res if res != 1005 else -1)