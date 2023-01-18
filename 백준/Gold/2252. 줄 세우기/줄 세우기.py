import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
inDegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
	A, B = map(int, input().split())
	inDegree[B] += 1
	graph[A].append(B)
	
q = deque()

for i in range(1, N+1):
	if inDegree[i] == 0:
		q.append(i)
		
res = []
while q:
	u = q.popleft()
	res.append(u)
	for v in graph[u]:
		inDegree[v] -= 1
		if inDegree[v] == 0:
			q.append(v)

print(*res)