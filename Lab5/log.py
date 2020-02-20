#!/usr/bin/env python3

# ----------------------------------------------------------------------
# log.py
# Alex Harris
# 03/14/19
# ----------------------------------------------------------------------

def log(x) -> int:
    if x // 10 >= 1:
        answer = x // 10
        answer = log(answer)
        answer += 1
        return answer
    else:
        answer = 0
        return answer