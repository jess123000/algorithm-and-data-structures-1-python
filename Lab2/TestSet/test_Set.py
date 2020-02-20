#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Set.py
# Alex Harris
# CS 161 12pm
# ----------------------------------------------------------------------

import sys
import unittest

# ----------------------------------------------------------------------

sys.path.insert(0, '..')
from Set import *

# ----------------------------------------------------------------------

class SetTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def testInsert(self):
        items = Set()
        items.insert(1)
        items.insert(2)
        items.insert(3)
        items.insert(4)
        items.insert(5)
        self.assertEqual(len(items), 5)
        items2 = Set()
        for i in range(1, 6):
            items2.insert(i)
        self.assertEqual(len(items2), 5)

    # ------------------------------------------------------------------

    def testContains(self):
        items = Set()
        for i in range(1, 6):
            items.insert(i)
        item = 1
        item2 = item in items
        self.assertEqual(item2, True)


    # ------------------------------------------------------------------

    def testRemove(self):
        items = Set()
        for i in range(1, 6):
            items.insert(i)
        items.remove(2)
        self.assertEqual(len(items), 4)

    # ------------------------------------------------------------------

    def testIsSubsetOf(self):
        items = Set()
        for i in range(7):
            items.insert(i)

    # ------------------------------------------------------------------

    def testLen(self):
        items = Set()
        for i in range(1, 6):
            items.insert(i)
        self.assertEqual(len(items), 5)

    # ------------------------------------------------------------------

    def testAdd(self):
        items = Set()
        for i in range(1, 6):
            items.insert(i)
        items2 = Set()
        for i in range(6, 11):
            items2.insert(i)
        items + items2
        self.assertEqual(len(items), 10)

    # ------------------------------------------------------------------

    def testSub(self):
        items = Set()
        for i in range(1, 6):
            items.insert(i)
        items2 = Set()
        for i in range(2, 4):
            items2.insert(i)
        items - items2
        self.assertEqual(len(items), 3)

    # ------------------------------------------------------------------

    def testEq(self):
        items = Set()
        for i in range(1, 6):
            items.insert(i)
        items2 = Set()
        for i in range(1, 6):
            items2.insert(i)
        items3 = items == items2
        self.assertEqual(items3, True)

        items = Set()
        for i in range(1, 6):
            items.insert(i)
        items2 = Set()
        for i in range(6, 11):
            items2.insert(i)
        items3 = items == items2
        self.assertEqual(items3, False)

    # ------------------------------------------------------------------

    def testNe(self):
        items = Set()
        for i in range(1, 6):
            items.insert(i)
        items2 = Set()
        for i in range(1, 6):
            items2.insert(i)
        items3 = items != items2
        self.assertEqual(items3, False)

        items = Set()
        for i in range(1, 6):
            items.insert(i)
        items2 = Set()
        for i in range(6, 11):
            items2.insert(i)
        items3 = items != items2
        self.assertEqual(items3, True)

    # ------------------------------------------------------------------

# ----------------------------------------------------------------------

def main(argv):
    try:
        unittest.main()
    except SystemExit as inst:
        # raised by sys.exit(True) when tests failed
        if inst.args[0] is True:
            raise

# ----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)