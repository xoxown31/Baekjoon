import sys
n = 10000
l = [i for i in range(n+1)]
for i in range(n+1):
    a = i+sum(map(int, str(i)))
    if a <= n:
        l[a] = 0

for i in filter(lambda x:x!=0, l):
	sys.stdout.write(str(i) + '\n')
