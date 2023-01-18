while True:
    try:
        N, B, M = map(float, input().split())

        i = 0
        while N < M:
            N *= (100+B)/100
            i += 1

        print(i)
    except:
        break
