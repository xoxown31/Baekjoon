import sys

input = sys.stdin.readline

MOD = 10 ** 9 + 7

N, K = map(int, input().split())

A = [int(x) for x in input().split()]

c = [0] * K

for a in A:
    c[a%K] += 1

res = 1
for i in range(1, (K+1) // 2):
    res = res * (pow(2, c[i], MOD) + pow(2, c[K-i], MOD) - 1) % MOD

res = res * (c[0] + 1) % MOD
if K % 2 == 0:
    res = res * (c[K//2] + 1) % MOD
res = (res - (N+1)) % MOD

print(res)