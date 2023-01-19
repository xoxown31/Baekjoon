T, P = input().rstrip(), input().rstrip()

n, m = len(T), len(P)

lps = [0] * m
i, j = 1, 0
while i < m:
    if P[i] == P[j]:
        j += 1
        lps[i] = j
        i += 1
    else:
        if j != 0: 
            j = lps[j-1]   
        else:
            lps[i] = 0
            i += 1

i = j = 0
res = []

while i < n:
    if P[j] == T[i]:
        i += 1
        j += 1
    else:
        if j != 0: j = lps[j-1]
        else: i += 1
    
    if j == m:
        res.append(i-j+1)
        j = lps[j-1]

print(len(res))
print(*res)