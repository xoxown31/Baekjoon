R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

dij = [(0,1),(0,-1),(1,0),(-1,0)]
isin = lambda i,j : 0 <= i < R and 0 <= j < C

def f(x): return 1 << (ord(x) - 65)

res = 1
stack = [(0, 0, 1, f(board[0][0]))]

while stack:
    ui, uj, uw, us = stack.pop()
    res = max(res, uw)

    if res == 26:  # 가지치기
        break

    for di, dj in dij:
        vi, vj = ui + di, uj + dj
        if not isin(vi, vj): continue
        bit = f(board[vi][vj])
        if us & bit: continue
        stack.append((vi, vj, uw + 1, us | bit))

print(res)