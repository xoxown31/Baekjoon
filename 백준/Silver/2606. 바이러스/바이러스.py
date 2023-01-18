import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

link = [[] for i in range(N+1)]

visited = [1]

for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

stack = [1]

while stack:
    u = stack.pop()

    for v in link[u]:
        if v not in visited:
            visited.append(v)
            stack.append(v)

print(len(visited)-1)
