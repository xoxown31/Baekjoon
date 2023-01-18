N = int(input()) - 2

dp = [[[[0 for l in range(6)] for k in range(6)] for j in range(6)] for i in range(N)]

for i in range(6):
    dp[0][i][i][i] = 10000 + 1000*(i+1)

for i in range(6):
    for j in range(6):
        if i != j:
            dp[0][i][i][j] = 1000 + 100*(i+1)
            dp[0][i][j][i] = 1000 + 100*(i+1)
            dp[0][j][i][i] = 1000 + 100*(i+1)

for i in range(6):
    for j in range(6):
        for k in range(6):
            if i != j and j != k and k != i:
                dp[0][i][j][k] = 100*(max((i, j, k))+1)

for i in range(1, N):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                dp[i][j][k][l] = max((dp[0][j][k][l], sum(dp[i-1][k][l])/6))

s = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            s += dp[-1][i][j][k]

print(s/6/6/6)
