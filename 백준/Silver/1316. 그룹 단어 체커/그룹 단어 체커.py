import sys
L = []
for _ in range(int(sys.stdin.readline())):
    L.append(sys.stdin.readline())

res = 0
l = []
for i in L:
    s = ""
    j = 0
    while j < len(i):
        for k in range(j+1, len(i)):
            if i[j] != i[k]:
                s += i[j]
                j = k
                break
            if k == len(i)-1:
                break
            
        if i[j] in s:
            l.append(i)
            break
        
        if j == len(i)-1:
            break

print(len(L) - len(l))