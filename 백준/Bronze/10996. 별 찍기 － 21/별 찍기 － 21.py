n = int(input())

for i in range(n*2):
    for j in range(n):
        print(" " if (i+j)%2 else "*", end = '')
    print()
