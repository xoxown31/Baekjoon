import sys

input = sys.stdin.readline

N, M  = map(int, input().split())

d = {}

for i in range(N):
	url, psw = input().split()
	d[url] = psw
	
for i in range(M):
	print(d[input().strip()])