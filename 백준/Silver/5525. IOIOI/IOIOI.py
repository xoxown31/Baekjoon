import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

i = 0
count = 0
res = 0
while i < M-2:
    if S[i:i+3] == 'IOI':
        count += 1
        if count == N:
            res += 1
            count -= 1
        i += 2
    else:
        count = 0
        i += 1

print(res)