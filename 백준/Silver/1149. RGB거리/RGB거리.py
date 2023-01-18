import sys

input = sys.stdin.readline

N = int(input())

r, g, b = map(int, input().split())

for i in range(N-1):
    t1, t2, t3 = map(int, input().split())
    r, g, b = t1 + min(g, b), t2 + min(r, b), t3 + min(r, g)

print(min(r, g, b))
