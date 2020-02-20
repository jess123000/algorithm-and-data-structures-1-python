#!/usr/bin/env python3

#----------------------------------------------------------------------
# test_LListCursor.py
# Alex Harris
# 2/6/2019
#----------------------------------------------------------------------

import unittest
import sys
sys.path.insert(0, '..')

from LListCursor import LListCursor

#----------------------------------------------------------------------

class LListTest(unittest.TestCase):

    #------------------------------------------------------------------

    def checkList(self, linked, lst, cursor):
        self.assertEqual(len(linked), len(lst))
        items = []
        for x in linked:
            items.append(x)
        self.assertEqual(items, lst)
        if len(lst) > 0:
            self.assertEqual(linked.itemAtHead(), lst[0], 'head wrong')
            self.assertEqual(linked.itemAtTail(), lst[-1], 'tail wrong')
            self.assertEqual(linked.itemAtCursor(), cursor, 'cursor wrong')
            
    #------------------------------------------------------------------

    def testInit(self):

        items = LListCursor()
        self.assertEqual(len(items), 0)
    
    #------------------------------------------------------------------

    def testInitInstanceVars(self):

        items = LListCursor()
        self.assertEqual(items.length, 0)
        self.assertEqual(items.head, None)
        self.assertEqual(items.cursor, None)
        self.assertEqual(items.tail, None)
    
    #------------------------------------------------------------------

    def testAtAllRaisesError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.itemAtHead)
        self.assertRaises(IndexError, items.itemAtCursor)
        self.assertRaises(IndexError, items.itemAtTail)

    #------------------------------------------------------------------

    def testInsertAtHead(self):

        items = LListCursor()
        for i in range(3, -1, -1):
            items.insertAtHead(i)
        self.checkList(items, list(range(4)), 3)
    
    #------------------------------------------------------------------

    def testInsertAtTail(self):

        items = LListCursor()
        for i in range(4):
            items.insertAtTail(i)
        self.checkList(items, list(range(4)), 0)

    #------------------------------------------------------------------

    def testInsertAfterCursor(self):

        items = LListCursor()
        for i in (0, 3, 2, 1):
            items.insertAfterCursor(i)
        self.checkList(items, list(range(4)), 0)

    # ------------------------------------------------------------------

    def testABitOfAll(self):

        items = LListCursor()
        items.insertAtHead(2)
        items.insertAtHead(1)
        items.insertAfterCursor(5)
        items.insertAfterCursor(4)
        items.insertAtTail(6)
        items.insertAtTail(7)
        items.insertAfterCursor(3)
        self.checkList(items, list(range(1, 8)), 2)

    # ------------------------------------------------------------------

    def testLength(self):

        items = LListCursor()
        for i in range(5):
            items.insertAtTail(i)
        self.assertEqual(5, len(items))

    # ------------------------------------------------------------------

    def testCursorToStartAndCursorForward(self):

        items = LListCursor()
        for i in range(5):
            items.insertAtTail(i)
        items.cursorForward()
        self.checkList(items, list(range(5)), 1)
        items.cursorForward()
        self.checkList(items, list(range(5)), 2)
        items.cursorForward()
        self.checkList(items, list(range(5)), 3)
        items.cursorForward()
        self.checkList(items, list(range(5)), 4)
        items.cursorForward()
        self.checkList(items, list(range(5)), 4)
        items.cursorToStart()
        self.checkList(items, list(range(5)), 0)

    # ------------------------------------------------------------------

    def testRemoveItemAtHead(self):

        items = LListCursor()
        for i in range(5):
            items.insertAtTail(i)
        items.removeItemAtHead()
        self.checkList(items, list(range(1, 5)), 1)
        items.removeItemAtHead()
        self.checkList(items, list(range(2, 5)), 2)
        items.removeItemAtHead()
        items.removeItemAtHead()
        items.removeItemAtHead()
        self.checkList(items, list(), None)

    # ------------------------------------------------------------------

    def testRemoveItemAtCursor(self):

        items = LListCursor()
        for i in range(5):
            items.insertAtTail(i)
        items.removeItemAtCursor()
        self.checkList(items, list(range(1, 5)), 1)
        items.cursorForward()
        items.cursorForward()
        items.removeItemAtCursor()
        self.checkList(items, [1, 2, 4], 4)
        items.removeItemAtCursor()
        self.checkList(items, list(range(1, 3)), 2)
        items.removeItemAtCursor()
        items.removeItemAtCursor()
        self.checkList(items, list(), None)

    # ------------------------------------------------------------------

    def testRemoveItemAtTail(self):

        items = LListCursor()
        for i in range(5):
            items.insertAtTail(i)
        items.removeItemAtTail()
        self.checkList(items, list(range(4)), 0)
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        items.removeItemAtTail()
        self.checkList(items, list(range(3)), 2)
        items.removeItemAtTail()
        items.removeItemAtTail()
        items.removeItemAtTail()
        self.checkList(items, list(), None)

    # ------------------------------------------------------------------

#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
