import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

res = [0, 0, 0]

def f(x, y, n):
	for i in range(x, x+n):
		t = 1
		for j in range(y, y+n):
			if graph[i][j] != -1:
				t = 0
				break
		if t == 0:
			break
	else:
		return -1
	
	for i in range(x, x+n):
		t = 1
		for j in range(y, y+n):
			if graph[i][j] != 0:
				t = 0
				break
		if t == 0:
			break
	else:
		return 0
	
	for i in range(x, x+n):
		t = 1
		for j in range(y, y+n):
			if graph[i][j] != 1:
				t = 0
				break
		if t == 0:
			break
	else:
		return 1
	return 2
	

def solve(x, y, n):
	if n <= 0:
		return
	
	t = f(x,y,n)
	if t != 2:
		res[t] += 1
		return
	
	solve(x,y,n//3)
	solve(x+n//3,y,n//3)
	solve(x+2*n//3,y,n//3)
	solve(x,y+n//3,n//3)
	solve(x+n//3,y+n//3,n//3)
	solve(x+2*n//3,y+n//3,n//3)
	solve(x,y+2*n//3,n//3)
	solve(x+n//3,y+2*n//3,n//3)
	solve(x+2*n//3,y+2*n//3,n//3)
	
solve(0, 0, N)
	
print(res[-1])
print(res[0])
print(res[1])