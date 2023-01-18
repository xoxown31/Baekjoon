import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	
	n = int(input())
	
	d = {}
	
	for _ in range(n):
		
		name, type = input().strip().split()
		
		if type in d:
			d[type] += 1
		else:
			d[type] = 1
			
	res = 1
	
	for type in d:
		res *= (d[type] + 1)
	
	print(res-1)