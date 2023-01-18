S = input()
if S == '0':
    print('W')
    exit()
l = []
if S.count('-') > 0:
    if S.count('+') > 0:
        if S[::-1].find('-') < S[::-1].find('+'):
            f = S[::-1].find('-')
            S = S[:-(f+1)] + '+' + S[-(f+1):]
    else:
        f = S[::-1].find('-')
        S = S[:-(f+1)] + '+' + S[-(f+1):]
        
S = S.split('+')
if S[0] == '':
    S = S[1:]

for j, i in enumerate(S):
    d = i.count('x')
    sign = '+' if i[0] != '-' else '-'
    if j==0 and sign == '+':
        sign = ''
    if d != 0:
        coe = int(i[:-d]) if sign != '-' else int(i[1:-d])
    else:
        coe = int(i[:]) if sign != '-' else int(i[1:])
    a = coe // (d+1)
    s = sign + (str(a) if a != 1 else '') + 'x'*(d+1)
    l.append(s)
    
l.append('+W')

print(''.join(l))