N = int(input())

dp1 = [False] * N
dp2 = [False] * (2*N + 1)
dp3 = [False] * (2*N + 1)

res = 0

def f(x):
    global res
    if x == N:
        res = res + 1
        return
    
    for i in range(N):
        if dp1[i] or dp2[x+i] or dp3[x-i]:
            continue

        dp1[i] = dp2[x+i] = dp3[x-i] = True
        f(x+1)
        dp1[i] = dp2[x+i] = dp3[x-i] = False

f(0)
print(res)