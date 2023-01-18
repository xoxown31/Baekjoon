import sys
from heapq import heappush, heappop

input = sys.stdin.readline

MAX = sys.maxsize

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    dest = sorted([int(input()) for _ in range(t)])

    dp = [MAX] * (n+1)
    dp[s] = 0

    queue = []
    heappush(queue, (0,0,s))
    passlist = [0] * (n+1)
    visited = [False] * (n+1)

    while queue:
        uw, ispass, u = heappop(queue)

        if visited[u]: continue

        visited[u] = True
        passlist[u] = ispass
        dp[u] = uw

        for vw, v in graph[u]:
            if not visited[v] and uw + vw <= dp[v]:
                dp[v] = uw + vw
                heappush(queue, (uw+vw, -1 if (u,v) in ((g,h),(h,g)) or ispass else 0, v))

    print(*[x for x in dest if passlist[x]==-1])
