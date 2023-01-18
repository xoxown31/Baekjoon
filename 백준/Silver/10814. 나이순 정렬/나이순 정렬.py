import sys

input = sys.stdin.readline

N = int(input())

l = []

for i in range(N):
    age, name = input().split()

    l.append((int(age), i, name))

l.sort()

for i in range(N):
    print(" ".join((str(l[i][0]), l[i][2])))
