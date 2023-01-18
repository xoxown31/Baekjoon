N = int(input())
n = 0
while True:
    if N%5 != 0:
        N -= 3
        n += 1
    else:
        n += N//5
        break
    if N < 0:
        n = -1
        break
print(n)