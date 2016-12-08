import unittest
from lib.day_3 import TriangleFinder

class TriangleFinderTestCase(unittest.TestCase):
    def setUp(self):
        self.triangle_finder = TriangleFinder()

    def test_finds_number_of_triangles(self):
        side_lengths = '5 10 25'
        self.triangle_finder.count(side_lengths)
        self.assertEqual(self.triangle_finder.tally, 1)
