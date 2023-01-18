import sys

input = sys.stdin.readline

N = int(input())

l = [[int(x) for x in input().strip()] for _ in range(N)]

def f(i,j,n):
	
	t = l[i][j]
	for a in range(i,i+n):
		for b in range(j,j+n):
			if l[a][b] != t:
				t = -1
				break
		if t == -1:
			break
	
	if t == -1:
		print('(', end = '')
		n //= 2
		f(i,j,n)
		f(i,j+n,n)
		f(i+n,j,n)
		f(i+n,j+n,n)
		print(')', end = '')
	
	else:
		print(t, end='')

f(0,0,N)