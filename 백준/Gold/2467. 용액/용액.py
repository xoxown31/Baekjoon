import sys
input = sys.stdin.readline
MAX = sys.maxsize

N = int(input())

l = [int(x) for x in input().split()]

s, e = 0, N-1
res = [MAX, (l[s], l[e])]

while s < e:
	res = min(res, [abs(l[s]+l[e]), (l[s],l[e])])
	
	if l[s]+l[e] > 0:
		e -= 1
	elif l[s]+l[e] < 0:
		s += 1
	else:
		break
	
print(*res[1])