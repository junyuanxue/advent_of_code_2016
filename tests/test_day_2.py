import unittest
from lib.day_2 import Decoder
from tests.input.input_day_2 import bathroom_code_instructions

class DecoderTestCase(unittest.TestCase):
    def setUp(self):
        self.decoder = Decoder()
        self.puzzle_input = bathroom_code_instructions

    def test_decodes_instructions(self):
        instructions = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD'
        ]
        self.assertEqual(self.decoder.run(instructions), '1985')
