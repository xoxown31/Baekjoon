n = int(input())

dp = [n] * (100000+1)

dp[2] = dp[5] = 1
dp[4] = 2

for i in range(6, n+1):
    if dp[i-2] == n and dp[i-5] == n:
        dp[i] = n
    else:
        dp[i] = min(dp[i-2], dp[i-5]) + 1

print(dp[n] if dp[n] != n else -1)
