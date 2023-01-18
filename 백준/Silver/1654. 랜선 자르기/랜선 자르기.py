import sys

input = sys.stdin.readline

K, N = map(int, input().split())

l = [int(input()) for _ in range(K)]

ans = 1
start = 1
end = max(l) + 1

while start <= end:
    
    mid = (start + end) // 2

    #possible
    if sum([x//mid for x in l]) >= N:
        ans = max(mid, ans)
        start = mid + 1
    else:
        end = mid - 1

print(ans)
