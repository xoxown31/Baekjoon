n = int(input())
res = [0 for i in range(10)]
point = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            res[int(i)] += point
        n -= 1
    if n < 10:
        for i in range(n + 1):
            res[i] += point
        res[0] -= point
        break
    else:
        for i in range(10):
            res[i] += (n // 10 + 1) * point
    res[0] -= point
    point *= 10
    n //= 10
print(*res)