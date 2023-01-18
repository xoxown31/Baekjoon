def isthat(x):
    s = str(x)
    for i in range(2, len(s)):
        if int(s[i-1])-int(s[i-2]) != int(s[i])-int(s[i-1]):
            return False
    return True

n = int(input())
print(len([i for i in range(1, n+1) if isthat(i)]))
