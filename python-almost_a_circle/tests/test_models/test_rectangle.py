#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    def test_triangle_with_two_arguments(self):
        r1 = Rectangle(1, 2)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_triangle_with_tree_argument(self):
        r2 = Rectangle(1, 2, 3)

        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)

    def test_triangle_with_four_arguments(self):
        r3 = Rectangle(1, 2, 3, 4)

        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
    def test_triangle_with_four_arguments(self):
        r4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)
    
    def test_triangle_with_the_first_argument_str(self):
        r5 = Rectangle("1", 2)

        self.assertEqual(r5.width, "1")
        self.assertEqual(r5.height, 2)

    def test_triangle_with_the_second_argument_str(self):
        r6 = Rectangle(1, "2")

        self.assertEqual(r6.width, 1)
        self.assertEqual(r6.height, "2")

    def test_triangle_with_the_third_argument_str(self):
        r7 = Rectangle(1, 2, "3")

        self.assertEqual(r7.width, 1)
        self.assertEqual(r7.height, 2)
        self.assertEqual(r7.x, "3")

    def test_triangle_with_the_fourth_argument_str(self):
        r8 = Rectangle(1, 2, 3, "4")

        self.assertEqual(r8.width, 1)
        self.assertEqual(r8.height, 2)
        self.assertEqual(r8.x, 3)
        self.assertEqual(r8.y, "4")

    def test_triangle_with_the_first_argument_is_negative(self):
        r9 = Rectangle(-1, 2)

        self.assertEqual(r9.width, -1)
        self.assertEqual(r9.height, 2)

    def test_triangle_with_the_second_argument_is_negative(self):
        r10 = Rectangle(1, -2)

        self.assertEqual(r10.width, 1)
        self.assertEqual(r10.height, -2)

    def test_triangle_with_the_third_argument_is_negative(self):
        r11 = Rectangle(1, 2, -3)

        self.assertEqual(r11.width, 1)
        self.assertEqual(r11.height, 2)
        self.assertEqual(r11.x, -3)

    def test_triangle_with_the_fourth_argument_is_negative(self):
        r12 = Rectangle(1, 2, 3, -4)

        self.assertEqual(r12.width, 1)
        self.assertEqual(r12.height, 2)
        self.assertEqual(r12.x, 3)
        self.assertEqual(r12.y, -4)

    def test_triangle_with_the_first_argument_is_zero(self):
        r13 = Rectangle(0, 2)

        self.assertEqual(r13.width, 0)
        self.assertEqual(r13.height, 2)

    def test_triangle_with_the_second_argument_is_zero(self):
        r14 = Rectangle(1, 0)

        self.assertEqual(r14.width, 1)
        self.assertEqual(r14.height, 0)

    if __name__ == "__main__":
        unittest.main()