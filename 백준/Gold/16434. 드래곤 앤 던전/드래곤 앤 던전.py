import sys
from math import ceil

input = sys.stdin.readline

N, atk = map(int, input().split())

cur = mx = 0

for _ in range(N):
    t, a, h = map(int, input().split())

    if t == 1:
        dmg = a * (ceil(h / atk) - 1)
        if dmg > cur:
            mx += dmg - cur
            cur = 0
        else:
            cur -= dmg
    else:
        atk += a
        cur = min(cur + h, mx)

print(mx + 1)
