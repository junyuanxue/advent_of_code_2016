import unittest
from lib.day_1 import BlockCalculator

class BlockCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.block_calculator = BlockCalculator()
        self.puzzle_input = 'L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1'

    def test_calculate_total_blocks_away(self):
        input_1 = 'R2, L3'
        self.block_calculator.run(input_1)
        self.assertEqual(self.block_calculator.totalBlocksAway, 5)

        input_2 = 'R2, R2, R2'
        self.block_calculator.run(input_2)
        self.assertEqual(self.block_calculator.totalBlocksAway, 2)

        input_3 = 'R5, L5, R5, R3'
        self.block_calculator.run(input_3)
        self.assertEqual(self.block_calculator.totalBlocksAway, 12)

        self.block_calculator.run(self.puzzle_input)
        self.assertEqual(self.block_calculator.totalBlocksAway, 209)

    def test_calculate_distance_from_first_revisted_block(self):
        test_input = 'R8, R4, R4, R8'
        self.block_calculator.run(test_input)
        self.assertEqual(self.distance, 4)
