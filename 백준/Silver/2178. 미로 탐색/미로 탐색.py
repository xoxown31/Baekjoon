import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

l = [[int(x) for x in input().strip()] for _ in range(N)]

queue = deque()
queue.append([0,0])
dxy = [(0,1), (0,-1), (1,0), (-1,0)]

while queue:
	u = queue.popleft()
	i, j = u
	
	for dx, dy in dxy:
		x = i + dx
		y = j + dy
		
		if x >= 0 and x < N and y >= 0 and y < M:
			if l[x][y] > 0 and l[x][y] == 1:
				l[x][y] = l[i][j] + 1
				queue.append([x,y])

print(l[-1][-1])