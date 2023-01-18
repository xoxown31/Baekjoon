import sys
from collections import deque

input = sys.stdin.readline

def solve():
    p = input().strip()
    
    n = int(input())
    
    x = input().strip()[1:-1].split(',')
    if x[0] == '': x = []
    
    dq = deque(x)
    r = 1
    
    for c in p:
        if c=='R': r*=-1
        else:
            if not dq: return 'error'
            if r==1: dq.popleft()
            else: dq.pop()
            
    return '[' + ','.join(list(dq)[::r]) + ']'
    
T = int(input())

for _ in range(T):
    print(solve())
    