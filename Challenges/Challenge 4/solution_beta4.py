def answer(start, length):
    ans = 0
    for l in xrange(length - 1, -1, -1):
        print(l)
        b = start + l
        ans ^= (b, 1, b + 1, 0)[b % 4] ^ (0, start - 1, 1, start, 0)[start % 4]
        start += length
    return ans
#print(answer(20000000000, 39))
#print(answer(17, 4))
print(answer(0, 3))
