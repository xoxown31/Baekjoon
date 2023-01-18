import sys

input = sys.stdin.readline

n = int(input())

s = []
ans = []
i = 1

for _ in range(n):

    x = int(input())

    while i <= x:
        s.append(i)
        ans.append('+')
        i += 1

    if s[-1] == x:
        s.pop()
        ans.append('-')
        
    else:
        print("NO")
        break

else:
    print(*ans, sep = '\n')
