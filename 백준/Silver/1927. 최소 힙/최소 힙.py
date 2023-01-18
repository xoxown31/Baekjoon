import heapq
import sys

input = sys.stdin.readline

l = []

N = int(input())

for i in range(N):
    x = int(input())

    if x == 0:
        if l:
            print(heapq.heappop(l))
        else:
            print(0)
    else:
        heapq.heappush(l, x)
