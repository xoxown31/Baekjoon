import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

l = [[0] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
	A, B = map(int, input().split())
	graph[A].append(B)
	graph[B].append(A)

res = []
for i in range(1, N+1):
	q = deque([i])
	visited = [False] * (N+1)
	while q:
		u = q.popleft()
		for v in graph[u]:
			if not visited[v]:
				visited[v] = True
				l[i][v] = l[i][u] + 1
				q.append(v)
	res.append(sum(l[i]))

print(min([i+1 for i in range(N)], key = lambda x : res[x-1]))