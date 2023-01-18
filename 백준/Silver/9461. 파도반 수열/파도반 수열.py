import sys

input = sys.stdin.readline

l = [0, 1, 1, 1, 2, 2]

for i in range(6, 101):
	l.append(l[i-1] + l[i-5])

T = int(input())

for _ in range(T):
	
	N = int(input())
	
	print(l[N])
	
	
	