#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    def test_rectangle_with_two_arguments(self):
        r1 = Rectangle(1, 2)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_rectangle_with_tree_argument(self):
        r2 = Rectangle(1, 2, 3)

        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)

    def test_rectangle_with_four_arguments(self):
        r3 = Rectangle(1, 2, 3, 4)

        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
    def test_rectangle_with_five_arguments(self):
        r4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)
    
    def test_rectangle_with_the_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r5 = Rectangle("1", 2)


    def test_rectangle_with_the_heigt_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r6 = Rectangle(1, "2")

    def test_rectangle_with_the_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r7 = Rectangle(1, 2, "3")

    def test_rectangle_with_the_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r8 = Rectangle(1, 2, 3, "4")

    def test_rectangle_with_the_width_is_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r9 = Rectangle(-1, 2)

    def test_rectangle_with_the_heigth_is_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10 = Rectangle(1, -2)

    def test_rectangle_with_the_x_is_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r11 = Rectangle(1, 2, -3)

    def test_rectangle_with_the_y_is_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r12 = Rectangle(1, 2, 3, -4)

    def test_rectangle_with_the_width_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r13 = Rectangle(0, 2)

    def test_rectangle_with_the_heigth_is_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r14 = Rectangle(1, 0)

    def test_rectangle_method_area(self):
        r15 = Rectangle(1, 2)

        self.assertEqual(r15.area(), 2)

    if __name__ == "__main__":
        unittest.main()