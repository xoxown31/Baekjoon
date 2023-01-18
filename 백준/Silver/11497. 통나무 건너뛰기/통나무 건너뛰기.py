import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    L = [int(x) for x in input().split()]

    L.sort()

    l = L[::2] + list(reversed(L[1::2]))

    Answer = -1

    for i in range(N):
        Answer = max(abs(l[i-1] - l[i]), Answer)

    print(Answer)
