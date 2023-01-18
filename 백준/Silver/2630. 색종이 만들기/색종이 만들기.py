import sys

input = sys.stdin.readline

N = int(input())

l = [[int(j) for j in input().split()] for i in range(N)]

count = [0, 0]

def condition(x, y, n):
    first = l[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if first != l[i][j]:
                return False
    count[first] += 1
    return True

def backtrack(x, y, n):
    if condition(x, y, n):
        return
    else:
        n //= 2
        backtrack(x, y, n)
        backtrack(x+n, y, n)
        backtrack(x, y+n, n)
        backtrack(x+n, y+n, n)

backtrack(0, 0, N)
print(count[0])
print(count[1])
