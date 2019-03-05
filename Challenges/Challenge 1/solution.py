def answer(s):

    x = 1
    i = (s+s).find(s, 1, -1)
    print (i)
    print(s+s)
    if i == -1:
        return x
    else:
        x = s.count(s[:i])
    return x

