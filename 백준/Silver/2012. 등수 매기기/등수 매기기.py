import sys

input = sys.stdin.readline

N = int(input())

l = sorted([int(input()) for _ in range(N)])

s = 0
for i in range(N):
    s += abs(l[i] - (i+1))

print(s)