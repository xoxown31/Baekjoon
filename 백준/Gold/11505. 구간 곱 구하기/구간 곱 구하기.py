import sys
from math import *

p = 1000000007

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    
    mid = (start+end)//2
    tree[node] = (init(node*2, start, mid) * init(node*2+1, mid+1, end)) % p
    return tree[node]

def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return
    
    if start == end:
        tree[node] = val
        return
    
    mid = (start+end)//2
    update(node*2, start, mid, idx, val)
    update(node*2+1, mid+1, end, idx, val)
    tree[node] = (tree[node*2] * tree[node*2+1]) % p

def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start+end)//2
    return (query(node*2, start, mid, left, right) * query(node*2+1, mid+1, end, left, right)) % p

N, M, K = map(int, input().split())

l = [int(input()) for _ in range(N)]
h = ceil(log2(N))
tree = [0] * 2 ** (h+1)

init(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(query(1, 0, N-1, b-1, c-1))
