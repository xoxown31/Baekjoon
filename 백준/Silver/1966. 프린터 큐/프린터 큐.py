from collections import deque
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

for _ in range(int(input())):

    N, M = map(int, input().split())

    l = list(map(int, input().split()))
    queue = deque()
    heap = []

    for i, e in enumerate(l):
        queue.append((i, e))
        heappush(heap, (-e, e))

    count = 0
    while True:

        if queue[0][1] == heap[0][1]:
            heappop(heap)
            count += 1

            if queue.popleft()[0] == M:
                break

        else:
            queue.append(queue.popleft())

    print(count)
