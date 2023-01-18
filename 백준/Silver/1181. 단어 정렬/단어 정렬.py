import sys
l = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    l.append(sys.stdin.readline().rstrip())
l = list(set(l))
N = len(l)
l.sort(key = lambda x:(len(x), x))
for i in range(N):
    print(l[i])