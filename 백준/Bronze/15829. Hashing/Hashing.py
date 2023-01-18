M, r = 1234567891, 31

L = int(input())
s = input()

res = 0

for i in range(L):
	res = (res + (ord(s[i]) - ord('a') + 1) * r ** i) % M

print(res)