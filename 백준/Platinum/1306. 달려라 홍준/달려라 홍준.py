import sys
import math

input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = max(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return max(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

N, M = map(int, input().split())

l = [int(x) for x in input().split()]

height = math.ceil(math.log2(N))
t_size = 2 ** (height + 1)
tree = [0] * t_size

init(1, 0, N-1)

for i in range(M-1, N-M+1):

    print(query(1, 0, N-1, i-M+1, i+M-1), end = ' ')