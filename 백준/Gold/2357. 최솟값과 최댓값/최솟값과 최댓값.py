import sys
import math

input = sys.stdin.readline

def initMin(node, start, end):
    if start == end:
        treeMin[node] = l[start]
        return treeMin[node]
    
    treeMin[node] = min(initMin(node*2, start, (start+end)//2), initMin(node*2+1, (start+end)//2+1, end))
    return treeMin[node]

def initMax(node, start, end):
    if start == end:
        treeMax[node] = l[start]
        return treeMax[node]
    
    treeMax[node] = max(initMax(node*2, start, (start+end)//2), initMax(node*2+1, (start+end)//2+1, end))
    return treeMax[node]

def queryMin(node, start, end, left, right):
    if left > end or right < start:
        return 1e12
    
    if left <= start and right >= end:
        return treeMin[node]
    
    return min(queryMin(node*2, start, (start+end)//2, left, right), queryMin(node*2+1, (start+end)//2+1, end, left, right))
    
def queryMax(node, start, end, left, right):
    if left > end or right < start:
        return -1e12
    
    if left <= start and right >= end:
        return treeMax[node]
    
    return max(queryMax(node*2, start, (start+end)//2, left, right), queryMax(node*2+1, (start+end)//2+1, end, left, right))

N, M = map(int, input().split())

l = [int(input()) for _ in range(N)]
h = math.ceil(math.log2(N))
treeMin = [0] * 2 ** (h + 1)
treeMax = [0] * 2 ** (h + 1)

initMin(1, 0, N-1)
initMax(1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())

    print(queryMin(1, 0, N-1, a-1, b-1), queryMax(1, 0, N-1, a-1, b-1))