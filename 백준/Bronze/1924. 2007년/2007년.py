l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())

print(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'][(sum(l[:x-1]) + y-1)%7])