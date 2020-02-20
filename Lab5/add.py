#!/usr/bin/env python3

# ----------------------------------------------------------------------
# add.py
# Alex Harris
# 03/14/19
# ----------------------------------------------------------------------

def add(items: list):

    #If the list only contains one item, the sum is that item
    if len(items) ==  1:
        return items[0]
    #else if the length the passed list is two, add those two together
    elif len(items) == 2:
        return items[0] + items[1]
    #else if the list is empty, the sum is 0
    elif len(items) == 0:
        return 0
    #else recursively call add until there is two items in the list and add the two numbers together
    else:
        r = add(items[1:])
        r += items[0]
        return r