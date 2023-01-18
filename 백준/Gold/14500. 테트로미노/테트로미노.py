dijs = [
    [(0,0),(0,-1),(0,-2),(0,-3)],
    [(0,0),(-1,-1),(-1,0),(0,-1)],
    [(0,0),(-1,0),(-1,-1),(-1,-2)],
    [(0,0),(-1,0),(-1,-1),(-2,-1)],
    [(0,0),(0,-1),(1,0),(0,1)],
]

def rotate(dij):
    for i in range(4):
        dij[i] = (dij[i][1], -dij[i][0])

def reverse(dij):
    for i in range(4):
        dij[i] = (dij[i][0], -dij[i][1])
        
def match(dij, ui, uj):
    res = 0
    for di, dj in dij:
        vi, vj = ui+di, uj+dj
        if not isin(vi,vj):
            return -1
        res += board[vi][vj]
    return res
        
isin = lambda i,j : 0 <= i < N and 0 <= j < M
        
N, M = map(int, input().split())

board = [[int(x) for x in input().split()] for _ in range(N)]

res = -1

for i in range(N):
    for j in range(M):
        
        for k in range(5):
            
            for _ in range(2):
                reverse(dijs[k])
                for _ in range(4):
                    rotate(dijs[k])
                    
                    res = max(match(dijs[k], i, j), res)

print(res)