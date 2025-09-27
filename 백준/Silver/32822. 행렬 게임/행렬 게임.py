import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
board1 = [[int(x) for x in input().split()] for _ in range(N)]
board2 = [[int(x) for x in input().split()] for _ in range(N)]
board = [[abs(board1[i][j]-board2[i][j]) for j in range(N)] for i in range(N)]

l = [int(x) for x in input().split()]
d = defaultdict(int)

for j in range(N):
    d[j] = max(board[i][j] for i in range(N))

res = 0
for j in l:
    res += d[j-1]

print(res)