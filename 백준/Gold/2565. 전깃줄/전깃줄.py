import sys
input = sys.stdin.readline

N = int(input())

l = [[int(x) for x in input().split()] for _ in range(N)]

l.sort(key = lambda x : (x[0], -x[1]))

dp = [1] * N

for i in range(N):
	
	for j in range(i):
		if l[i][1] > l[j][1]:
			dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))