import sys

input = sys.stdin.readline

MAX = sys.maxsize

N, M = map(int, input().split())

graph = []

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A,B,C))

dp = [MAX] * (N+1)
dp[1] = 0

for i in range(N):
    for j in range(M):
        u, v, w = graph[j]
        if dp[u] != MAX and dp[v] > dp[u] + w:
            dp[v] = dp[u] + w
            if i == N-1: 
                print(-1)
                exit()

print(*[i if i != MAX else -1 for i in dp[2:]], sep='\n')