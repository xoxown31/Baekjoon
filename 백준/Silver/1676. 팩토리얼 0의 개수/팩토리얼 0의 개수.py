import math

N = int(input())

s = str(math.factorial(N))

i = 0
while len(s) - i - 1 >= 0 and s[len(s)-i-1] == '0':
	i += 1

print(i)