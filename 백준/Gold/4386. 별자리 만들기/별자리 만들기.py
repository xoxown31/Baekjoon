import sys
import heapq

input = sys.stdin.readline

n = int(input())

X, Y = [], []

for _ in range(n):
	x, y = map(float, input().split())
	X.append(x)
	Y.append(y)
	
graph = [[] for _ in range(n)]

for i in range(n):
	for j in range(i+1, n):
		w = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** 0.5
		graph[i].append([w, j])
		graph[j].append([w, i])

visited = [False] * n
heap = [[0,0]]
count = 0
res = 0

while heap:
	if count == n:
		break
	w, s = heapq.heappop(heap)
	if not visited[s]:
		visited[s] = True
		res += w
		for i in graph[s]:
			heapq.heappush(heap, i)

print(round(res, 2))
