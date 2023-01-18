import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

l = sorted([int(input()) for _ in range(N)])

print(round(sum(l) / len(l)))
print(l[N//2])

common = Counter(l).most_common(2)

mod = common[0][0]
if len(common) > 1:
    if common[0][1] == common[1][1]:
        mod = common[1][0]

print(mod)
print(l[-1] - l[0])
