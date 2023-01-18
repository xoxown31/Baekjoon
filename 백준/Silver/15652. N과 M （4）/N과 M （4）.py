N, M = map(int, input().split())

l = []

def dfs(v):
	if len(l) == M:
		return print(*l)
	
	for i in range(v, N+1):
		l.append(i)
		dfs(i)
		l.pop()

dfs(1)