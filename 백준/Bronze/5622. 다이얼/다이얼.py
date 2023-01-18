D = {2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ'}

s = 0
for i in input():
    for j, k in enumerate(D.values()):
        if i in k:
            s += j + 3
            
print(s)