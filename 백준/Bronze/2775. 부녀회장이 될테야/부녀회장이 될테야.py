import sys

def P(n, r):
    res = 1
    for i in range(r):
        res *= n
        n -= 1
    return res

def C(n, r):
    return P(n, r)//P(r, r-1)

for _ in range(int(sys.stdin.readline().rstrip())):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(C(n+k, n-1))