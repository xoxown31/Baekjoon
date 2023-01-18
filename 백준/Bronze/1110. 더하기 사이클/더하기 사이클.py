N = int(input())
n = N
count = 0
while True:
    n = int(str(n)[-1] + str(sum(map(int, str(n if n >= 10 else n*10))))[-1])
    count += 1
    if N == n:
        break
print(count)