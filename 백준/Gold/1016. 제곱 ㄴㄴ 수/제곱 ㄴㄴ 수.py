m, M = map(int, input().split())

l = [0] * (M-m+1)

i = 2
ii = 4
while ii <= M:
    j = m // ii
    while j*ii <= M:
        if j*ii - m >= 0:
            l[j*ii-m] = 1
        j+=1
    i += 1
    ii = i*i

print(M-m+1-sum(l))
