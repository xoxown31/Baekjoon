N, M = map(int, input().split())

l = [int(x) for x in input().split()]
res = set()

def dfs(A, K):
    if K==M:
        res.add(tuple(A))
        return
    for i in range(N):
        if A and A[-1] > l[i]: continue
        dfs(A+[l[i]], K+1)

dfs([], 0)

for x in sorted(list(res)):
    print(*x)