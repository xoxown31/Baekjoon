from collections import defaultdict

d = defaultdict(int)

N = int(input())

for x in input().split():
    d[int(x)] += 1

M = int(input())

for x in input().split():
    print(d[int(x)], end = ' ')

