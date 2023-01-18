a, b = map(int, input().split())

def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1%n2)

print(gcd(a, b))
print(a*b//gcd(a, b))
