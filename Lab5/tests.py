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
from add import *
from base2 import *
from log import *
from maximum import *


# ----------------------------------------------------------------------

class SetTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def testAdd(self):
        r = add([2, 2, 2, 2])
        self.assertEqual(8, r)
        q = add([74])
        self.assertEqual(74, q)
        t = add([])
        self.assertEqual(0, t)
        y = add((2, 2, 2, 2))
        self.assertEqual(8, y)

    # ------------------------------------------------------------------

    def testBase2AsString(self):
        r = base2AsString(1113)
        self.assertEqual("10001011001", r)
        q = base2AsString(1)
        self.assertEqual("1", q)
        t = base2AsString(-14)
        self.assertEqual("-1110", t)

    # ------------------------------------------------------------------

    def testBase2AsInt(self):
        r = base2AsInt(1113)
        self.assertEqual(10001011001, r)
        q = base2AsInt(1)
        self.assertEqual(1, q)
        t = base2AsInt(-14)
        self.assertEqual(-1110, t)

    # ------------------------------------------------------------------

    def testMaximum(self):
        r = maximum([1, 2, 3, 4, 5])
        self.assertEqual(5, r)
        q = maximum([7, 3, 4, 6])
        self.assertEqual(7, q)
        t = maximum([1, 5, 100, 2, 6])
        self.assertEqual(100, t)
        y = maximum((1, 2, 3, 4, 5))
        self.assertEqual(5, y)

    # ------------------------------------------------------------------

    def testLog(self):
        r = log(1000)
        self.assertEqual(3, r)
        q = log(50392)
        self.assertEqual(4, q)
        t = log(9)
        self.assertEqual(0, t)