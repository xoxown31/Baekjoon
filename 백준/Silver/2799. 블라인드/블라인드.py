l = [0, 0, 0, 0, 0]
m, n = map(int, input().split())
for i in range(m):
    sl = []
    s = input()
    for a in range(4):
        s = input()
        sl += s.split()
    for j in range(n):
        sc = 0
        for b in range(4):
            if sl[b][5*j+1] == '*':
                sc += 1
        l[sc] += 1
print(l[0], l[1], l[2], l[3], l[4])