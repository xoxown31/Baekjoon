from collections import defaultdict

N = int(input())

dp = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

while True:
    u, v = map(int, input().split())

    if u == v: break

    dp[u-1][v-1] = 1
    dp[v-1][u-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

l = list(max(dp[i]) for i in range(N))

print(min(l), l.count(min(l)))
print(*[x+1 for x in range(N) if l[x] == min(l)])