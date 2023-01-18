import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = [[0 for j in range(2)] for i in range(6)]
for _ in range(N):
    j, i = map(int, input().split())
    l[i-1][j] += 1

res = 0
for i in range(6):
    for j in range(2):
        res += l[i][j]//K + (1 if l[i][j]%K != 0 else 0)

print(res)
