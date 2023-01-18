import sys
import copy

input = sys.stdin.readline

S = set()

for _ in range(int(input())):
    I = input()

    if I[:2] == 'al':
        S = set([i+1 for i in range(20)])
    elif I[0] == 'e':
        S = set()
    else:
        s, x = I.split()
        x = int(x)
        
        if s[0] == 'c':
            print(int(x in S))
        elif s[0] == 't':
            if x in S:
                S -= set([x])
            else:
                S |= set([x])
        elif s[0] == 'r':
            S -= set([x])
        else:
            S |= set([x])
