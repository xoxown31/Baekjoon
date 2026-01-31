i = 3
while True:
    s = input()

    if s.isdigit():
        break

    i -= 1

x = int(s)+i

if x%3 == 0 and x%5==0:
    print("FizzBuzz")
elif x%3 == 0:
    print("Fizz")
elif x%5 == 0:
    print("Buzz")
else:
    print(x)
