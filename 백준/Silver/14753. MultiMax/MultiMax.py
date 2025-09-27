import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

d = sorted([int(x) for x in input().split()])

res = max(d[0]*d[1]*d[-1], d[-3]*d[-2]*d[-1], d[-2]*d[-1], d[0]*d[1])

print(res)