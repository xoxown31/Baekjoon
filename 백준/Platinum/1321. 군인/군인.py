import sys

sys.setrecursionlimit(500000)
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
    return tree[node]

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start+end)//2+1, end, left, right)

def update(node, start, end, index, diff):

    if index < start or index > end :
        return
 
    tree[node] += diff
    
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

def subSum_zero2n(x):
    return subSum(1, 0, N-1, 0, x)
    
N = int(input())

l = [int(x) for x in input().split()]

M = int(input())

tree = [0] * 5000000

init(1, 0, N-1)


for _ in range(M):

    line = [int(x) for x in input().split()]

    if line[0] == 1:
        i, a = line[1], line[2]
        update(1, 0, N-1, i-1, a)
    else:
        i = line[1]
        left = 0
        right = N
        while left < right:
            mid = (left+right)//2

            s = subSum_zero2n(mid)

            if s < i:
                left = mid+1

            else:
                right = mid
        print(right+1)
        
