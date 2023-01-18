N = int(input())

l = list(range(N+1))

for i in range(1, N+1):
    l[i] += l[i-1]


res = 0

for i in range(1, N+1):
    res += l[N-(i-1)] + (l[N-(2*i-1)] if N-(2*i-1) > 0 else 0)

print(res)
