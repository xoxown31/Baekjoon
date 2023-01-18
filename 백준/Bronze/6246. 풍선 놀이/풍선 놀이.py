N, Q = map(int, input().split())

s = set()
for _ in range(Q):
    L, I = map(int, input().split())
    s = s | set([x for x in range(L, N+1, I)])

print(N-len(s))
