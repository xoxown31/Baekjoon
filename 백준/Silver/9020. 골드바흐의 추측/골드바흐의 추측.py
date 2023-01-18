import sys
input = sys.stdin.readline

l = [False]*2 + [True]*(9999)
for i, e in enumerate(l):
    if e:
        for j in range(i*2, 10001, i):
            l[j] = False

for _ in range(int(input())):
    n = int(input())
    mid = n//2
    for i in range(n//2-1):
        if l[mid-i] and l[mid+i]:
            print(mid-i, mid+i)
            break
