import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    if N == 0:
        print(1, 0)
        continue
    f1 = [1, 0]
    f2 = [0, 1]
    for i in range(N-1):
        f1, f2 = f2, [f1[0]+f2[0], f1[1]+f2[1]]
    print(f2[0], f2[1])