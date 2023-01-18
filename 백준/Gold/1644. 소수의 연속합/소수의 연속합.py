N = int(input())

a = [1] * (N+1)
l = []
a[0] = a[1] = 0

for i in range(2, N+1):
	if a[i] == 0:
		continue
	
	l.append(i)
	for j in range(2*i, N+1, i):
		a[j] = 0

s = e = 0
res = 0

while e < len(l):
	if sum(l[s:e+1]) > N:
		s += 1
	elif sum(l[s:e+1]) < N:
		e += 1
	else:
		e += 1
		res += 1

print(res)