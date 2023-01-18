N, S = map(int,input().split())
l = list(map(int,input().split()))
i, j = 0, 0
s = l[0]
ans = 100001
 
while True:
    if s >= S:
        s -= l[i]
        ans = min(ans, j - i + 1)
        i += 1
    else:
        j += 1
        if j == N:
            break
        s += l[j]
 
print(0) if ans == 100001 else print(ans)
