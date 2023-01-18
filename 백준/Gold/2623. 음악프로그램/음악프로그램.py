from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
inDegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]


for _ in range(M):
	l = [int(x) for x in input().split()]
	for i in range(1, l[0]):
		inDegree[l[i+1]] += 1
		graph[l[i]].append(l[i+1])
		

q = deque()		
for i in range(1, N+1):
	if inDegree[i] == 0:
		q.append(i)

res = []
for _ in range(N):
	if not q:
		print(0)
		exit()
	u = q.popleft()
	res.append(u)
	for v in graph[u]:
		inDegree[v] -= 1
		if inDegree[v] == 0:
			q.append(v)

print(*res, sep='\n')