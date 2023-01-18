import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = []
for _ in range(N):
    l.append(input().strip())

res = 50 * 50

for n in range(N-7):
    for m in range(M-7):
        for k in range(2):
            count = 0
            for i in range(8):
                for j in range(8):
                    if l[n+i][m+j] != "WB"[(i+j+k)%2]:
                        count += 1
            res = min(res, count)

print(res)
