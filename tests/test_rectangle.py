import unittest
from shape.rectangle import Rectangle
from shape.error import LengthIsNegativeError, WidthIsNegativeError

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rect = Rectangle(10.0, 5.0)

    def test_area(self):
        self.assertEqual(50.0, self.rect.area())

    def test_perimeter(self):
        self.assertEqual(30.0, self.rect.perimeter())

    def test_construct_negative_length(self):
        with self.assertRaises(LengthIsNegativeError):
            rect = Rectangle(-1.0, 5.0)

    def test_change_length_to_negative(self):
        self.rect.set_length(-10.0)
        self.assertEqual(10.0, self.rect.get_length())
        self.rect.set_length(5.0)
        self.assertEqual(5.0, self.rect.get_length())

if __name__ == "__main__":
    unittest.main()