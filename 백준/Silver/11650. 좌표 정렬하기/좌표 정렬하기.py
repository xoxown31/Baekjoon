import sys
input = sys.stdin.readline

N = int(input())

for i in sorted([tuple(map(int, input().split())) for _ in range(N)]):
    print('{} {}'.format(i[0], i[1]))