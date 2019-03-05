def answer(l):
    triples_sets = []
    for i in l:
        for j in l[i:]:
            if j % i == 0:
                for k in l[j:]:
                    if k % j == 0:
                        triples_sets.append([i, j, k])

    return len(triples_sets)
print (answer([1, 1]))
