from collections import deque

N, K = map(int, input().split())

M = len(str(N))

visited = set([(N,0)])
queue = deque([(N,0)])
res = 0

while queue:
    n, k = queue.popleft()

    if k == K:
        res = max(n, res)
        continue

    n = list(str(n))

    for i in range(M-1):
        for j in range(i+1, M):
            if i==0 and n[j] == '0': continue

            n[i], n[j] = n[j], n[i]

            nn = int(''.join(n))

            if (nn, k+1) not in visited:
                queue.append((nn, k+1))
                visited.add((nn, k+1))

            n[i], n[j] = n[j], n[i]

print(res if res else -1)