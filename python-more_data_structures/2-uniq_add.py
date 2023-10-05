#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    for i in range(len(my_list)):
        if my_list[i] in my_list[i+1:]:
            my_list[i] = 0
    return sum(my_list)
