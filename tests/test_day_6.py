import unittest
from lib.day_6 import Messenger

class MessengerTestCase(unittest.TestCase):
    def setUp(self):
        self.messenger = Messenger()
        self.signal = 'eedadn\ndrvtee\neandsr\nraavrd\natevrs\ntsrnev\nsdttsa\nrasrtv\nnssdts\nntnada\nsvetve\ntesnvt\nvntsnd\nvrdear\ndvrsen\nenarar'
        with open('tests/input/input_day_6.txt', 'r') as input_file:
            self.puzzle_signal = input_file.read()

    def test_reads_message_from_signal(self):
        message = self.messenger.read(self.signal)
        self.assertEqual(message, 'easter')

        puzzle_message = self.messenger.read(self.puzzle_signal)
        self.assertEqual(puzzle_message, 'ikerpcty')
