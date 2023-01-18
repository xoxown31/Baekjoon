T = int(input())

for i in range(T):
    
    N, D = map(int, input().strip().split())
    
    count = 0
    
    for j in range(N):
        
        v, f, c = map(int, input().strip().split())

        if D / v * c <= f:
            count += 1

    print(count)
