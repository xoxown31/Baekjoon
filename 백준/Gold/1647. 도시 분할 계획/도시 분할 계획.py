import sys
input = sys.stdin.readline

V, E = map(int, input().split())
roots = [x for x in range(V+1)]
l = sorted([[int(x) for x in input().split()] for _ in range(E)], key = lambda x : x[2])

def find(x):
	if x != roots[x]:
		roots[x] = find(roots[x])
	return roots[x]

ans = []
for s, e, w in l:
	sr = find(s)
	er = find(e)
	
	if sr != er:
		if sr > er:
			roots[sr] = er
		else:
			roots[er] = sr
		ans += [w]
		
print(sum(ans[:-1]))