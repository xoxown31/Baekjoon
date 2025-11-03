import sys

input = sys.stdin.readline

MAX = sys.maxsize

N = int(input())

board = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[0] * (1 << N) for _ in range(N+1)]

def dfs(i, visited):
    if visited == 2**N - 1:
        return board[i][0] if board[i][0] else MAX
    
    if dp[i][visited]:
        return dp[i][visited]
    
    t = MAX
    
    for j in range(N):
        if visited & 1 << j or not board[i][j]:
            continue
        
        t = min(board[i][j] + dfs(j, visited + (1 << j)), t)
    
    dp[i][visited] = t
    return t

print(dfs(0, 1))