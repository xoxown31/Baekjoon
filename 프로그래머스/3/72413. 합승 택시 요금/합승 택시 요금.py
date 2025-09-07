import sys

MAX = sys.maxsize

def solution(n, s, a, b, fares):
    dist = [[MAX]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
                
    answer = MAX
    for x in range(1, n+1):
        answer = min(dist[s][x] + dist[x][a] + dist[x][b], answer)
    
    return answer