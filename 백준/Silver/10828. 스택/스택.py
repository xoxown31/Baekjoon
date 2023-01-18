import sys

input = sys.stdin.readline

N = int(input())

l = []

for _ in range(N):
    s = input().strip()

    if s[:2] == "pu":
        l.append(int(s[4:]))
    elif s[0] == "p":
        if l:
            print(l.pop())
        else:
            print(-1)
    elif s[0] == "s":
        print(len(l))
    elif s[0] == "e":
        print(0 if l else 1)
    else:
        if l:
            print(l[-1])
        else:
            print(-1)