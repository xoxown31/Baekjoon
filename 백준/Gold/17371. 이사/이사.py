n=int(input())
a=[tuple(map(int, input().split()))for _ in range(n)]
print(*min((max((x-j)**2+(y-i)**2for j,i in a),x,y)for x,y in a)[1:])