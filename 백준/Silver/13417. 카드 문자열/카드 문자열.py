import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    l = input().split()

    s = l[0]

    for i in range(1, N):
        if l[i] > s[0]:
            s += l[i]
        else:
            s = l[i] + s

    print(s)
