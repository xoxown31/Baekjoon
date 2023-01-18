import sys

input = sys.stdin.readline

K, L = map(int, input().split())

d = {}

l = []

for i in range(L):
    num = int(input())

    if num in d:
        l[d[num]] = -1

    l.append(num)
    d[num] = i

i = 0
j = 0
while i < K:

    while j < L:
        if l[j] != -1:
            print((8-len(str(l[j])))*'0' + str(l[j]))
            j += 1
            break
        j += 1
    
    i += 1
