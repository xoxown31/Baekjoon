N, M = map(int, input().split())

l = sorted([int(x) for x in input().split()] + [0])

p, m = l[-1:l.index(0):-1], l[:l.index(0)]

tuple_list = []

i = -1
for i in range(len(p)//M):
    tuple_list.append(p[M*i:M*(i+1)])

tuple_list.append(p[M*(i+1):] + [0] * (M-len(p)%M))

i = -1
for i in range(len(m)//M):
    tuple_list.append(m[M*i:M*(i+1)])

tuple_list.append(m[M*(i+1):] + [0] * (M-len(m)%M))

tuple_list.sort(key = lambda x:abs(x[0]))

s = abs(tuple_list[-1][0])

for i in range(len(tuple_list)-1):
    s += abs(tuple_list[i][0]) * 2

print(s)
