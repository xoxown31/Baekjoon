import sys

input = sys.stdin.readline

p = 1000000007

factorial = [1] * 4000001
for i in range(1, 4000001): 
    factorial[i] = (factorial[i-1] * i) % p

def pow(n, r):
    if r <= 1:
        return n ** r % p
    if r%2 == 0:
        return pow(n,r//2) ** 2 % p
    else:
        return n * pow(n,r//2) ** 2 % p

M = int(input())

for _ in range(M):
    N, K = map(int, input().split())
    
    a = factorial[N]
    b = (factorial[K] * factorial[N-K]) % p
        
    print(a * pow(b, p-2) % p)