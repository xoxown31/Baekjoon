import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = ['']
d = {}
for i in range(1, N+1):
    name = input().strip()
    l.append(name)
    d[name] = i

for i in range(M):
    s = input().strip()
    if s.isdigit():
        print(l[int(s)])
    else:
        print(d[s])
