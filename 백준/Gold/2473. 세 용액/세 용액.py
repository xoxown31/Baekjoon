import sys

N = int(input())
l = sorted([int(x) for x in input().split()])

res = []
m = sys.maxsize

for i in range(N-2):
	p1 = i+1
	p2 = N-1
	
	while p1 < p2:
		t = l[i] + l[p1] + l[p2]
		if abs(t) <= abs(m):
			res = [l[i], l[p1], l[p2]]
			m = t
		if t < 0:
			p1 += 1
		elif t > 0:
			p2 -= 1
		else:
			print(*res)
			exit()

print(*res)