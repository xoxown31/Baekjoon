L = int(input())
N = int(input())

l = [0] * L
maxV1 = 0
maxI1 = -1

for i in range(1, N+1):
    P, K = map(int, input().split())

    if K-P+1 > maxV1:
        maxV1 = K-P+1
        maxI1 = i
    
    for j in range(P-1, K):
        if l[j] == 0:
            l[j] = i

maxV2 = 0
maxI2 = -1
for i in range(1, N+1):
    if maxV2 < l.count(i):
        maxV2 = l.count(i)
        maxI2 = i

print(maxI1)
print(maxI2)
