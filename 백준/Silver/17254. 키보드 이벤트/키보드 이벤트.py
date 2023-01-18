import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = []
for i in range(M):
    s = input().split()
    l.append((int(s[0]), int(s[1]), s[2]))

l.sort(key = lambda x: (x[1], x[0]))

for i in range(M):
    print(l[i][2], end='')
