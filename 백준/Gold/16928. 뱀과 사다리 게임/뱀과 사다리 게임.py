from collections import deque
import sys

MAX = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

root = [i for i in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    root[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    root[u] = v
    
dp = [MAX] * 101

dp[0] = dp[1] = 0

queue = deque([(1,0)])

while queue:
    u, uw = queue.popleft()
    
    for d in range(u+1, min(u+7, 101)):
        v, vw = root[d], uw+1
        
        if v > 100: continue
        
        if vw < dp[v]:
            dp[v] = vw
            queue.append((v,vw))


        
print(dp[-1])