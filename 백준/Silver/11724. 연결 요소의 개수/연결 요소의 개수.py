import sys

input = sys.stdin.readline

N, M = map(int, input().split())

link = [[] for i in range(N+1)]

visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())

    link[u].append(v)
    link[v].append(u)

def dfs(n):
    stack = [n]
    while stack:
        u = stack.pop()
        
        for v in link[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
res = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    dfs(i)
    res += 1

print(res)
