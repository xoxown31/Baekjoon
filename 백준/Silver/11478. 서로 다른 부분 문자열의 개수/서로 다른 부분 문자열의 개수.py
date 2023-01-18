s = input()
l = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        l.add(s[i:j])
print(len(l))
