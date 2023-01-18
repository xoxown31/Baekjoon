N = int(input())-1
k = N // 14 + 1
a, b = 'tu' + (('ru' * (k+1)) if k+1 < 5 else '+ru*{}'.format(k+1)), 'tu' + (('ru' * k) if k < 5 else '+ru*{}'.format(k))
l = ['baby', 'sukhwan', a, b, 'very', 'cute', a, b, 'in', 'bed', a, b, 'baby', 'sukhwan']
print(l[N%14])
