s = input().strip()

res = 0
j = -1
for i in range(13):
    if s[i].isdigit():
        res += int(s[i]) * [1, 3][i%2]
    else:
        j = i

res %= 10
print(((10 - res) % 10 * pow([1, 3][j%2], -1, 10)) % 10)
