for _ in range(int(input())):
    n = int(input())
    l = [1, 2, 4]
    for i in range(3, n):
        l.append(sum(l[i-3:i]))
    print(l[n-1])
