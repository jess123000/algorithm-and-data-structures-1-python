#!/usr/bin/env python

#----------------------------------------------------------------------
# LListCursor.py
# Alex Harris
# 2/6/2019
#----------------------------------------------------------------------

from __future__ import annotations

from ListNode import ListNode

#----------------------------------------------------------------------

class LListCursor:

    """LListCursor is a linked list where you can add/remove/access
    items at beginning, end, and a cursor position in the list

    class invariant:

        1. if the list is empty, self.head, self.cursor, self.tail are
        all None
        
        2. if the list is not empty, self.head, self.cursor, and
        self.tail all point to an appropriate ListNode; self.head
        points to the first ListNode; self.tail points to the last
        ListNode; self.cursor points to a ListNode in the list

        3. inserting an item should not change self.cursor unless the
        list was empty, in which case self.cursor points to the one
        item in the list

        4. when deleting at the head or tail, self.cursor stays where
        it is unless it was at the head or tail; if cursor was at the
        head and the head was deleted, self.cursor now refers to the
        ListNode after it. if self.cursor was at the tail and the tail
        is deleted, self.cursor now refers to the ListNode before it

        5. when deleting the item at the cursor, self.cursor now
        refers to the ListNode after it, unless there is no ListNode
        after it in which case it refers to the ListNode before it.

        6. self.length indicates the number of items in the LListCursor
        """
        
    #------------------------------------------------------------------
    
    def __init__(self, seq=None):

        """
        initializes empty list or list with items in seq if it is not None
        :param seq: optional sequence of items to insert into the list
        """

        self.head = None
        self.cursor = None
        self.tail = None
        self.length = 0
        if seq is not None:
            for x in seq:
                self.insertAtTail(x)

    #------------------------------------------------------------------

    def __len__(self) -> int:

        """
        :return: number of items in the list
        """

        return self.length

    #------------------------------------------------------------------

    def insertAtHead(self, item) -> None:

        """
        inserts item at the beginning of the list
        :param item: value to insert
        :return: None
        """

        #if the list is empty, insert to the beginning create all the variables
        if self.head is None:
            self.head = ListNode(item)
            self.cursor = self.head
            self.tail = self.head
        else:
            #if there's already a head save it, replace it, relink it
            prevNode = self.head
            self.head = ListNode(item, prevNode)
        self.length += 1

    #------------------------------------------------------------------

    def insertAfterCursor(self, item) -> None:

        """
        insert item after the cursor position
        :param item: value to insert
        :return: None
        """

        #if the list is empty, insert to the beginning create all the variables
        if self.head is None:
            self.head = ListNode(item)
            self.cursor = self.head
            self.tail = self.head
        else:
            #save the node already connected to the cursor
            prevNode = self.cursor.link
            #create the new node
            node = ListNode(item)
            #link the new node to the cursor
            self.cursor.link = node
            #link the new node to the previous link
            node.link = prevNode
            #if the cursor was the tail, make the new node the tail
            if self.cursor == self.tail:
                self.tail = node
        self.length += 1

    #------------------------------------------------------------------

    def insertAtTail(self, item) -> None:

        """
        insert item at the end of the list
        :param item: value to insert
        :return: None
        """

        # if the list is empty, insert to the beginning create all the variables
        if self.head is None:
            self.head = ListNode(item)
            self.cursor = self.head
            self.tail = self.head
        else:
            #create the new node, connect it to the tail, update the tail
            node = ListNode(item)
            self.tail.link = node
            self.tail = node
        self.length += 1

    #------------------------------------------------------------------

    def removeItemAtHead(self):

        """
        removes first item in the list; IndexError is raised if list is empty
        :return: the item that was removed
        """

        if self.length == 0:
            # raise IndexError if list is empty
            raise IndexError('removeItemAtHead called on empty LListCursor')
        else:
            self.length -= 1
            # get item so can return it later
            item = self.head.item
            # if list is empty after the deletion
            if self.length == 0:
                # make all ListNode instance vars None
                self.head = self.cursor = self.tail = None
            else:
                # if cursor was at head
                if self.cursor == self.head:
                    # move cursor forward to new first item
                    self.cursor = self.cursor.link
                # move head forward to new first item
                self.head = self.head.link

        return item

    #------------------------------------------------------------------

    def removeItemAtCursor(self):

        """
        removes item in the list that is at the cursor; IndexError is raised if list is empty;
        the cursor now points to the node after the original cursor unless the cursor was the
        last item in which case the cursor is now the new last item'
        :return: the item that was removed
        """

        if self.length == 0:
            # raise IndexError if list is empty
            raise IndexError('removeItemAtCursor called on empty LListCursor')
        else:
            self.length -= 1
            #save item to return
            item = self.cursor.item
            #if the list is empty after removing, reset all the values
            if self.length == 0:
                self.head = self.cursor = self.tail = None
            else:
                #prepare to find node before the cursor
                prevNode = self.head
                #if cursor is at the head, move the head
                if self.cursor == self.head:
                    self.head = self.cursor.link
                    self.cursor = self.head
                else:
                    #go through the nodes until the one before the cursor is found
                    while prevNode.link is not self.cursor:
                        prevNode = prevNode.link
                    #once previous is found, relink it to the new cursor
                    prevNode.link = self.cursor.link
                    #if the cursor is the tail, move the tail and cursor to the prevNode
                    if self.cursor == self.tail:
                        self.tail = prevNode
                        self.cursor = prevNode
                    #else make the new cursor the node after the cursor being deleted
                    else:
                        self.cursor = prevNode.link

        return item

    #------------------------------------------------------------------

    def removeItemAtTail(self):

        """
        removes last item in the list; IndexError is raised if list is empty
        :return: the item that was removed
        """

        if self.length == 0:
            # raise IndexError if list is empty
            raise IndexError('removeItemAtTail called on empty LListCursor')
        else:
            self.length -= 1
            #save item to return
            item = self.cursor.item
            # if the list is empty after removing, reset all the values
            if self.length == 0:
                self.head = self.cursor = self.tail = None
            else:
                # find the node before the tail
                prevNode = self.head
                while prevNode.link is not self.tail:
                    prevNode = prevNode.link
                # if cursor is at the tail, move the cursor to the one before to the one before
                if self.tail == self.cursor:
                    #link the cursor to the node before the one being deleted
                    self.cursor = prevNode
                self.tail = prevNode
                self.tail.link = None

        return item

    #------------------------------------------------------------------

    def itemAtHead(self):

        """
        returns first item; IndexError is raised if list is empty
        :return: first item in list
        """

        if self.length == 0:
            # raise IndexError if list is empty
            raise IndexError('itemAtHead called on empty LListCursor')
        else:
            return self.head.item

    #------------------------------------------------------------------

    def itemAtCursor(self):

        """
        returns item at cursor; IndexError is raised if list is empty
        :return: item at cursor
        """

        if self.length == 0:
            # raise IndexError if list is empty
            raise IndexError('itemAtCursor called on empty LListCursor')
        else:
            return self.cursor.item

    #------------------------------------------------------------------

    def itemAtTail(self):

        """
        returns list item; IndexError is raised if list is empty
        :return: first last in list
        """
        if self.length == 0:
            # raise IndexError if list is empty
            raise IndexError('itemAtTail called on empty LListCursor')
        else:
            return self.tail.item

    #------------------------------------------------------------------

    def cursorToStart(self) -> None:

        """
        move cursor to start/head of list
        :return:
        """
        
        self.cursor = self.head
            
    #------------------------------------------------------------------

    def cursorForward(self) -> bool:

        """
        move cursor forward one item
        :return: True if cursor was moved forward or False if list empty or cursor already at end of list
        """

        #if the cursor isn't the tail and the list isn't empty, move the cursor forward
        if self.cursor.link is not None and self.cursor is not None:
            self.cursor = self.cursor.link
            return True
        return False
    
    #------------------------------------------------------------------

    def __iter__(self):

        """
        iterates over items in list yielding one item at a time
        """

        # start at beginning of list
        node = self.head
        # while nodes left
        while node is not None:
            # yield item
            yield node.item
            # and move node forward
            node = node.link

    #------------------------------------------------------------------

    def __add__(self, other: LListCursor) -> LListCursor:

        """
        returns a new LListCursor that is the concatenation of self and other
        :param other: another LListCursor to concatenate with self
        :return: a new LListCursor that is concatenation of self and other
        """

        pass

#----------------------------------------------------------------------
