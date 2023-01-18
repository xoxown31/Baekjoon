N = int(input())
l = sorted([int(x) for x in input().split()])

p = 1000000007

def pow(n, r):
    if r <= 1:
        return n ** r % p
    if r%2 == 0:
        return pow(n,r//2) ** 2 % p
    else:
        return n * pow(n,r//2) ** 2 % p

print(sum([l[i] * (pow(2,i)-pow(2,N-i-1)) for i in range(N)])%p)