def primes(m: int, n: int):
    l = [False]*2 + [True]*(n-1)
    for i, e in enumerate(l):
        if e:
            for j in range(i*2, n+1, i):
                l[j] = False
    return [x for x, y in enumerate(l) if y and x >= m]

while True:
    n = int(input())
    if n == 0:
        break
    print(len(primes(n+1, n*2)))
