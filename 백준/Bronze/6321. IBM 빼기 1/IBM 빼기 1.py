import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(T):

    print("String #" + str(test_case+1))
    print(''.join(chr(ord(c)+1) if ord(c) < ord('Z') else 'A' for c in input().strip()))
    print()