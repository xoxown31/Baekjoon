A = int(input())
B = input()
s = 0

for i, k in enumerate(reversed(B)):
    t = int(k) * A
    s += t * 10 ** i
    print(t)
print(s)