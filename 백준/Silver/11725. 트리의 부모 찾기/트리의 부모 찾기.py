import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

link = [[] for i in range(N+1)]

for i in range(N-1):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)

l = [0] * (N+1)
q = deque([1])

while q:
    u = q.popleft()

    for v in link[u]:
        if l[v] != 0:
            continue

        l[v] = u
        q.append(v)

for i in range(2, N+1):
    print(l[i])
