import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

for u in graph:
	graph[u].sort(reverse = True)
	
stack = [V]
visited = []

while stack:
	u = stack.pop()
	if u not in visited:
		visited.append(u)
		print(u, end=' ')
		stack += graph[u]

print()
		
for u in graph:
	graph[u].sort()
	
queue = deque([V])
visited = []

while queue:
	u = queue.popleft()
	if u not in visited:
		visited.append(u)
		print(u, end=' ')
		queue += graph[u]