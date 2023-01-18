import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

total = 0

queue = [deque() for _ in range(21)]

for i in range(N):
    
    size = len(input().strip())
    
    while queue[size] and i - queue[size][0] > K:
        queue[size].popleft()
    
    total += len(queue[size])
    queue[size].append(i)
    
print(total)