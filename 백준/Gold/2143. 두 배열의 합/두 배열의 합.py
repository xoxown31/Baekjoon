import bisect

T = int(input())

n = int(input())
A = [int(x) for x in input().split()]

m = int(input())
B = [int(x) for x in input().split()]

Asum = []
for i in range(n):
	s = 0
	for j in range(i,n):
		s += A[j]
		Asum.append(s)

Bsum = []
for i in range(m):
	s = 0
	for j in range(i,m):
		s += B[j]
		Bsum.append(s)

Asum.sort()
Bsum.sort()

res = 0
for i in range(n*(n+1)//2):
	l = bisect.bisect_left(Bsum, T-Asum[i])
	r = bisect.bisect_right(Bsum, T-Asum[i])
	res += r-l

print(res)