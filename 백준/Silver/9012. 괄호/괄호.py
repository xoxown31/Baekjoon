import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):

    s = input().strip()

    l = []

    for c in s:
        if c == '(':
            l.append(c)
        else:
            if l:
                l.pop()
            else:
                l = [0]
                break

    if l:
        print("NO")
    else:
        print("YES")
