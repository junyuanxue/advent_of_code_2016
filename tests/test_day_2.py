import unittest
from lib.day_2 import Decoder
from tests.input.input_day_2 import bathroom_code_instructions

class DecoderTestCase(unittest.TestCase):
    def setUp(self):
        self.decoder = Decoder()
        self.instructions = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD'
        ]
        self.puzzle_input = bathroom_code_instructions

    def test_decodes_instructions(self):
        self.assertEqual(self.decoder.run(self.instructions), '1985')
        self.assertEqual(self.decoder.run(self.puzzle_input), '47978')

    def test_unlocks_funky_keypad(self):
        self.assertEqual(self.decoder.unlock_funky_keypad(self.instructions), '5DB3')
