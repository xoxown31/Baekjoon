import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()

res = 0

i = 0
while i < len(a) - len(b) + 1:
    j = 0
    while j < len(b) and a[i+j] == b[j]:    
        j += 1

    if j == len(b):
        i += j-1
        res += 1
    
    i += 1

print(res)