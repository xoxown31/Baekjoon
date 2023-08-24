from bisect import bisect_right

def f(s):
    h, m = s.split(':')
    return 60 * (int(h)) + int(m)

def g(t):
    h, m = t//60, t%60
    return f'{h:02}:{m:02}'

def solution(n, t, m, timetable):
    l = sorted([f(x) for x in timetable])
    for i in range(n-1):
        bus = f("09:00") + t * i
        index = bisect_right(l, bus)
        l = l[min(m,index):index] + l[index:]
        print(bus, l)
    last_bus = f("09:00") + t * (n-1)
    index = bisect_right(l, last_bus)
    l = l[:min(index, m)]
    print(last_bus, l)
    return g(last_bus if len(l) < m else l[-1]-1)