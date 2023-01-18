N = int(input())

l = set([int(x) for x in input().split()])

M = int(input())

for i in input().split():
    if int(i) in l:
        print(1)
    else:
        print(0)
