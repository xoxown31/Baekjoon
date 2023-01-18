import sys
import math
input = sys.stdin.readline

def init(node, start, end):

    if start == end:
        tree[node] = l[start]
        return tree[node]

    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2 + 1, (start+end)//2 + 1, end)
        return tree[node]

def query(node, start, end, left, right):

    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[node]

    return query(node*2, start, (start+end)//2, left, right) + query(node*2+1, (start+end)//2 + 1, end, left, right)

def update(node, start, end, index, diff):
    
    if index < start or index > end:
        return
    
    tree[node] += diff

    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2 + 1, (start+end)//2 + 1, end, index, diff)


N, M, K = map(int, input().split())

l = [int(input()) for _ in range(N)]
H = math.ceil(math.log2(N))
tree = [0] * (2 ** (H+1))

init(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - l[b-1]
        l[b-1] = c
        update(1, 0, N-1, b-1, diff)
    else:
        print(query(1, 0, N-1, b-1, c-1))