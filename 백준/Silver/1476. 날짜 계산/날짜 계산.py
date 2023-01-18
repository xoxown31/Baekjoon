a = list(map(int, input().split()))
b = [0, 0, 0]
i = 1
while True:
    b[0] %= 15
    b[1] %= 28
    b[2] %= 19
    for j in range(3):
        b[j] += 1
    if a == b:
        break
    i += 1

print(i)
