def primes_up_to(n: int) -> bool:
    l = [False, False] + [True] * (n-1)
    for (i, e) in enumerate(l):
        if e:
            for k in range(i*2, n+1, i):
                l[k] = False
    return [x for (x, y) in enumerate(l) if y]

l = primes_up_to(1000)
N = int(input())

count = 0
for i in map(int, input().split()):
    if i in l:
        count += 1

print(count)