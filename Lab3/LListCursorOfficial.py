#!/usr/bin/env python

#----------------------------------------------------------------------
# LListCursor.py
# Dave Reed
# 12/18/2018
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
    
    def __init__(self, *args):

        """
        initializes empty list or list with items in seq if it is not None
        :param seq: optional sequence of items to insert into the list
        """

        self.head = None
        self.cursor = None
        self.tail = None
        self.length = 0
        # if only one argument, see if it is iterable
        if len(args) == 1:
            try:
                # try to insert each item
                for x in args[0]:
                    self.insertAtTail(x)
            except TypeError:
                # exception raised if item not iterable so just insert it
                self.insertAtTail(args[0])
        else:
            # 0 or 2 or more arguments so iterate over them and insert them
            for x in args:
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

        self.length += 1

        # if list is empty
        if self.head is None:
            # create node and set each ListNode instance var to it
            self.head = self.cursor = self.tail = ListNode(item)
        else:
            # create node with new node's link the old head
            # and set head to the newly created node
            self.head = ListNode(item, self.head)

    #------------------------------------------------------------------

    def insertAfterCursor(self, item) -> None:

        """
        insert item after the cursor position
        :param item: value to insert
        :return: None
        """

        if self.cursor == self.tail:
            self.insertAtTail(item)
        else:
            self.length += 1
            # list is not empty since cursor == tail if it is and cursor not at tail
            # create node
            node = ListNode(item, self.cursor.link)
            # connect cursor to the new node
            self.cursor.link = node


    #------------------------------------------------------------------

    def insertAtTail(self, item) -> None:

        """
        insert item at the end of the list
        :param item: value to insert
        :return: None
        """

        self.length += 1
        # if list is empty
        if self.tail is None:
            # create node and set each ListNode instance var to it
            self.head = self.cursor = self.tail = ListNode(item)
        else:
            # add new node onto end of list
            self.tail.link = ListNode(item)
            # update tail to be the new end of the list
            self.tail = self.tail.link

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

        if self.cursor == self.head:
            return self.removeItemAtHead()
        elif self.cursor == self.tail:
            return self.removeItemAtTail()
        else:
            # know we have at least three items in the list
            self.length -= 1
            # get item so can return it later
            item = self.cursor.item

            # need to set link of item before the cursor
            # to item after the cursor

            # find item before the cursor
            precursor = self.head
            while precursor.link != self.cursor:
                precursor = precursor.link
            # update its link
            precursor.link = self.cursor.link

            self.cursor = self.cursor.link
            return item

    #------------------------------------------------------------------

    def removeItemAtTail(self):

        """
        removes last item in the list; IndexError is raised if list is empty
        :return: the item that was removed
        """

        if self.head == self.tail:
            return self.removeItemAtHead()
        else:
            # list is not empty and head != tail
            self.length -= 1
            # get item so can return it later
            item = self.tail.item

            # if now just one item
            if self.length == 1:
                # ListNode instance vars refer to that one item
                self.cursor = self.tail = self.head
                # indicate no item after the first item
                self.head.link = None
            else:
                # check if cursor was at tail
                cursorWasTail = self.cursor == self.tail

                # move tail to item before the last item we deleted
                # start at head
                self.tail = self.head
                # move tail forward to last item
                for i in range(self.length - 1):
                    self.tail = self.tail.link
                # indicate no items after tail
                self.tail.link = None
                # update cursor if it was the tail before the deletion
                if cursorWasTail:
                    self.cursor = self.tail
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

        # if cursor is not None and there is a node after it
        if self.cursor and self.cursor.link:
            # move cursor forward
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
        :return: a new LListCursor that is concatenation of self and other; the
        cursor of it should be at the beginning of the list
        """

        # create new list
        r = LListCursor()
        # iterate over self and add its items to r
        for x in self:
            r.insertAtTail(x)
        # iterate over other and add its items to r
        for x in other:
            r.insertAtTail(x)

        # not necessary
        r.cursor = r.head

        return r

#----------------------------------------------------------------------
