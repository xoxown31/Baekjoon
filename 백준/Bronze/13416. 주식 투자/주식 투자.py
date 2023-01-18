import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    S = 0

    for i in range(N):
        M = max(map(int, input().split()))
        if M > 0:
            S += M

    print(S)
