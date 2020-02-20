#!/usr/bin/env python3

# ----------------------------------------------------------------------
# add.py
# Alex Harris
# 03/14/19
# ----------------------------------------------------------------------

def maximum(items: list) -> float:
    # If the list only contains one item, the maximum is that item
    if len(items) == 1:
        return items[0]
    # else if the length the passed list is two, compare those two
    elif len(items) == 2:
        if items[0] < items[1]:
            return items[1]
        else:
            return items[0]
    #else recursively call add until there is two items in the list and add the two numbers together
    else:
        r = maximum(items[1:])
        if r < items[0]:
            return items[0]
        else:
            return r