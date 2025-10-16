import sys

input = sys.stdin.readline

N = int(input())
l1 = sorted([int(x) for x in input().split()], reverse=True)

M = int(input())
l2 = sorted([int(x) for x in input().split()], reverse=True)

if l1[0] < l2[0]:
    print(-1)
    exit()

res = 0

while l2:
    res += 1

    for x1 in l1:
        for j in range(len(l2)):
            if x1 >= l2[j]:
                l2.pop(j)
                break

print(res)
