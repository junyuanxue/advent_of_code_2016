import unittest
from lib.day_8 import Authy

class AuthyTestCase(unittest.TestCase):
    def setUp(self):
        self.authy = Authy()
        self.sequence = 'rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1'
        with open('tests/input/input_day_8.txt', 'r') as input_file:
            self.puzzle_sequence = input_file.read()

    def test_counts_number_of_pixels_lit(self):
        number = self.authy.count_lit_pixels(self.sequence)
        self.assertEqual(number, 6)
