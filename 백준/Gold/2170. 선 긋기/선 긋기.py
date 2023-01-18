import sys

input = sys.stdin.readline

N = int(input())

l = sorted([list(map(int, input().split())) for _ in range(N)])

cur = [l[0][0], l[0][1]]
ans = 0

for i in range(1, N):
    if cur[1] >= l[i][0]:
        cur[1] = max(cur[1], l[i][1])

    else:
        ans += cur[1] - cur[0]
        cur = [l[i][0], l[i][1]]

ans += cur[1] - cur[0]
print(ans)