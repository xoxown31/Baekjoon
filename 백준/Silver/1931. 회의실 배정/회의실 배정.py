import sys
input = sys.stdin.readline

N = int(input())

l = []
for _ in range(N):
    start, end = map(int, input().split())
    l.append((start, end))

l.sort(key = lambda i:i[0])
l.sort(key = lambda i:i[1])

end = 0
count = 0
for i in l:
    if end <= i[0]:
        count += 1
        end = i[1]

print(count)
