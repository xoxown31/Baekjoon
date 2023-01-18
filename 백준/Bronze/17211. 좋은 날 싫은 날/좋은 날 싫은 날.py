N, fir = map(int, input().split())
l = [float(i) for i in input().split()]
l = [[l[0], l[1]], [l[2], l[3]]]

G = l[fir][0]
B = l[fir][1]

for i in range(N-1):
    G, B = (l[0][0]*G + l[1][0]*B, l[0][1]*G + l[1][1]*B)

print(round(G*1000))
print(round(B*1000))
