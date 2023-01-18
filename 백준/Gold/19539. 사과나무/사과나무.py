N = int(input())

l = [int(x) for x in input().split()]

S = 0
count1 = 0
count2 = 0
for i in range(N):
    S += l[i]
    count1 += 1 if l[i]%2 == 1 else 0
    count2 += l[i]//2

if S%3 == 0 and count1 <= count2:
    print("YES")
else:
    print("NO")
