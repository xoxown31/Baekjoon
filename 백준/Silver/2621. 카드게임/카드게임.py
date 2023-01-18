l = []

for _ in range(5):
    color, number = input().split()
    l.append([color, int(number)])

colors = [x[0] for x in l]
numbers = [x[1] for x in l]

score = 0

case1 = len(set(colors)) == 1 and sorted(numbers) == [x for x in range(min([x[1] for x in l]), min([x[1] for x in l]) + 5)]
case2 = len(set(numbers)) == 2 and (numbers.count(numbers[0]) == 1 or numbers.count(numbers[0]) == 4)
case3 = len(set(numbers)) == 2
case4 = len(set(colors)) == 1
case5 = sorted(numbers) == [x for x in range(min([x[1] for x in l]), min([x[1] for x in l]) + 5)]
case6 = len(set(numbers)) == 3 and (numbers.count(numbers[0]) == 3 or numbers.count(numbers[1]) == 3 or numbers.count(numbers[2]) == 3)
case7 = len(set(numbers)) == 3
case8 = len(set(numbers)) == 4

if case1:
    score = 900 + max(numbers)

elif case2:

    if numbers.count(l[0][1]) == 1:
        score = 800 + l[1][1]
    else:
        score = 800 + l[0][1]

elif case3:

    a, b = set(numbers)

    if numbers.count(a) == 3:
        score = 700 + 10 * a + b

    else:
        score = 700 + 10 * b + a

elif case4:

    score = 600 + max(numbers)
    
elif case5:

    score = 500 + max(numbers)
    
elif case6:
    
    if numbers.count(numbers[0]) == 3:
        score = 400 + numbers[0]
        
    elif numbers.count(numbers[1]) == 3:
        score = 400 + numbers[1]
        
    else:
        score = 400 + numbers[2]
        
elif case7:
    
    a, b, c = set(numbers)

    if numbers.count(a) == 1:
        score = 300 + 10 * max(b, c) + min(b, c)
    elif numbers.count(b) == 1:
        score = 300 + 10 * max(a, c) + min(a, c)
    else:
        score = 300 + 10 * max(b, a) + min(b, a)
        
elif case8:
    if numbers.count(numbers[0]) == 2:
        score = 200 + numbers[0]
    elif numbers.count(numbers[1]) == 2:
        score = 200 + numbers[1]
    elif numbers.count(numbers[2]) == 2:
        score = 200 + numbers[2]
    else:
        score = 200 + numbers[3]
        
else:
    score = 100 + max(numbers)

print(score)
