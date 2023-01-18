import sys

input = sys.stdin.readline

N = int(input())

l = []
for i in range(N):
    l.append(input().strip())

for i in range(N):
    s1 = l[i][::-1]
    for j in range(i, N):
        s2 = l[j]
        b = s1 == s2
        if b:
            print(len(l[i]), l[i][len(l[i])//2])
            break
    if b:
        break
