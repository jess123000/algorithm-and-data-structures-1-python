#!/usr/bin/env python

#----------------------------------------------------------------------
# ListNode.py
# Alex Harris
# 2/6/2019
#----------------------------------------------------------------------

from __future__ import annotations

#----------------------------------------------------------------------

class ListNode:

    """A single-linked structure"""
    
    #----------------------------------------------------------------------
    
    def __init__(self, item = None, link: ListNode = None):

        """
        creates a node with the specified data value and link
        :param item: item to store in the node
        :param link: reference to the next ListNode
        """
        
        self.item = item
        self.link = link
        
#----------------------------------------------------------------------
