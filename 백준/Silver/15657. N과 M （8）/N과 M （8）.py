N, M = map(int, input().split())
a = sorted(list(map(int, input().split())))

l = []

def dfs(v):
	if len(l) == M:
		return print(*l)
	
	for i in range(v, N):
		l.append(a[i])
		dfs(i)
		l.pop()

dfs(0)