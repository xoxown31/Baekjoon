import sys

input = sys.stdin.readline

res = "YES"

N, M = map(int, input().split())

l = []
for i in range(N):
    l.append([int(x) for x in input().split()])

l.sort()

for i in range(M):
    for j in range(N-1):
        if l[j][i] > l[j+1][i]:
            res = "NO"
            break
    if res == "NO":
        break

print(res)
