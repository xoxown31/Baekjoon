import sys
from math import *

input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    mid = (start+end)//2
    tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return 1e10
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start+end)//2
    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))


N, M = map(int, input().split())

l = [int(input()) for _ in range(N)]
h = ceil(log2(N))
tree = [0] * 2 ** (h+1)

init(1, 0, N-1)

for _ in range(M):

    a, b = map(int, input().split())

    print(query(1, 0, N-1, a-1, b-1))