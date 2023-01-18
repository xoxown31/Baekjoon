import sys
from collections import deque

input = sys.stdin.readline
dxy = [(0,1),(0,-1),(1,0),(-1,0)]

N = int(input())

visited = [[int(x) for x in input().strip()] for _ in range(N)]
res = []

for i in range(N):
	for j in range(N):
		if visited[i][j] == 0:
			continue
		
		visited[i][j] = 0
		
		q = deque()
		q.append((i,j))
		count = 1
		
		while q:
			ux, uy = q.popleft()
			
			for dx, dy in dxy:
				vx = ux + dx
				vy = uy + dy
				
				if 0 <= vx < N and 0 <= vy < N:
					if visited[vx][vy] == 1:
						q.append((vx,vy))
						count += 1
						visited[vx][vy] = 0
		
		res.append(count)

res.sort()
print(len(res))
for i in range(len(res)):
	print(res[i])