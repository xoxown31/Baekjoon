while True:
    s = input()
    if s == '.':
        break

    l = []

    for i in s:
        if i == '(' or i == '[':
            l.append(i)
        elif i == ')':
            if not l or l[-1] != '(':
                print("no")
                break
            l.pop()
        elif i == ']':
            if not l or l[-1] != '[':
                print("no")
                break
            l.pop()

    else:
        if not l:
            print('yes')
        else:
            print('no')