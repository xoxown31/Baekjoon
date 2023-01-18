import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	
	n = int(input())
	
	l = [[int(x) for x in input().split()] for _ in range(2)]
	
	if n == 1:
		print(max(l[0][0], l[1][0]))
		continue
	
	dp = [[l[i][j] for j in range(n)] for i in range(2)]
	dp[0][1] += dp[1][0]
	dp[1][1] += dp[0][0]
	
	for j in range(2, n):
		for i in range(2):
			dp[i][j] += max(dp[i-1][j-1], dp[i-1][j-2])
	
	res = 0
	for i in range(2):
		res = max(res, max(dp[i]))
	print(res)