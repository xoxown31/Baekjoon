n, k = map(int, input().split())

def pactorial(n):
    if n <= 1:
        return 1
    return n * pactorial(n-1)

def combination(n, k):
    return pactorial(n) // (pactorial(k) * pactorial(n-k))

print(combination(n, k))
