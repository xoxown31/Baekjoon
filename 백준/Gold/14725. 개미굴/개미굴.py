import sys

input = sys.stdin.readline

def add(d, x):
    if not len(x): return
    
    if x[0] not in d:
        d[x[0]] = {}
    add(d[x[0]], x[1:])
    
def printTree(d, t):
    for i in sorted(d):
        print("--"*t+i)
        printTree(d[i], t+1)

N = int(input())

d = {}

for x in [input().split()[1:] for _ in range(N)]:
    add(d, x)

printTree(d, 0)