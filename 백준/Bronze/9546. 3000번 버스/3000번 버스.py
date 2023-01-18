import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = 0
    for i in range(int(input())):
        a += 0.5
        a *= 2
    print(int(a))
