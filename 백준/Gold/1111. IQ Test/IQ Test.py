N = int(input())
l = [int(x) for x in input().split()]

if N < 3:
    print(l[0] if N == 2 and l[0] == l[1] else 'A')
    exit()

a = int((l[2] - l[1]) / (l[1] - l[0])) if l[0] != l[1] else 0
b = l[1] - a * l[0]

for i in range(N-1):
    if l[i] * a + b != l[i+1]:
        print('B')
        exit()

print(l[-1] * a + b)