import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	
	N, K = map(int, input().split())
	l = [0] + [int(x) for x in input().split()]
	graph = [[] for _ in range(N+1)]
	inDegree = [0] * (N+1)
	dp = [0] * (N+1)
	
	for _ in range(K):
		u, v = map(int, input().split())
		graph[u].append(v)
		inDegree[v] += 1
	
	q = deque()
	for i in range(1, N+1):
		if inDegree[i] == 0:
			q.append(i)
			dp[i] = l[i]
	
	while q:
		u = q.popleft()
		for v in graph[u]:
			inDegree[v] -= 1
			dp[v] = max(dp[v], dp[u]+l[v])
			if inDegree[v] == 0:
				q.append(v)
	
	print(dp[int(input())])