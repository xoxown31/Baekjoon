N = int(input())
fir = int(input())
l = []

for i in range(2, N+1):
    nex = 0 if fir == 1 else 1
    fir = nex
    
    if i%2 == 0:
        if i == 2:
            n2 = fir
        elif n2 != fir:
            print("Love is open door")
            exit()
        
    if i%3 == 0:
        if i == 3:
            n3 = fir
        elif n3 != fir:
            print("Love is open door")
            exit()

    l.append(fir)

for i in l:
    print(i)
