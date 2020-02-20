#!/usr/bin/env python3

# ----------------------------------------------------------------------
# base2.py
# Alex Harris
# 03/14/19
# ----------------------------------------------------------------------

from __future__ import annotations

def base2AsString(n: int) -> str:
    multiplier = None
    #if the number is negative, change it to a positive number
    if n / -1 == abs(n):
        multiplier = -1
        n = abs(n)
    # if we aren't to the last division
    if n // 2 != 0:
        #divide by two
        nextNum = n // 2
        #calculate the remainder
        remainder = n % 2
        #recursive call
        answer = base2AsString(nextNum)
        #change the remainder to a str for concatenation
        strRemainder = str(remainder)
        #concatanoate the answer
        answer += strRemainder
        #if the original number was negative, change it back to a negative
        if multiplier == -1:
            answer = int(answer)
            answer *= multiplier
            return str(answer)
        #else return the string
        else:
            return answer
    else:
        #else the remainder is the number
        remainder = n
        answer = str(remainder)
        return answer

# ----------------------------------------------------------------------

def base2AsInt(n: int) -> int:
    multiplier = None
    # if the number is negative, change it to a positive number
    if n / -1 == abs(n):
        multiplier = -1
        n = abs(n)
    # if we aren't to the last division
    if n // 2 != 0:
        # divide by two
        nextNum = n // 2
        #find the remainder
        remainder = n % 2
        # recursive call
        answer = base2AsInt(nextNum)
        #multiply by ten to get to the next placeholder
        answer *= 10
        #if the remainder is 1
        if remainder == 1:
            #add on
            answer += 1
        #if the original answer was negative, negate the answer
        if multiplier == -1:
            answer *= multiplier
            return answer
        #else return the string
        else:
            return answer
    else:
        #else the start of our answer is the remainder which is the number the function was passed
        return n