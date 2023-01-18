N = int(input())

dp = [False] * (1001)

dp[0] = dp[2] = False
dp[1] = dp[3] = dp[4] = True

for i in range(5, N+1):
    dp[i] = False if dp[i-1] and dp[i-3] and dp[i-4] else True

print("SK" if dp[N] else "CY")
