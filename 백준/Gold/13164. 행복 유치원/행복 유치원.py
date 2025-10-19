import sys

input = sys.stdin.readline

N, K = map(int, input().split())

l = [int(x) for x in input().split()]

print(sum(sorted([l[i+1]-l[i] for i in range(N-1)])[:N-K]))