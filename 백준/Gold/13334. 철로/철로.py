import sys
import heapq

input = sys.stdin.readline

n = int(input())
l = sorted([sorted([int(x) for x in input().split()]) for _ in range(n)], key=lambda x:x[1])
d = int(input())

res = 0
heap = []
for x in l:
    if x[1]-x[0] > d: continue
    while heap and x[1] - heap[0][0] > d:
        heapq.heappop(heap)
    heapq.heappush(heap, x)
    
    res = max(len(heap), res)
    
print(res)