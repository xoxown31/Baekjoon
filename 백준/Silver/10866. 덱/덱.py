import sys

input = sys.stdin.readline

N = int(input())

l = []

for _ in range(N):
    s = input().strip()

    if s[:2] == "pu":
        if s[5] == "f":
            l.insert(0, int(s[10:]))
        else:
            l.append(int(s[10:]))
            
    elif s[0] == "p":
        if l:
            if s[4] == "f":
                print(l.pop(0))
            else:
                print(l.pop())
        else:
            print(-1)
    elif s[0] == "s":
        print(len(l))
    elif s[0] == "e":
        print(0 if l else 1)
    else:
        if l:
            if s[0] == "f":
                print(l[0])
            else:
                print(l[-1])
        else:
            print(-1)
