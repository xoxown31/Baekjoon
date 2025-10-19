import sys

input = sys.stdin.readline

N = int(input())

l = [int(x) for x in input().split()]

res = 0
i = 0
while i < N:
    j = i + 1
    while j < N and l[i] > l[j]:
        j += 1
    res = max(j-i, res)
    i = j

print(res)