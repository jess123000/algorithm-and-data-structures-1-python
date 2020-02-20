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
from inToPost import *

# ----------------------------------------------------------------------

class SetTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def testInToPost(self):
        userInfix = "3 * ( 4 + 5 ) - 2 + ( 3 * 6 )"
        postfix = inToPost(userInfix)
        self.assertEqual(postfix, "3 4 5 + * 2 - 3 6 * +")
        userInfix = "( 3 + 4 ) * 10 + 4 * 5"
        postfix = inToPost(userInfix)
        self.assertEqual(postfix, "3 4 + 10 * 4 5 * +")

    # ------------------------------------------------------------------

    def testEvalPostfix(self):
        postfix = "3 4 5 + * 2 - 3 6 * +"
        evaluation = evalPostfix(postfix)
        self.assertEqual(evaluation, 43)
        postfix = "3 4 + 10 * 4 5 * +"
        evaluation = evalPostfix(postfix)
        self.assertEqual(evaluation, 90)

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