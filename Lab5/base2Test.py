#!/usr/bin/env python3

# ----------------------------------------------------------------------
# base2.py
# Alex Harris
# 03/14/19
# ----------------------------------------------------------------------

def base2AsString(n: int) -> str:
    multipler = None
    #if the number is negative, change it to a positive number
    if n / -1 == abs(n):
        multipler = -1
        n = abs(n)
    # if we aren't to the last division
    if n // 2 != 0:
        #divide by two
        nextNum = n // 2
        #calculate the remainder
        remainder = nextNum * 2
        remainder = n - remainder
        #recursive call
        answer = base2AsString(nextNum)
        #change the remainder to a str for concatenation
        strRemainder = str(remainder)
        #concatanoate the answer
        answer += strRemainder
        #if the original number was negative, change it back to a negative
        if multipler == -1:
            answer = int(answer)
            answer *= multipler
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
        # calculate the remainder
        remainder = nextNum * 2
        remainder = n - remainder
        # recursive call
        answer = base2AsInt(nextNum)

        #figure out whether the next number will make the answer in the 10s, 100s, 1000s, etc.
        ansMulti = len(str(answer))
        ansMulti = 10 ** ansMulti
        #if the remainder is 0
        if remainder == 0:
            # the answer will be the answer plus answer multiplier (which will be 10, 100, 1000, etc.)
            # minus 10 to the length of the answer minus one (which will be 9, 90, 900, etc.)
            # this will give the answer 10, then 100, then 1000, if all the remainders are 0 from the first number
            answer += (ansMulti - 10 ** (len(str(answer)) - 1))
        else:
            #else the answer is the same thing
            answer += (ansMulti - 10 ** (len(str(answer)) - 1))
            #plus the 1 to account for the remainder being 1 instead of 0
            answer += 1
        if multiplier == -1:
            answer *= multiplier
            return answer
        #else return the string
        else:
            return answer
    else:
        #else the start of our answer is the remainder which is the number the function was passed
        return n