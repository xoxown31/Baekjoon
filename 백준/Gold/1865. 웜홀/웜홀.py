import sys
input = sys.stdin.readline
 
 
def bellmanFord():
    global isPossible
 
    for i in range(1, N + 1):
        for u in range(1, N + 1):
            for w, v in link[u]:
                if dp[v] > w + dp[u]:
                    dp[v] = w + dp[u]
                    if i == N:
                        isPossible = False
                    
 
T = int(input())
 
for _ in range(T):
    N, M, W = map(int, input().split())
 
    INF = 2147483647
    dp = [INF for _ in range(N + 1)]
    link = [[] for _ in range(N + 1)]
 
    for _ in range(M):
        S, E, T = map(int, input().split())
 
        link[S].append((T, E))
        link[E].append((T, S))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
 
        link[S].append((-T, E))
    
    isPossible = True
    
    bellmanFord()
 
    print("NO" if isPossible else "YES")
