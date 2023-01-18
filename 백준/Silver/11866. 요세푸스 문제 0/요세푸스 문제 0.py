from collections import deque
N, K = map(int, input().split())
d = deque(range(1, N+1))
l = []

while d:
    d.rotate(-(K-1))
    l.append(d.popleft())

print('<', end = '') 
for i in l[:-1]:
    print(i, end = ', ')
print(l[-1], end = '')
print('>')
