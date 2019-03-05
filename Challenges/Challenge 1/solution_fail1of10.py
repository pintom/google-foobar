def answer(s):
    x = []
    res = 1
    s1 = s.lower().replace(" ", "")
    s1 = "".join([i for i in s1 if not i.isdigit()])

    for i in range(len(s1), 1, -1):
        x = [s1[j:j + i] for j in range(0, len(s1), i)]
        if len(set(x)) == 1:
            res1 = len(s1) // i

            if res < res1:
                res = res1
    return res
