n, m = map(int, input().split())
l = [0] + list(map(int, input().split()))

s = 0
for i in range(len(l)):
    l[i] += l[i-1]

M = 0
for i in range(len(l)):
    M = (l[i] - l[i-m]) if M < (l[i] - l[i-m]) else M

print(M)