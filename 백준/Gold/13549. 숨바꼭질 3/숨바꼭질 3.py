from collections import deque

N, K = map(int, input().split())

l = [-1 for _ in range(100001)]
l[N] = 0

queue = deque([N])

while queue:
    x = queue.popleft()
    if x == K:
        break

    if 0 <= 2*x <= 100000 and l[2*x] == -1:
        l[2*x] = l[x]
        queue.append(2*x)

    for nx in [x-1, x+1]:
        if not 0 <= nx <= 100000 or l[nx] != -1:
            continue

        l[nx] = l[x] + 1
        queue.append(nx)

print(l[x])
