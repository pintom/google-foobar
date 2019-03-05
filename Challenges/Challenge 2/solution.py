def answer(x, y):
    id = sum(range(x+1))
    if y == 1:
        return id
    if y == 2:
        id += x
        return id
    else:
        while y > 1:
            id += x
            x += 1
            y -= 1
    return id




