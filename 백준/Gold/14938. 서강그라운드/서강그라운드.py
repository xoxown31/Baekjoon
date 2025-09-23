from collections import defaultdict

n, m, r = map(int, input().split())

l = [int(x) for x in input().split()]

graph = defaultdict(list)
dp = [[float('inf')]*n for _ in range(n)]

for _ in range(r):
    u, v, w = map(int, input().split())

    dp[u-1][v-1] = w
    dp[v-1][u-1] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

res = 0

for i in range(n):
    t = l[i]
    for j in range(n):
        if i==j or dp[i][j] > m: continue
        t += l[j]
    res = max(t, res)

print(res)