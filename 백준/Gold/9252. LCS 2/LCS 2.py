s1 = input().strip()
s2 = input().strip()

len1 = len(s1)
len2 = len(s2)

dp = [[0] * (len2+1) for _ in range(len1+1)]

for i in range(len1):
	for j in range(len2):
		if s1[i] == s2[j]:
			dp[i+1][j+1] = dp[i][j] + 1
		else:
			dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
	
print(dp[-1][-1])

if dp[-1][-1] == 0:
	exit()
	
lcs = ""
i = j = -1
while dp[i][j] > 0:
	if dp[i][j] == dp[i-1][j]:
		i -= 1
	elif dp[i][j] == dp[i][j-1]:
		j -= 1
	else:
		lcs += s1[i]
		i -= 1
		j -= 1

print(lcs[::-1])
		