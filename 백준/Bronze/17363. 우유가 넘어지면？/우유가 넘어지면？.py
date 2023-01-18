import sys

input = sys.stdin.readline

d = {'.':'.', 'O':'O', '-':'|', '|':'-', '/':'\\', '\\':'/',
     '^':'<', '<':'v', 'v':'>', '>':'^'}

N, M = map(int, input().split())

l1 = []
for _ in range(N):
    l1.append(input().strip())

l2 = []
for i in range(M):
    s = ''
    for j in range(N):
        s += d[l1[j][i]]
    l2.append(s)

for i in range(M, 0, -1):
    print(l2[i-1])
