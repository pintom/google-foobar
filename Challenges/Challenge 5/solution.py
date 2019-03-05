def answer(l):
    n = len(l)
    triples_set = []
    triples_count = {}
    for i in xrange(0, n-1):
        for j in xrange(i+1, n):
            if l[j] % l[i] == 0:
                triples_set.append(j)
                triples_count[i] = triples_count.get(i, 0) + 1
    triples_sum = 0
    for v in triples_set:
        triples_sum += triples_count.get(v, 0)

    return triples_sum
print (answer([1, 1, 1]))
