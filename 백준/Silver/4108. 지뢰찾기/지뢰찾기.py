while 1:

    array = []
    
    a, b = map(int ,input().strip().split())

    if a == 0 and b == 0:
        break
    
    for i in range(a):
        string = input()
        array.append([string[j] for j in range(b)])
    
    for i in range(a):
        for j in range(b):
            if array[i][j] == '.':
                array[i][j] = 0
    
    for i in range(a):
        for j in range(b):
            if array[i][j] == '*':
                if j < b-1 and array[i][j+1] != '*':
                    array[i][j+1] += 1
                if j > 0 and array[i][j-1] != '*':
                    array[i][j-1] += 1
                if i < a-1 and array[i+1][j] != '*':
                      array[i+1][j] += 1
                if i > 0 and array[i-1][j] != '*':
                    array[i-1][j] += 1
                if i < a-1 and j < b-1 and array[i+1][j+1] != '*':
                    array[i+1][j+1] += 1
                if i < a-1 and j > 0 and array[i+1][j-1] != '*':
                    array[i+1][j-1] += 1
                if i > 0 and j > 0 and array[i-1][j-1] != '*':
                    array[i-1][j-1] += 1
                if i > 0 and j < b-1 and array[i-1][j+1] != '*':
                    array[i-1][j+1] += 1

    for i in range(a):
        for j in range(b):
            print(array[i][j], end = '')
        print()