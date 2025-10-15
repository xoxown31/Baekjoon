import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())

l = [[int(x) for x in input().split()] for _ in range(N)]
l.sort(reverse=True)

heap = []

for x in l:
    heappush(heap, (-x[1], x[0]))

res = 0
for i in range(N):
    while heap and l[i][0] < -heappop(heap)[0]:
        res += 1

print(res)