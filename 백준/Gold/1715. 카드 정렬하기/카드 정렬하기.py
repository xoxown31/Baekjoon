from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    heappush(heap, int(input()))

res = 0

while len(heap) > 1:
    a, b = heappop(heap), heappop(heap)
    res += a+b
    heappush(heap, a+b)

print(res)