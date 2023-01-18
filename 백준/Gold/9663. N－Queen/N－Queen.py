N = int(input())

count = 0
col = [False] * N
inc = [False] * (2*N-1)
dec = [False] * (2*N-1)

def dfs(row):
    global count
    if row == N:
        count += 1
        return

    for i in range(N):
        if col[i] or inc[row + i] or dec[row - i]:
            continue

        col[i] = inc[row + i] = dec[row - i] = True

        dfs(row+1)

        col[i] = inc[row + i] = dec[row - i] = False

dfs(0)

print(count)
