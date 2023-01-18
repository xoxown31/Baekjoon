import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = [[int(x) for x in input().split()] for _ in range(m)]

roots = [x for x in range(n)]

def find(x):
	if x!=roots[x]:
		roots[x] = find(roots[x])
	return roots[x]

ans = 0
for i, t in enumerate(l):
	s, e = t[0], t[1]
	sr, er = find(s), find(e)
	
	if sr == er:
		ans = i+1
		break
	
	if sr > er:
		roots[sr] = er
	
	else:
		roots[er] = sr
	
print(ans)