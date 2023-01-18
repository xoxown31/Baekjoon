l = list(map(int, input().split()))
if l[0] == 1:
    for i in range(8):
        if i+1 != l[i]:
            print("mixed")
            exit()
    print("ascending")
elif l[0] == 8:
    for i in range(8):
        if i+1 != l[-(i+1)]:
            print("mixed")
            exit()
    print("descending")
else:
    print("mixed")