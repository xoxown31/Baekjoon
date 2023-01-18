n = 1
X = int(input())

while n*(n+1)//2 < X:
    n += 1

d = X-n*(n-1)//2

if n%2==0:
    print('{}/{}'.format(d, n-d+1))
else:
    print('{}/{}'.format(n-d+1, d))
