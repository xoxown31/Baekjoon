import sys

BLUE = 1
RED = -1

def dfs(i):
    stack = [i]
    isit = True

    while stack:
        u = stack.pop()

        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = RED if visited[u] == BLUE else BLUE

            if visited[u] == visited[v]:
                return False
    return True

input = sys.stdin.readline

K = int(input())

for _ in range(K):

    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (V+1)
    isit = True
    for i in range(1, V+1):
        if visited[i]: continue
        visited[i] = RED
        if not dfs(i):
            isit = False
            break
    
    print("YES" if isit else "NO")

