from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())

max_heap = []
min_heap = []

for i in range(N):
    a = int(input())

    if len(max_heap) == len(min_heap):
        heappush(max_heap, -a)
    else:
        heappush(min_heap, a)
    
    if min_heap and -max_heap[0] > min_heap[0]:
        heappush(max_heap, -heappop(min_heap))
        heappush(min_heap, -heappop(max_heap))

    print(-max_heap[0])