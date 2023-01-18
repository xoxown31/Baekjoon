from itertools import permutations

X = input()

l = []

for t in permutations(X, len(X)):
    s = ''.join(t)
    if int(s) > int(X):
        l.append(int(s))

if len(l) > 0:
    print(sorted(l)[0])
else:
    print(0)
