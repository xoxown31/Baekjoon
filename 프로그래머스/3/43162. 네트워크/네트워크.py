def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]: continue
        answer += 1
        stack = [i]
        visited[i] = True
        while stack:
            u = stack.pop()
            for v in [j for j in range(n) if computers[u][j] == 1 and not visited[j]]:
                stack.append(v)
                visited[v] = True
    return answer