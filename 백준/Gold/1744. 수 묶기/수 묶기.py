import sys

input = sys.stdin.readline

N = int(input())
A, B, C = [], [], []

for _ in range(N):
    x = int(input())

    if x > 0:
        A.append(x)
    elif x < 0:
        B.append(x)
    else:
        C.append(x)

A.sort(reverse=True)
B.sort()

res = 0

i = 0
while i+1 < len(A) and A[i+1] > 1:
    res += A[i] * A[i+1]
    i += 2

while i < len(A):
    res += A[i]
    i += 1

j = 0
while j+1 < len(B):
    res += B[j] * B[j+1]
    j += 2

if j < len(B) and not C:
    res += B[j]

print(res)