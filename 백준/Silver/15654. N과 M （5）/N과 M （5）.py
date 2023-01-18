N, M = map(int, input().split())

num_list = sorted([int(i) for i in input().split()])
visited = [False] * N

l = []
def dfs(count):
    if count == M:
        print(*l)
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        l.append(num_list[i])
        dfs(count + 1)
        l.pop()

        visited[i] = False

dfs(0)
