import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    if len(s)%2:
        s *= 2

    a = ''
    b = ''

    for i in range(len(s)):
        if i%2:
            b += s[i]
        else:
            a += s[i]

    print(a)
    print(b)
