from math import ceil, log
import sys

input = sys.stdin.readline
MAX = sys.maxsize

def min(a:list, b:list):
    return b if a[0] > b[0] else a

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    
    mid = (start+end)//2
    tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def search(node, start, end, left, right):
    if start > right or end < left:
        return [MAX, MAX]
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start+end)//2
    return min(search(node*2, start, mid, left, right), search(node*2+1, mid+1, end, left, right))

def update(node, start, end, index, x):
    if index < start or index > end:
        return [MAX,MAX]
    
    if start == end:
        tree[node] = x
        return
    
    mid = (start + end) // 2
    update(node * 2, start, mid, index, x)
    update(node * 2 + 1, mid + 1, end, index, x)

    tree[node] = min(tree[node * 2], tree[node * 2 + 1])

    

N = int(input())

A = [int(x) for x in input().split()]
l = [[A[i], i+1] for i in range(N)]

tree = [0] * (1 << (int(ceil(log(N, 2))) + 1))
init(1, 0, N-1)

M = int(input())

for _ in range(M):
    a, b, c = map(int, input().split())
    
    if a==1:
        l[b-1][0] = c
        update(1,0,N-1,b-1,l[b-1])
    
    else:
        print(search(1,0,N-1,b-1,c-1)[1])
    
