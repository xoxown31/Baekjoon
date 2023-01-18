import sys
input = sys.stdin.readline

N = int(input())

l = [int(x) for x in input().split()]

dp = [[0] * N for _ in range(N)]

for i in range(N):
	dp[i][i] = 1
for i in range(N-1):
	dp[i][i+1] = 1 if l[i] == l[i+1] else 0
for size in range(N-2):
	for i in range(N-2-size):
		j = i+2+size
		if l[i] == l[j] and dp[i+1][j-1] == 1:
			dp[i][j] = 1

M = int(input())

for _ in range(M):
	S, E = map(int, input().split())
	print(dp[S-1][E-1])