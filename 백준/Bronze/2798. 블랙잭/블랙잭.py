import sys
import itertools
N, M = map(int, sys.stdin.readline().split())
d = 300000
for i in itertools.combinations(map(int, sys.stdin.readline().split()), 3):
    pd = M - sum(i)
    if pd >= 0 and pd < d:
        d = pd
print(M-d)