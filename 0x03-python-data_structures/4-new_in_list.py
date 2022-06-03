#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element at specific ndex without modifying the whole list"""
    if idx < o or idx > (len(my_list) - 1):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy
