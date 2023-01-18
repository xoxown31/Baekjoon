from collections import Counter

l = sorted(sorted(Counter([input() for _ in range(int(input()))]).items()), key = lambda x : x[1], reverse = True)
print(l[0][0])
