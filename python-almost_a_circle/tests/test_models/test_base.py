#!/usr/bin/python3

import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):
    def test_automatic_id(self):
        b1 = Base()

        self.assertEqual(b1.id, 1)

    def test_automatic_increment(self):
        b2 = Base()
        b3 = Base()

        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_saving_ted_id(self):
        b4 = Base(89)

        self.assertEqual(b4.id, 89)

    def test_to_json_string_none(self):

    if __name__ == "__main__":
        unittest.main()