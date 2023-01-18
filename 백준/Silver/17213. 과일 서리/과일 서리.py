def Com(n, r):
    if n//2 < r:
        r = n-r
    if r == 0:
        return 1
    l = [[0 for j in range(r+1)] for i in range(n+1)]
    for i in range(n+1):
        l[i][0] = 1

    for i in range(n+1):
        l[i][1] = i

    for i in range(1, n+1):
        for j in range(2, r+1):
            l[i][j] = l[i-1][j] + l[i-1][j-1]

    return l[n][r]
    
            
def Hom(n, r):
    return Com(n+r-1, r)

N = int(input())
print(Hom(N, int(input())-N))
