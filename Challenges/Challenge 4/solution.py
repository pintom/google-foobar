def answer(start, length):
    all_ids = range(start, start + length**2, 1)
    length_count = length
    checked_ids = []
    print (all_ids)
    while length_count > 0:
        checked_ids += all_ids[0:length_count]
        del all_ids[0:length]
        length_count -= 1
    print(checked_ids)
    check_sum = checked_ids[0] ^ checked_ids[1]
    for i in checked_ids[2:]:
        check_sum = i ^ check_sum
    return check_sum

print(answer(0, 3))
#print(answer(17, 4))
#print(answer(29, 4))
