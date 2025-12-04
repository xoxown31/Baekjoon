N = int(input())
l = [int(x) for x in input().split()]

a, b, c, d = map(int, input().split())
d = {
    'x+y':a,
    'x-y':b,
    'x*y':c,
    'x//y if x > 0 else -(abs(x)//y)':d,
}

MAX = -float('inf')
MIN = float('inf')

def f(x, y):
    global MAX, MIN
    if x == N:
        MAX = max(y, MAX)
        MIN = min(y, MIN)
        return
    
    for i in d:
        if not d[i] > 0: continue
        d[i] -= 1
        f(x+1, eval(f'(lambda x,y:{i})({y}, {l[x]})'))
        d[i] += 1

f(1, l[0])

print(MAX)
print(MIN)