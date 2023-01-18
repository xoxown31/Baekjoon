N, M = map(int, input().split())

heights = sorted([int(x) for x in input().split()])

ph = [0] * N
ph[0] = heights[0]
for i in range(1, N):
    ph[i] = heights[i] + ph[i-1]

def getTree(h):
    result = end = N
    start = 0

    while start <= end:
        mid = (start + end) // 2

        if heights[mid] < h:
            start = mid + 1
        else:
            end = mid - 1
            result = min(result, mid)

    if result >= N:
        return 0
    
    return ph[N-1] - ph[result] + heights[result] - h * (N-result)

result = start = 0
end = max(heights) + 1

while start <= end:
    mid = (start + end) // 2

    if getTree(mid) < M:
        end = mid - 1
    else:
        start = mid + 1
        result = max(mid, result)

print(result)