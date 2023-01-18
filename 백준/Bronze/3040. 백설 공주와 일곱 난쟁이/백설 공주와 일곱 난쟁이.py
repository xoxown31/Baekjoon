from itertools import combinations

l = []
for _ in range(9):
    l.append(int(input()))

target = sum(l) - 100

for i in combinations(l ,2):
    if sum(i) == target:
        break

for j in l:
    if j not in i:
        print(j)
