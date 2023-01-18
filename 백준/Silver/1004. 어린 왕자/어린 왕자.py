import sys
input = sys.stdin.readline

def isin(x1, y1, cx, cy, r):
    return (cx-x1)**2+(cy-y1)**2 < r**2

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    l = []
    c = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if isin(x1, y1, cx, cy, r) and isin(x2, y2, cx, cy, r):
            pass
        elif isin(x1, y1, cx, cy, r) or isin(x2, y2, cx, cy, r):
            c += 1
    print(c)
