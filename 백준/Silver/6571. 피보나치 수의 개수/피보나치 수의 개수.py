l = []
for i in range(1, 482):
    a = 0
    b = 1
    for j in range(i-1):
        a, b = b, a+b
    l.append(b)

l = sorted(list(set(l)))
while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    i = 0
    c = 0
    while True:
        if a <= l[i] <= b:
            c += 1
        if l[i] >= b:
            break
        i += 1

    print(c)
