N = int(input())
l = [int(i) for i in input().split()]

M = 0
s = 0
for i in range(1, len(l)):
    if l[i-1] < l[i]:
        s += l[i] - l[i-1]
    else:
        s = 0
    M = s if s>M else M

print(M)
