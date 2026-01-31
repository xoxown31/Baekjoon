import sys

input = sys.stdin.readline

N = int(input())

l = [int(x) for x in input().split()]

T, P = map(int, input().split())

res = 0
for x in l:
    res += (x-1) // T + 1

print(res)
print(N//P, N%P)