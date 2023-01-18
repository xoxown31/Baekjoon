n = int(input())
l = list(map(int, input().split()))

l.sort()

l = [l[i]-l[i-1] for i in range(1, n)]

res = 0

for i in range(n-1):
    res += (i+1)*(n-i-1)*l[i]

print(res*2)
