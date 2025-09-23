from itertools import combinations
from collections import defaultdict

board = [[x for x in input().strip()] for _ in range(5)]

isin = lambda i,j : 0 <= i < 5 and 0 <= j < 5

dij = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0)
]

l = []
for i in range(5):
    for j in range(5):
        l.append((i, j))

def f(l):
    if sum(board[i][j] == 'S' for i, j in l) < 4:
        return False

    si, sj = l[0]

    stack = []
    visited = [[True] * 5 for _ in range(5)]
    
    stack.append((si, sj))
    for ui, uj in l[1:]:
        visited[ui][uj] = False

    res = 0

    while stack:

        ui, uj = stack.pop()

        res += 1

        for di, dj in dij:

            vi, vj = ui + di, uj + dj

            if not isin(vi,vj) or visited[vi][vj]: continue

            stack.append((vi, vj))
            visited[vi][vj] = True

    return res == 7

res = 0

for x in combinations(l, 7):
    res += 1 if f(x) else 0

print(res)