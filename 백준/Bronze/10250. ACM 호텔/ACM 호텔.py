import sys
for _ in range(int(sys.stdin.readline())):
    H, W, N = map(int, sys.stdin.readline().split())
    a, b = N%H, N//H+1
    if a == 0:
        a = H
        b = N//H
    print(a * 100 + b)