#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Set.py
# Alex Harris
# CS 161 12pm
# ----------------------------------------------------------------------

from __future__ import annotations

class Set:

    # ------------------------------------------------------------------

    def __init__(self, *args):
        self.items = []
        for x in args:
            self.insert(x)

    # ------------------------------------------------------------------

    def insert(self, item):
        if item not in self.items:
            self.items.append(item)

    # ------------------------------------------------------------------

    def __contains__(self, item) -> bool:
        return item in self.items

    # ------------------------------------------------------------------

    def remove(self, item) -> None:
        if item in self.items:
            self.items.remove(item)

    # ------------------------------------------------------------------

    def isSubsetOf(self, item: list) -> bool:
        for i in item:
            if i not in self.items:
                return False

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        length = 0
        for i in self.items:
            length += 1
        return length

    # ------------------------------------------------------------------

    def __add__(self, other: list) -> Set:
        for item in other:
            if item not in self.items:
                self.items.append(item)

    # ------------------------------------------------------------------

    def __sub__(self, other: list) -> Set:
        for item in other:
            if item in self.items:
                self.items.remove(item)

    # ------------------------------------------------------------------

    def __eq__(self, other: list) -> bool:
        for item in other:
            if item not in self.items:
                return False
        return True

    # ------------------------------------------------------------------

    def __ne__(self, other: list) -> bool:
        for item in other:
            if item in self.items:
                return False
        return True

    # ------------------------------------------------------------------

    def __iter__(self):
        for x in self.items:
            yield x

    # ------------------------------------------------------------------