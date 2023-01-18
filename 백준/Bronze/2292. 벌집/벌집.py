a = 1
b = 1
N = int(input())
i = 0
while True:
    if a <= N <= b:
        break
    a += 6*i
    b += 6*(i+1)
    i += 1
print(i+1)
