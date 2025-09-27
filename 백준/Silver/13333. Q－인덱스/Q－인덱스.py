import sys

input = sys.stdin.readline

N = int(input())
d = sorted([int(x) for x in input().split()])

print(max([k for k in range(N+1) if sum([i>=k for i in d])>=k]))