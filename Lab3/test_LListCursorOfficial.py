#!/usr/bin/env python3

#----------------------------------------------------------------------
# test_LListCursor.py
# Dave Reed
# 12/18/2018
#----------------------------------------------------------------------

import unittest
import sys
sys.path.insert(0, '..')

from LListCursor import LListCursor

#----------------------------------------------------------------------

class LListTest(unittest.TestCase):

    #------------------------------------------------------------------

    def checkList(self, linked, lst, cursorValue):
        self.assertEqual(len(linked), len(lst), f"length is not {len(lst)}")
        items = []
        for x in linked:
            items.append(x)
        self.assertEqual(items, lst)
        if len(lst) > 0:
            headItem = linked.itemAtHead()
            tailItem = linked.itemAtTail()
            cursorItem = linked.itemAtCursor()
            self.assertEqual(headItem, lst[0], f"head wrong: should be {lst[0]}, but is {headItem}")
            self.assertEqual(tailItem, lst[-1], f"tail wrong: should be {lst[-1]}, but is {tailItem}")
            self.assertEqual(cursorItem, cursorValue, f"cursor wrong: should be {cursorValue}, but is {cursorItem}")
            
    #------------------------------------------------------------------

    def testInit(self):

        items = LListCursor()
        self.assertEqual(len(items), 0)
    
    #------------------------------------------------------------------

    def testInitSeq(self):

        items = LListCursor(list(range(4)))
        self.checkList(items, list(range(4)), 0)
        self.assertEqual(len(items), 4)
    
    #------------------------------------------------------------------

    def testInitInstanceVars(self):

        items = LListCursor()
        self.assertEqual(items.length, 0)
        self.assertEqual(items.head, None)
        self.assertEqual(items.cursor, None)
        self.assertEqual(items.tail, None)
    
    #------------------------------------------------------------------

    def testItemAtHeadRaisesIndexError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.itemAtHead)

    #------------------------------------------------------------------

    def testItemAtCursorRaisesIndexError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.itemAtCursor)

    #------------------------------------------------------------------

    def testItemAtTailRaisesIndexError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.itemAtTail)

    #------------------------------------------------------------------

    def testRemoveItemAtHeadRaisesIndexError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.removeItemAtHead)
    
    #------------------------------------------------------------------

    def testRemoveItemAtCursorRaisesIndexError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.removeItemAtCursor)
    
    #------------------------------------------------------------------

    def testRemoveItemAtTailRaisesIndexError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.removeItemAtTail)
    
    #------------------------------------------------------------------

    def testInsertAtHead(self):

        items = LListCursor()
        for i in range(3, -1, -1):
            items.insertAtHead(i)
        self.checkList(items, list(range(4)), 3)
    
    #------------------------------------------------------------------

    def testInsertAfterCursor(self):

        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
            items.cursorForward()
        self.checkList(items, list(range(4)), 3)
        
    #------------------------------------------------------------------

    def testInsertAfterCursor2(self):

        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
        self.checkList(items, [0, 3, 2, 1], 0)

    #------------------------------------------------------------------

    def testInsertAfterCursor3(self):

        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
        self.checkList(items, [0, 3, 2, 1], 0)

    #------------------------------------------------------------------

    def testInsertAtTail(self):

        items = LListCursor()
        for i in range(4):
            items.insertAtTail(i)
        self.checkList(items, list(range(4)), 0)
            
    #------------------------------------------------------------------

    def testRemoveItemAtHead(self):

        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
            items.cursorForward()
        self.checkList(items, list(range(4)), 3)

        a = list(range(4))
        for i in range(4):
            self.assertEqual(items.removeItemAtHead(), i)
            a.pop(0)
            self.checkList(items, a, 3)
            
    #------------------------------------------------------------------

    def testRemoveItemAtHead2(self):

        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
            items.cursorForward()
        self.checkList(items, list(range(4)), 3)

        items.cursorToStart()
        self.checkList(items, list(range(4)), 0)
        
        a = list(range(4))
        for i in range(4):
            self.assertEqual(items.removeItemAtHead(), i)
            a.pop(0)
            if len(a) > 0:
                cursor = a[0]
            else:
                cursor = None
            self.checkList(items, a, cursor)
        
    #------------------------------------------------------------------

    def testRemoveItemAtCursor(self):

        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
            items.cursorForward()
        self.checkList(items, list(range(4)), 3)

        self.assertEqual(items.removeItemAtCursor(), 3)
        self.checkList(items, [0, 1, 2], 2)
        items.cursorToStart()
        items.cursorForward()
        self.checkList(items, [0, 1, 2], 1)
        self.assertEqual(items.removeItemAtCursor(), 1)
        self.checkList(items, [0, 2], 2)
        items.cursorToStart()
        self.checkList(items, [0, 2], 0)
        self.assertEqual(items.removeItemAtCursor(), 0)
        self.checkList(items, [2,], 2)
        self.assertEqual(items.removeItemAtCursor(), 2)
        self.checkList(items, [], None)

    #------------------------------------------------------------------

    def testRemoveItemAtCursor2(self):

        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
            items.cursorForward()
        items.cursorToStart()
        self.assertEqual(items.removeItemAtCursor(), 0)
        self.checkList(items, [1, 2, 3], 1)

        self.assertEqual(items.removeItemAtCursor(), 1)
        self.checkList(items, [2, 3], 2)

        self.assertEqual(items.removeItemAtCursor(), 2)
        self.checkList(items, [3,], 3)

        self.assertEqual(items.removeItemAtCursor(), 3)
        self.checkList(items, [], None)

    #------------------------------------------------------------------

    def testRemoveItemAtTail(self):
        
        items = LListCursor()
        for i in range(4):
            items.insertAfterCursor(i)
            items.cursorForward()
        self.checkList(items, list(range(4)), 3)
        self.assertEqual(items.removeItemAtTail(), 3)
        self.checkList(items, [0, 1, 2], 2)
        
        items.cursorToStart()
        items.cursorForward()
        self.checkList(items, [0, 1, 2], 1)
        self.assertEqual(items.removeItemAtTail(), 2)
        self.checkList(items, [0, 1], 1)
        items.cursorToStart()
        self.checkList(items, [0, 1], 0)
        self.assertEqual(items.removeItemAtTail(), 1)
        self.checkList(items, [0,], 0)
        
    #------------------------------------------------------------------

    def testAddEmpty(self):
        
        a = LListCursor()
        for i in range(4):
            a.insertAfterCursor(i)
            a.cursorForward()
        a.cursorToStart()
        a.cursorForward()

        b = LListCursor()
        c = a + b
        self.checkList(a, list(range(4)), 1)
        self.checkList(c, list(range(4)), 0)
        
        
    #------------------------------------------------------------------

    def testAddEmpty2(self):
        
        a = LListCursor()
        for i in range(4):
            a.insertAfterCursor(i)
            a.cursorForward()
        a.cursorToStart()
        a.cursorForward()

        b = LListCursor()
        c = b + a
        self.checkList(a, list(range(4)), 1)
        self.checkList(c, list(range(4)), 0)
        
    #------------------------------------------------------------------

    def testAdd(self):
        
        a = LListCursor()
        for i in range(4):
            a.insertAfterCursor(i)
            a.cursorForward()
        a.cursorToStart()
        a.cursorForward()

        b = LListCursor()
        for i in range(4, 8):
            b.insertAfterCursor(i)
            b.cursorForward()
        c = a + b

        # make certain that __add__ does not change parameter
        self.checkList(a, list(range(4)), 1)
        self.checkList(b, list(range(4, 8)), 7)

        # make certain __add__ returns correct result
        self.checkList(c, list(range(8)), 0)

    #------------------------------------------------------------------

    def testExampleFromClass(self):
        a = LListCursor()
        a.insertAtHead(3)
        self.checkList(a, [3], 3)
        a.insertAtHead(2)
        self.checkList(a, [2, 3], 3)
        a.insertAtTail(4)
        self.checkList(a, [2, 3, 4], 3)
        a.insertAfterCursor(5)
        self.checkList(a, [2, 3, 5, 4], 3)
        a.cursorForward()
        self.checkList(a, [2, 3, 5, 4], 5)
        a.removeItemAtCursor()
        self.checkList(a, [2, 3, 4], 4)

    #------------------------------------------------------------------

#----------------------------------------------------------------------

def main():
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main()
