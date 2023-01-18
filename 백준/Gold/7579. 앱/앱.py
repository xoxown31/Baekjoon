N, M = map(int, input().split())

m = [0] + [int(x) for x in input().split()]
c = [0] + [int(x) for x in input().split()]

dp = [[0] * (sum(c)+1) for _ in range(N+1)]

res = sum(c)

for i in range(1, N+1):
    byte = m[i]
    cost = c[i]

    for j in range(1, sum(c)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])
        if dp[i][j] >= M:
            res = min(j, res)

print(res)