def solution(n, results):
    dp = [[False]*n for _ in range(n)]
    for a, b in results:
        dp[a-1][b-1] = True
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] and dp[k][j]:
                    dp[i][j] = True
    
    answer = 0
    for i in range(n):
        if sum(dp[i][j]+dp[j][i] for j in range(n)) == n-1:
            answer += 1

    return answer