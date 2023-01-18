def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def f(n1, n2, n3):
    return lcm(lcm(n1, n2), n3)

l = [int(x) for x in input().split()]
m = 1000000
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            a = f(l[i], l[j], l[k])
            m = a if a < m else m

print(m)
