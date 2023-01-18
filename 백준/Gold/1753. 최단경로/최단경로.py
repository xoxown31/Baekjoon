import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V, E = map(int, input().split())

INF = 10 * V + 1

K = int(input())

link = [[] for x in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())

    link[u].append((w, v))

q = []
dp = [INF] * (V+1)
dp[K] = 0
heappush(q, (0, K))
while q:

    uw, u = heappop(q)
    if dp[u] < uw:
        continue

    for vw, v in link[u]:
        vw += uw
        if dp[v] > vw:
            dp[v] = vw
            heappush(q, (vw, v))
            
for i in dp[1:]:
    print(i if i < INF else "INF")
