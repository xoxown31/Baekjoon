l = [tuple(int(i) for i in input().split())]
for _ in range(int(input())):
    l.append(tuple(map(int, input().split())))

a = min(l, key = lambda i: i[0]/i[1])
print(1000/a[1]*a[0])
