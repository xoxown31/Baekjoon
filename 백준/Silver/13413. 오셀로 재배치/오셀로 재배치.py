import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    s1 = input().strip()
    s2 = input().strip()

    d = {'B':0, 'W':0}

    for i in range(N):
        if s1[i] == s2[i]:
            continue
        
        d[s1[i]] += 1

    print(max(d['B'], d['W']))
