R, C = map(int, input().split())

board = [[x for x in input().strip()] for _ in range(R)]

isin = lambda i,j : 0 <= i < R and 0 <= j < C

dij = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0)
]

res = -1

stack = [(0, 0, 1, {board[0][0]})]

while stack:

    ui, uj, uw, us = stack.pop()

    res = max(uw, res)

    for di, dj in dij:

        vi, vj, vw = ui + di, uj + dj, uw + 1
        
        if not isin(vi,vj) or board[vi][vj] in us: continue

        stack.append((vi, vj, vw, us | {board[vi][vj]}))
    
print(res)