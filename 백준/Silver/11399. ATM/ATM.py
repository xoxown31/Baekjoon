input()
l = sorted([int(i) for i in input().split()])
print(sum([l[i]*(len(l)-i) for i in range(len(l))]))