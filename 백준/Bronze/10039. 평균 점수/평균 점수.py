l = []
for i in range(5):
    t = int(input())
    l.append(t if t>40 else 40)

print(sum(l)//5)
