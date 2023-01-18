import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = [int(input()) for _ in range(N)]
count = 0

for i in reversed(l):
    if K // i > 0:
        count += K//i
        K -= i*(K//i)
    if K < 0:
        break

print(count)
