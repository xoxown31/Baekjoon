import sys

input = sys.stdin.readline

N = int(input())

S = [input().strip() for _ in range(N)]

M = int(input())

A = [input().strip() for _ in range(M)]

i = 0
while S[i] != '?':
    i += 1

for j in range(M):
    if i == 0 or S[i-1][-1] == A[j][0]:
        if i == N-1 or S[i+1][0] == A[j][-1]:
            if A[j] not in S:
                print(A[j])