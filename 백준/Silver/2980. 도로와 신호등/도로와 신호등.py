N, L = map(int, input().split())

l = []

for _ in range(N):
    D, R, G = map(int, input().split())

    l.append([D, R, G])

x = 0
time = 0
road = [True] * (L+1)

while x <= L:

    for i in range(N):
        D, R, G = l[i]
        
        if time % (R + G) < R:
            road[D] = False
        else:
            road[D] = True

    if road[x]:
        x += 1

    time += 1

print(time-1)
