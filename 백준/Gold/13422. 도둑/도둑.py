import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())

    if N == M:
        print(int(sum(map(int, input().split())) < K))
        continue

    l = [int(x) for x in input().split()] * 2

    for i in range(1, N*2):
        l[i] += l[i-1]

    count = 1 if l[M-1] < K else 0
    for i in range(1, N):
        if l[i+M-1] - l[i-1] < K:
            count += 1

    print(count)
