N = input()

l = [0] * 10
for i in N:
    l[int(i)] += 1

l[6] += l.pop()
l[6] = l[6]//2 if l[6]%2 == 0 else l[6]//2 + 1

print(max(l))