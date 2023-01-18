while True:
    s = input()
    if s == 'end':
        break
    res = ""
    p = ""
    vc = 0
    pc = 0
    for i in s:
        if i in 'aeiou':
            if p in 'aeiou' and p != '':
                pc += 1
            else:
                pc = 0
            vc += 1
        else:
            if p not in 'aeiou' and p != '':
                pc += 1
            else:
                pc = 0
        if p == i and p not in 'eo':
            res = "not "
            break
        if pc == 2:
            res = "not "
            break
        p = i

    if vc == 0:
        res = "not "

    print("<{}> is {}acceptable.".format(s, res))
