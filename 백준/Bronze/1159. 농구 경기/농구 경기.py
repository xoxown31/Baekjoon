l = []
for i in range(int(input())):
    l = l + list(input()[0])

cl = []
for i in l:
    if i not in cl:
        if l.count(i) >= 5:
            cl += list(i)

cl.sort()

if len(cl) == 0:
    print("PREDAJA")

else:
    for i in cl:
        print(i, end = '')