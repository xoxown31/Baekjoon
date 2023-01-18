N = int(input())
P = [0] + list(map(int, input().split()))

l = [0]*(N+1)

for i in range(1, N+1):
    l[i] = max([l[j] + P[i-j] for j in range(i)])

print(l[-1])
