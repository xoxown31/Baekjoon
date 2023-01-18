import sys
a, b = map(int, sys.stdin.readline().split())

l = []
for i in range(a+b):
    l.append(sys.stdin.readline().rstrip())

l.sort()
lc = []
for i in range(a+b-1):
    if l[i] == l[i+1]:
        lc.append(l[i])

print(len(lc))
for i in lc:
    print(i)