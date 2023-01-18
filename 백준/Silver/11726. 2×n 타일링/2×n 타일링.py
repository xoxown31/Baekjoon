n = int(input())

f1, f2 = 1, 2

for i in range(n-1):
    f1, f2 = f2, f1 + f2

print(f1%10007)
