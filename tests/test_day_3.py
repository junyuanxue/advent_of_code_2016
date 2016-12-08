import unittest
from lib.day_3 import TriangleFinder

class TriangleFinderTestCase(unittest.TestCase):
    def setUp(self):
        self.triangle_finder = TriangleFinder()
        with open('tests/input/input_day_3.txt', 'r') as input_file:
            self.sets = input_file.read()

    def test_finds_number_of_triangles(self):
        side_lengths = '5 10 25'
        self.triangle_finder.count(side_lengths)
        self.assertEqual(self.triangle_finder.tally, 0)

        three_sets = '458 70 645\n3 4 5\n7 10 14'
        self.triangle_finder.count(three_sets)
        self.assertEqual(self.triangle_finder.tally, 2)
