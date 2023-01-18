D = {chr(i):0 for i in range(ord('a'), ord('z')+1)}
s = input().lower()
for i in s:
    D[i] += 1

L = sorted([(i, D[i]) for i in D.keys()], key = lambda x: x[1])

if L[-1][1] == L[-2][1]:
    print('?')
else:
    print(L[-1][0].upper())
