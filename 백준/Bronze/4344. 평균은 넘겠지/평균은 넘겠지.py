for _ in range(int(input())):
    l = list(map(int, input().split()))[1:]
    avg = sum(l) / len(l)
    print("%.3f" % (len([i for i in l if i > avg])/len(l)*100) + '%')