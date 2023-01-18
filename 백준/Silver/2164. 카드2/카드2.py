from collections import deque
d = deque(range(1, int(input())+1))

while len(d) > 1:
    d.popleft()
    d.rotate(-1)

print(d[0])
