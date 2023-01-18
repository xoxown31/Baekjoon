from collections import deque

N, K = map(int, input().split())

MAX = 100000

l = [0] * (MAX+1)

q = deque([N])

while q:
    a = q.popleft()

    if a == K:
        print(l[a])
        exit()

    for i in [a+1, a-1, a*2]:
        if 0 <= i <= MAX and not l[i]:
            l[i] = l[a] + 1
            q.append(i)
