n, m = map(int, input().split())

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    
def combination(n, m):
    return factorial(n) // (factorial(n-m) * factorial(m))

if m >= n//2:
    m = n - m

print(combination(n, m))
