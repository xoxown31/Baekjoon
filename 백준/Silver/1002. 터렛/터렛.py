import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    d = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if d > r1 and d > r2:
        if d < r1 + r2:
            print(2)
        elif d == r1 + r2:
            print(1)
        else:
            print(0)
    else:
        if d == 0 and r1 == r2:
            print(-1)
        elif r1 >= r2:
            if r2 + d > r1:
                print(2)
            elif r2 + d == r1:
                print(1)
            else:
                print(0)
        elif r1 < r2:
            if r1 + d > r2:
                print(2)
            elif r1 + d == r2:
                print(1)
            else:
                print(0)
