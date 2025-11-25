N = int(input())

A = [int(x) for x in input().split()]

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))