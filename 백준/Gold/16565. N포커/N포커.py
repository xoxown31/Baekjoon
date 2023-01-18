N = int(input())

dp = [[0] * 53 for _ in range(53)]
dp[0][0] = 1

for n in range(1, 53):
    for k in range(0 , n+1):
        dp[n][k] = (dp[n-1][k] + (dp[n-1][k-1] if k > 0 else 0)) % 10007

print(sum([(-1)**(i-1) * dp[13][i] * dp[52-4*i][N-4*i] for i in range(1, N//4+1)])%10007)