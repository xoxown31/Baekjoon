l = []
for _ in range(10):
    l.append((lambda i:i%42) (int(input())))
print(len(set(l)))