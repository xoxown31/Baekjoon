def primes(m: int, n: int):
    l = [False, False] + [True] * (n-1)
    for i, e in enumerate(l):
        if e:
            for j in range(i*2, n+1, i):
                l[j] = False
    return [x for x, y in enumerate(l) if y and x>=m]

M, N = map(int, input().split())
for i in primes(M, N):
    print(i)
