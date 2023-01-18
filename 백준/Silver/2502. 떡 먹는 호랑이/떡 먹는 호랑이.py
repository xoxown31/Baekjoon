D, K = map(int, input().split())

a1 = 1
a2 = 0

b1 = 0
b2 = 1

for _ in range(D-2):
    a1, a2 = a2, a1+a2
    b1, b2 = b2, b1+b2

d1 = 1
k = 0
while k != K:
    d2 = 1
    k = a2 * d1 + b2 * d2
    while k < K:
        k = a2 * d1 + b2 * d2
        d2 += 1

    d1 += 1

print(d1-1)
print(d2-1)
