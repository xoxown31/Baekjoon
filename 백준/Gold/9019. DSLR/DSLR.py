from collections import deque
import sys

input = sys.stdin.readline
MAX = sys.maxsize

D = lambda n : (2*n) % 10000
S = lambda n : (n-1) if n != 0 else 9999
L = lambda n : (n * 10) % 10000 + n // 1000
R = lambda n : n//10 + (n%10) * 1000

DSLR = [D, S, L, R]

T = int(input())

for _ in range(T):
	
	A, B = map(int, input().split())
	
	visited = [False] * 10000
	queue = deque([(A, '')])
	visited[A] = ''
	
	while queue:
		u, uw = queue.popleft()
		
		for i in range(4):
			v, vw = DSLR[i](u), uw + "DSLR"[i]
			
			if visited[v] == False:
				visited[v] = vw
				queue.append((v, vw))
		
		if visited[B] != False:
			break
				
	print(visited[B])