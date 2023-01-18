for _ in range(int(input())):
    R, S = input().split()
    for i in S:
        for j in range(int(R)):
            print(i, end = '')
    print()
