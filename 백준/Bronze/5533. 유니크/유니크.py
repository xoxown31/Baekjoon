import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

l = []

for _ in range(N):
    l.append([int(x) for x in input().split()])

score = [0] * N

for i in range(3):

    d = defaultdict(int)

    for j in range(N):
        d[l[j][i]] += 1

    for j in range(N):

        if d[l[j][i]] == 1:

            score[j] += l[j][i]

for i in range(N):
    print(score[i])
