def answer(s):
    hallway = list(s.replace("-", ""))
    walking_left = hallway.count("<")
    encounters = 0
    while walking_left > 0:
        for i in hallway:
            if i == ">":
                encounters += walking_left
            else:
                walking_left -= 1
    return encounters * 2

s = ">----<"
print(answer(s))
#10


#    l = list(s.replace("-", ""))
#    if len(l) == 0:
#        return 0
#    while l[0] == "<":
#        del(l[0])
#    while l[-1] == ">":
#        del(l[-1])
#
#    else:
#        return l


