import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = [i+1 for i in range(N)]
visited = [False] * N
l = []

def combi(count):
    if count == M:
        print(*l)
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        l.append(data[i])
        combi(count + 1)
        l.pop()

        for j in range(i+1, N):
            visited[j] = False
        
combi(0)
