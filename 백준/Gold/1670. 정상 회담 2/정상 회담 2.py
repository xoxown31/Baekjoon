n = int(input(""))

dp = [0] * 10001
dp[0] = 1
dp[2] = 1
dp[4] = 2
i = 6
while(i <= n):
    total = 0
    for j in range(i//4): # n이 4의 배수던 아니던 공통이다
        j = j*2
        total = total + dp[j]*dp[i-j-2]*2

    if(i%4 == 2): # n이 4의 배수가 아닐때만 아래경우를 더해주어야한다
        total = total + dp[(i-2)//2]*dp[(i-2)//2]
    dp[i] = total%987654321
    i = i+2

print(dp[n])