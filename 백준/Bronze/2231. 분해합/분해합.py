def sum_digit(num):
    res = 0
    for i in str(num):
        res += int(i)
    return res
n = int(input())
j = 0
for i in range(1, n):
    if i + sum_digit(i) == n:
        j = i
        break
print(j)