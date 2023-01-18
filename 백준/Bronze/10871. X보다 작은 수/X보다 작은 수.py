N, X = map(int, input().split())
for i in filter(lambda x:x<X, map(int, input().split())):
	print(i, end = ' ')