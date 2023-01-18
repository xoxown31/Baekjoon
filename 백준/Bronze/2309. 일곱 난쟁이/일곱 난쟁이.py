l = list(range(9))
s = 0
for i in range(9):
    l[i] = int(input())
    s += l[i]
for i in range(8):
    for j in range(i+1, 9):
        if l[i] + l[j] == s - 100:
            l[i] = 0
            l[j] = 0
            break
    if 0 in l:
        break
for i in sorted(l):
    if i != 0:
        print(i)