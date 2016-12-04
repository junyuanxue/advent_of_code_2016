import unittest
from lib.day_1 import BlockCalculator

class BlockCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.block_calculator = BlockCalculator()

    def test_run(self):
        input_1 = 'R2, L3'
        self.assertEqual(self.block_calculator.run(input_1), 5)

        input_2 = 'R2, R2, R2'
        self.assertEqual(self.block_calculator.run(input_2), 2)

        input_3 = 'R5, L5, R5, R3'
        self.assertEqual(self.block_calculator.run(input_3), 12)
