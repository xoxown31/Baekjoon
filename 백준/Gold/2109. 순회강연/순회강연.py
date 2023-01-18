import heapq
import sys

input = sys.stdin.readline

n = int(input())

l = []

for _ in range(n):
    
    pay, day = map(int, input().split())

    l.append([day, pay])

l.sort()
    
queue = []
result = 0

for i in range(n):

    day, pay = l[i][0], l[i][1]

    result += pay
    heapq.heappush(queue, pay)

    if len(queue) > day:
        result += -heapq.heappop(queue)

print(result)
