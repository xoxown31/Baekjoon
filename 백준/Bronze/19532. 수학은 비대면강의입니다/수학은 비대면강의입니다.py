import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
x, y = 0, 0

if a == 0 and e == 0:
    y = c // b
    x = f // d

elif b == 0 and d == 0:
    x = c // a
    y = f // e

elif a == 0:
    y = c // b
    x = (f - e*y) // d

elif b == 0:
    x = c // a
    y = (f - d*x) // e

elif d == 0:
    y = f // e
    x = (c - b*y) // a

elif e == 0:
    x = f // d
    y = (c - a*x) // b

else:
    y = (c*d - a*f) // (b*d - a*e)
    x = (c - b*y) // a

print(x, y)
