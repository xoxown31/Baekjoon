t = ''
inp = input()
if inp.count('-') > 0:
    i = inp.find('-')
    plus = sum(map(int, inp[:i].replace('+', '-').split('-')))
    minus = sum(map(int, inp[i+1:].replace('+', '-').split('-')))
    print(plus - minus)
else:
    print(sum(map(int, inp.split('+'))))
