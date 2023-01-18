import heapq
import operator
import sys
import functools

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    
    x = int(input())
    
    if x == 0:
        print(functools.reduce(operator.mul, heapq.heappop(heap)) if heap else 0)
    
    else:
        heapq.heappush(heap, (abs(x), x//abs(x)))