#!/usr/bin/env python
# inToPost.py
# Alex Harris
# CS161
# 2/21/19

#----------------------------------------------------------------------

from Stack import *

#----------------------------------------------------------------------

def checkPrecedence(x, stack):
    top = stack.top()

    # if the top is a ( then it does not have equal or greater precedence otherwise, it does
    if top == "(":
        return False
    elif x == "+" or x == "-":
        return True
    else:
        if top == "+" or x == "-":
            return False
        return True

#----------------------------------------------------------------------

def inToPost(infix):
    infixList = infix.split(" ")
    # get a list and Stack ready to add to
    postfixList = []
    stack = Stack()

    for x in infixList:
        # if x is a ( push it onto the stack
        if x == "(":
            stack.push(x)
        # else if it's an operator
        elif x == "+" or x == "-" or x == "*" or x == "/":
            # check the stack size to see if we need to check for precedence
            size = stack.size()
            # if there's something in the stack, check precedence
            if size != 0:
                pop = checkPrecedence(x, stack)
            #while the stack isn't empty and the stack.top() has equal or greater precedence
            while (stack.size() != 0) and (pop):
                #pop the operator at the top of the stack and append it onto the postfix list
                operator = stack.pop()
                postfixList.append(operator)
            # push the x operator no matter what
            stack.push(x)
        # else if x is a )
        elif x == ")":
            # while the top of the stack isn't a )
            while stack.top() != "(":
                # pop the operator that must be there and append it onto the postfix list
                operator = stack.pop()
                postfixList.append(operator)
            # after popping all the operators between the ( ), pop the (
            stack.pop()
        elif x == " ":
            pass
        # else x is a number
        else:
            # append the number onto the postfix list
            postfixList.append(x)
    # once to the end of the infix list, pop the remaining operators and append them onto the postfix list
    while stack.size() != 0:
        operator = stack.pop()
        postfixList.append(operator)
    # join all the postfix list into a single string
    postfix = ' '.join(postfixList)

    return postfix

#----------------------------------------------------------------------

def evalPostfix(postfix):
    stack = Stack()

    postfixList = postfix.split(' ')

    for x in postfixList:
        # if x is +, -, *, or / pop two numbers from the top and apply the operator
        if x == "+":
            numberOne = stack.pop()
            numberTwo = stack.pop()
            newNumber = numberTwo + numberOne
            stack.push(newNumber)
        elif x == "-":
            numberOne = stack.pop()
            numberTwo = stack.pop()
            newNumber = numberTwo - numberOne
            stack.push(newNumber)
        elif x == "*":
            numberOne = stack.pop()
            numberTwo = stack.pop()
            newNumber = numberTwo * numberOne
            stack.push(newNumber)
        elif x == "/":
            numberOne = stack.pop()
            numberTwo = stack.pop()
            newNumber = numberTwo / numberOne
            stack.push(newNumber)
        else:
            # else if it's a number, push it onto the stack
            number = float(x)
            stack.push(number)

    # pop and return the solution
    solution = stack.pop()

    return solution

#----------------------------------------------------------------------

def main():
    userInfix = input("Please enter your infix with spaces: ")
    postfix = inToPost(userInfix)
    evaluation = evalPostfix(postfix)
    print("postfix is", postfix)
    print("the solution to the postfix is", evaluation)

#----------------------------------------------------------------------

if __name__ == "__main__":
    main()