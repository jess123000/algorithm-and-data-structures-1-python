#!/usr/bin/env python
# Stack.py
# Dave Reed
# CS161
# 01/29/2003

#----------------------------------------------------------------------

class Stack:

    #----------------------------------------------------------------------

    def __init__(self):

        """creates an empty stack"""
                
        self.items = []

    #----------------------------------------------------------------------

    def push(self, x):

        """places x on top of the stack"""
        
        self.items.append(x)

    #----------------------------------------------------------------------

    def pop(self):

        """removes and returns the top element of the stack"""
        
        return self.items.pop()

    #----------------------------------------------------------------------

    def top(self):

        """returns the top element of the stack without removing it"""
        
        return self.items[-1]

    #----------------------------------------------------------------------

    def size(self):

        """returns the number of elements in the stack"""
        
        return len(self.items)

#----------------------------------------------------------------------
