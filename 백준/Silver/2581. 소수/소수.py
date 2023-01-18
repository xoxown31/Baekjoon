def primes_up_to(m: int, n: int) -> bool:
    l = [False, False] + [True] * (n-1)
    for i, e in enumerate(l):
        if e:
            for j in range(i*2, n+1,i):
                l[j] = False
    return [x for x, y in enumerate(l) if y and x>=m]

M = int(input())
N = int(input())

l = primes_up_to(M, N)

if l:
    print(sum(l))
    print(min(l))
else:
    print(-1)
