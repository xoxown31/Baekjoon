def f(i):
 for j in e[i]*v[i]:
  v[i]=0
  if 0>d[j]or f(d[j]):d[j]=i;return 1
n,*a=map(int,open(0).read().split())
L=n+n-1
d=[-1]*L
r=k=0
e=[[]for _ in d]
for j in a:e[k//n+k%n]+=[n-1+k//n-k%n]*j;k+=1
while L:v=[1]*k;r+=f(L:=L-1)or 0
print(r)