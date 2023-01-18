l = [tuple(map(int, input().split())) for _ in range(int(input()))]

for i in l:
    c = 1
    for j in l:
        c += 1 if i[0] < j[0] and i[1] < j[1] else 0
    print(c, end = ' ')