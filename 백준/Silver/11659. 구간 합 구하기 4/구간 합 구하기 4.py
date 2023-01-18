import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = list(map(int, input().split())) + [0]

for i in range(1, N):
	l[i] += l[i-1]
	
for _ in range(M):
	i, j = map(int, input().split())
	print(l[j-1]-l[i-2])