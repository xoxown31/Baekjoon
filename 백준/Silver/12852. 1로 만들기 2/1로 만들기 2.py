N = int(input())

l = [[1000001, 0]] * (N+1)
l[1] = [0,1]

for i in range(1, N):
	l[i+1] = min(l[i+1], [l[i][0]+1, i])
	if 2*i <= N:
		l[2*i] = min(l[2*i], [l[i][0]+1, i])
	if 3*i <= N:
		l[3*i] = min(l[3*i], [l[i][0]+1, i])
		
print(l[N][0])
		
i = N
while True:
	print(i, end=' ')
	if i <= 1:
		break
	i = l[i][1]