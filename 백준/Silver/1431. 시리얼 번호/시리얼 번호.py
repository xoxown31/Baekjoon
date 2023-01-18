def isbig(a, b):
    if len(a) != len(b):
        return len(a) > len(b)
    s1 = sum([int(i) for i in a if i.isdigit()])
    s2 = sum([int(i) for i in b if i.isdigit()])
    if s1 != s2:
        return s1 > s2
    return a > b

import sys
input = sys.stdin.readline

l = []
N = int(input())
for _ in range(N):
    l.append(input().rstrip())

for i in range(N-1):
    for j in range(N-1-i):
        if isbig(l[j], l[j+1]):
            l[j], l[j+1] = l[j+1], l[j]

for i in l:
    print(i)
