vector_list = [[1,0],[0,1],[-1,0],[0,-1]]

for _ in range(int(input())):
    vi = 1
    d = [0, 0]
    minv = [0, 0]
    maxv = [0, 0]
    command_program = input()
    for command in command_program:
        v = vector_list[vi]
        if command == 'F':
            d[0], d[1] = d[0]+v[0], d[1]+v[1]
            minv[0] = d[0] if d[0] < minv[0] else minv[0]
            minv[1] = d[1] if d[1] < minv[1] else minv[1]
            maxv[0] = d[0] if d[0] > maxv[0] else maxv[0]
            maxv[1] = d[1] if d[1] > maxv[1] else maxv[1]
        elif command == 'B':
            d[0], d[1] = d[0]-v[0], d[1]-v[1]
            minv[0] = d[0] if d[0] < minv[0] else minv[0]
            minv[1] = d[1] if d[1] < minv[1] else minv[1]
            maxv[0] = d[0] if d[0] > maxv[0] else maxv[0]
            maxv[1] = d[1] if d[1] > maxv[1] else maxv[1]
        elif command == 'L':
            vi += 1
        elif command == 'R':
            vi -= 1
        if vi == 4:
            vi = 0
        elif vi == -1:
            vi = 3
    print((maxv[0]-minv[0])*(maxv[1]-minv[1]))
