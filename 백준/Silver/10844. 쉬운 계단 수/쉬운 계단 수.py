N = int(input())

dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    dp = [dp[1]] + [dp[j-1] + dp[j+1] for j in range(1, 9)] + [dp[8]]

print(sum(dp)%1000000000)
