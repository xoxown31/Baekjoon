import sys

input = sys.stdin.readline

N = int(input())

X = [int(x) for x in input().split()]

l = [x for x in X]

l.sort()

d = {}

i = 0
count = 0
while i < N:

    while i < N - 1 and l[i] == l[i+1]:
        i += 1
        
    d[l[i]] = count
    count += 1
    i += 1

for i in range(N):
    l[i] = str(d[X[i]])

print(" ".join(l))
