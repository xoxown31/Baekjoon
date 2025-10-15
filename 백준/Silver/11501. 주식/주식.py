import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())

    l = [int(x) for x in input().split()]

    res = 0
    i = 0

    for j, x in sorted(enumerate(l), key=lambda x:-x[1]):
        if i > j:
            continue
        if j == i:
            i += 1
            continue
        res += x * (j-i)

        while i < j:
            res -= l[i]
            i += 1
        i += 1
    print(res)