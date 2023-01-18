import sys
import heapq

input = sys.stdin.readline

l = []

N = int(input())

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if l:
            print(heapq.heappop(l)[1])
        else:
            print(0)
    else:
        heapq.heappush(l, (-x, x))