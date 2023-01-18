s = input()
for i in range(1, len(s)):
    a = b = 1
    for j in s[:i]:
        a *= int(j)
    for j in s[i:]:
        b *= int(j)
    if a==b:
        print("YES")
        break
else:
    print("NO")
