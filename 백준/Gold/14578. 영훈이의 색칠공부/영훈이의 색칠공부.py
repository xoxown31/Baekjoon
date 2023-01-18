N = int(input())

p = 1000000007

d = [0] * (N+1)

f = 1
d[0] = 1
d[1] = 0

for i in range(2, N+1):
    f *= i
    f %= p
    d[i] = (i - 1) * (d[i - 1] + d[i - 2]) % p

print((f * d[N]) % p)