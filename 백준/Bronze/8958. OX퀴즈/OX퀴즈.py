import sys
for _ in range(int(input())):
    c, s = 0, 0
    for i in sys.stdin.readline().rstrip():
        if i == 'O':
            c += 1
            s += c
        else:
            c = 0
    print(s)