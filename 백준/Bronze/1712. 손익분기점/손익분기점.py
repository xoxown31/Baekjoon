import sys
a, b, c = map(int, sys.stdin.readline().split())
d = c-b
if d > 0:
    print(int(a/(c - b) + 1))
else:
    print(-1)