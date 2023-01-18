for i in range(int(input())):
    t = ""
    for j in input():
        t += chr(ord(j)+1) if j != 'Z' else 'A'
    print("String #{}".format(i+1) + '\n' + t + '\n')
