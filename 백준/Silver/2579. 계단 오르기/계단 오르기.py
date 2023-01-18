import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * N

score = [int(input()) for _ in range(N)]

if N<3:
    if N==1:
        print(score[0])
    elif N==2:
        print(score[0]+score[1])
    exit()
    

dp[0] = score[0]
dp[1] = score[1] + dp[0]
dp[2] = score[2] + max(score[1], score[0])

for i in range(3, N):
    dp[i] = score[i] + max(dp[i-3] + score[i-1], dp[i-2])

print(dp[-1])
