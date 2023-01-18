N = int(input())

l = [int(x) for x in input().split()]

dp = [0] * N

dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if l[j] < l[i]:
            dp[i] = max(dp[j], dp[i])
    dp[i] += 1

print(max(dp))
