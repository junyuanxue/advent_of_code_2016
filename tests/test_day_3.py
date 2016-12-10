import unittest
from lib.day_3 import TriangleFinder

class TriangleFinderTestCase(unittest.TestCase):
    def setUp(self):
        self.triangle_finder = TriangleFinder()
        with open('tests/input/input_day_3.txt', 'r') as input_file:
            self.puzzle_sets = input_file.read()

    def test_finds_number_of_triangles(self):
        side_lengths = '5 10 25'
        tally_1 = self.triangle_finder.count(side_lengths)
        self.assertEqual(tally_1, 0)

        three_sets = '458 70 645\n3 4 5\n7 10 14'
        tally_2 = self.triangle_finder.count(three_sets)
        self.assertEqual(tally_2, 2)

        puzzle_tally = self.triangle_finder.count(self.puzzle_sets)
        self.assertEqual(puzzle_tally, 983)

    def test_targets_triangles_by_column(self):
        side_lengths = '101 301 501\n102 302 502\n103 303 503\n201 401 601\n202 402 602\n203 403 603'
        tally_1 = self.triangle_finder.count_by_column(side_lengths)
        self.assertEqual(tally_1, 6)

        puzzle_tally = self.triangle_finder.count_by_column(self.puzzle_sets)
        self.assertEqual(puzzle_tally, 1836)
